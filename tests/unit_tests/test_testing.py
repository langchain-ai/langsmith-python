import asyncio
import datetime
import uuid
from unittest.mock import MagicMock

import pytest

from langsmith import run_helpers as rh
from langsmith import testing as t
from langsmith import utils as ls_utils
from langsmith.testing import _internal
from langsmith.testing._internal import (
    _arun_test,
    _get_example_id,
    _LangSmithTestSuite,
    _run_test,
    _serde_example_values,
    _TestCase,
)


def test__serde_example_values():
    class Foo:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    results = _serde_example_values({"foo": Foo(1, 2)})
    assert "foo" in results
    assert isinstance(results["foo"], str)


def test__get_id():
    class Foo:
        bar: str = "baz"  # type: ignore

        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b

    def foo(x: Foo):
        return x

    dataset_id = "4e32bff6-5762-4906-8d74-ee2bd0f1d234"
    inputs = {"x": Foo(1, 2)}
    outputs = {"y": Foo(3, 4)}

    result = _get_example_id(dataset_id, inputs, outputs)
    assert isinstance(result, uuid.UUID)


def test_log_inputs_updates_test_case_inputs():
    """Test that calling log_inputs updates _TestCase.inputs.

    When a test has fixture params (e.g. model: BaseChatModel), the initial
    inputs captured from the function signature include the fixture values.
    Calling log_inputs should update self.inputs so that example ID generation
    in end_run uses the correct inputs.
    """
    mock_test_suite = MagicMock()
    mock_test_suite.id = uuid.uuid4()

    test_case = _TestCase(
        test_suite=mock_test_suite,
        run_id=uuid.uuid4(),
        inputs={"model": "<fixture object>", "db": "<db fixture>"},
    )

    # Before log_inputs, inputs reflect fixtures
    assert test_case.inputs == {"model": "<fixture object>", "db": "<db fixture>"}

    # User calls t.log_inputs({"question": "fix typo"}) inside their test.
    # The global log_inputs merges into run_tree then passes run_tree.inputs
    # to test_case.log_inputs. Simulate that merged result:
    test_case.log_inputs({"question": "fix typo"})

    assert test_case.inputs == {"question": "fix typo"}

    # Verify the example ID is now derived from the logged inputs,
    # not the original fixture-based inputs
    dataset_id = str(mock_test_suite.id)
    expected_id = _get_example_id(dataset_id, {"question": "fix typo"})
    fixture_id = _get_example_id(dataset_id, {"model": "<fixture object>", "db": "<db fixture>"})
    # end_run falls back to _get_example_id when no explicit id is set
    actual_id = _get_example_id(dataset_id, test_case.inputs or {})
    assert actual_id == expected_id
    assert actual_id != fixture_id


def test_pytest_feedback_includes_experiment_id_and_run_start_time():
    experiment_id = uuid.uuid4()
    run_id = uuid.uuid4()
    start_time = datetime.datetime.now(datetime.timezone.utc)
    test_suite = object.__new__(_LangSmithTestSuite)
    test_suite.client = MagicMock()
    test_suite._experiment = MagicMock(id=experiment_id)
    test_suite._executor = MagicMock()
    test_suite._executor.submit.side_effect = lambda fn, *args, **kwargs: fn(*args, **kwargs)

    test_suite._submit_result(run_id, start_time, 1)
    test_suite._submit_feedback(
        run_id,
        {"key": "quality", "score": 0.75},
        start_time=start_time,
    )

    assert test_suite.client.create_feedback.call_count == 2
    for call in test_suite.client.create_feedback.call_args_list:
        assert call.args[0] == run_id
        assert call.kwargs["session_id"] == experiment_id
        assert call.kwargs["start_time"] == start_time


def _make_tracked_test_case(monkeypatch):
    test_suite = MagicMock()
    test_suite.id = uuid.uuid4()
    test_suite.name = "test-suite"
    test_suite.client.api_url = "https://api.smith.langchain.com"
    test_case = _TestCase(test_suite=test_suite, run_id=uuid.uuid4(), inputs={})
    monkeypatch.setattr(_internal, "_create_test_case", lambda *args, **kwargs: test_case)
    return test_case


@pytest.fixture
def tracing_env_unset(monkeypatch):
    for var in ("LANGSMITH_TRACING", "LANGSMITH_TRACING_V2", "LANGCHAIN_TRACING", "LANGCHAIN_TRACING_V2"):
        monkeypatch.delenv(var, raising=False)
    ls_utils.get_env_var.cache_clear()
    yield
    ls_utils.get_env_var.cache_clear()


def test_log_functions_work_with_tracking_on_and_tracing_env_unset(monkeypatch, tracing_env_unset):
    """Test tracking alone must be enough for log_* (issue #107)."""
    test_case = _make_tracked_test_case(monkeypatch)
    client = MagicMock()
    seen = {}

    def tracked_test():
        t.log_inputs({"q": "2+2"})
        t.log_outputs({"a": 4})
        seen["run_tree"] = rh.get_current_run_tree()

    assert ls_utils.tracing_is_enabled() is False
    with rh.tracing_context(client=client):
        _run_test(tracked_test, pytest_request=None, langtest_extra={"cache": None, "cached_hosts": None})

    run_tree = seen["run_tree"]
    assert run_tree is not None
    assert run_tree.id == test_case.run_id
    assert run_tree.inputs == {"q": "2+2"}
    assert run_tree.outputs == {"a": 4}
    assert test_case.inputs == {"q": "2+2"}
    # The test's root run was posted to the experiment's project.
    client.create_run.assert_called_once()
    assert client.create_run.call_args.kwargs["session_name"] == "test-suite"


def test_async_log_functions_work_with_tracking_on_and_tracing_env_unset(monkeypatch, tracing_env_unset):
    test_case = _make_tracked_test_case(monkeypatch)
    client = MagicMock()
    seen = {}

    async def tracked_test():
        t.log_inputs({"q": "2+2"})
        t.log_outputs({"a": 4})
        seen["run_tree"] = rh.get_current_run_tree()

    with rh.tracing_context(client=client):
        asyncio.run(_arun_test(tracked_test, pytest_request=None, langtest_extra={"cache": None, "cached_hosts": None}))

    run_tree = seen["run_tree"]
    assert run_tree is not None
    assert run_tree.id == test_case.run_id
    assert run_tree.outputs == {"a": 4}
    client.create_run.assert_called_once()


def test_explicitly_disabled_tracing_is_respected(monkeypatch, tracing_env_unset):
    _make_tracked_test_case(monkeypatch)
    client = MagicMock()
    seen = {}

    def tracked_test():
        seen["run_tree"] = rh.get_current_run_tree()

    with rh.tracing_context(client=client, enabled=False):
        _run_test(tracked_test, pytest_request=None, langtest_extra={"cache": None, "cached_hosts": None})

    assert seen["run_tree"] is None
    client.create_run.assert_not_called()
