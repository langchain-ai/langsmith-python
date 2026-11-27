"""Tests for the explicit `status` field on run end/patch."""

import asyncio
import json
from unittest import mock

from langsmith import Client, run_trees
from langsmith._internal._operations import (
    serialize_run_dict,
    serialized_run_operation_to_multipart_parts_and_context,
)
from langsmith.run_helpers import trace


class _Marker:
    ls_run_status = "cancelled"


def _tree(client):
    return run_trees.RunTree(name="r", inputs={}, client=client)


def test_end_sets_status_and_patch_forwards_it():
    client = mock.MagicMock()
    rt = _tree(client)
    rt.end(error="boom", status="cancelled")
    rt.patch()
    assert client.update_run.call_args.kwargs["status"] == "cancelled"
    assert client.update_run.call_args.kwargs["error"] == "boom"


def test_status_default_none():
    client = mock.MagicMock()
    rt = _tree(client)
    rt.end(error="boom")
    rt.patch()
    assert client.update_run.call_args.kwargs["status"] is None


def test_later_error_does_not_inherit_earlier_cancel():
    rt = _tree(mock.MagicMock())
    rt.end(error="Cancelled", status="cancelled")
    rt.end(error="real failure")
    assert rt.status is None


def test_cancel_without_error_after_real_error_does_not_relabel():
    rt = _tree(mock.MagicMock())
    rt.end(error="real failure")
    rt.end(status="cancelled")
    assert rt.error == "real failure"
    assert rt.status is None


def test_update_run_puts_status_in_main_json_part_only():
    client = Client(api_url="http://localhost:1", api_key="k", auto_batch_tracing=False)
    captured = {}
    with mock.patch.object(Client, "_update_run", lambda self, d, **kw: captured.update(d)):
        client.update_run("00000000-0000-0000-0000-000000000001", error="e", status="cancelled")
    assert captured["status"] == "cancelled"
    op = serialize_run_dict("patch", dict(captured, trace_id=captured["id"]))
    parts = serialized_run_operation_to_multipart_parts_and_context(op)[0].parts
    names = [p[0] for p in parts]
    assert not any(n.endswith(".status") for n in names)
    main = next(p for p in parts if p[0] == f"patch.{op.id}")
    assert json.loads(main[1][1])["status"] == "cancelled"


def test_status_from_exception():
    f = run_trees.run_status_from_exception
    assert f(ValueError()) is None
    assert f(asyncio.CancelledError()) is None
    assert f(asyncio.CancelledError("x")) is None
    assert f(asyncio.CancelledError(_Marker())) == "cancelled"
    # A marked exception wrapped in an ordinary exception is a plain failure.
    assert f(RuntimeError(_Marker())) is None
    e = ValueError()
    e.ls_run_status = "interrupted"  # type: ignore[attr-defined]
    assert f(e) == "interrupted"


def test_trace_exit_marks_cancelled():
    client = mock.MagicMock()
    try:
        with trace("t", client=client, project_name="p") as rt:
            raise asyncio.CancelledError(_Marker())
    except asyncio.CancelledError:
        pass
    assert rt.status == "cancelled"
    assert rt.error


def test_trace_exit_unmarked_stays_error():
    client = mock.MagicMock()
    try:
        with trace("t", client=client, project_name="p") as rt:
            raise asyncio.CancelledError()
    except asyncio.CancelledError:
        pass
    assert rt.status is None
    assert rt.error


def test_claude_orphans_cancelled_only_when_conversation_cancelled():
    pytest = __import__("pytest")
    pytest.importorskip("claude_agent_sdk")
    from langsmith.integrations.claude_agent_sdk._hooks import (
        SessionState,
        clear_active_tool_runs,
    )

    for cancelled, expected in ((True, "cancelled"), (False, None)):
        session = SessionState()
        session.cancelled = cancelled
        tool = mock.MagicMock()
        session.active_tool_runs["t1"] = (tool, 0.0)
        clear_active_tool_runs(session)
        assert tool.end.call_args.kwargs["status"] == expected
        # The flag is per response: the next one starts clean.
        assert session.cancelled is False


class Interrupt(Exception):
    """Carries the marker as a class attribute, as LangGraph's interrupts do."""

    ls_run_status = "interrupted"


class GraphInterrupt(Exception):
    """Named like LangGraph's but without the marker: not recognized by name."""


def test_class_attribute_marker_is_interrupted():
    assert run_trees.run_status_from_exception(Interrupt("x")) == "interrupted"


def test_unmarked_graph_interrupt_named_class_has_no_status():
    assert run_trees.run_status_from_exception(GraphInterrupt("x")) is None


def test_unknown_marker_value_is_ignored():
    e = Interrupt("x")
    e.ls_run_status = "success"  # type: ignore[assignment]
    assert run_trees.run_status_from_exception(e) is None


def _trace_raising(exc):
    from langsmith import traceable, tracing_context

    captured = {}

    @traceable(client=mock.MagicMock())
    def step():
        raise exc

    with mock.patch.object(
        run_trees.RunTree,
        "patch",
        lambda self, *a, **k: captured.update(status=self.status, error=self.error),
    ):
        with tracing_context(enabled=True):
            try:
                step()
            except type(exc):
                pass
    return captured


def test_traceable_marked_exception_is_interrupted():
    captured = _trace_raising(Interrupt("pause"))
    assert captured["status"] == "interrupted"
    assert captured["error"]


def test_traceable_unmarked_graph_interrupt_named_class_stays_error():
    captured = _trace_raising(GraphInterrupt("pause"))
    assert captured["status"] is None
    assert captured["error"]


def _capture_patches():
    captured = []
    patcher = mock.patch.object(
        run_trees.RunTree,
        "patch",
        lambda self, *a, **k: captured.append((self.status, self.error)),
    )
    return captured, patcher


def test_traceable_generator_closed_early_is_cancelled():
    from langsmith import traceable, tracing_context

    @traceable(client=mock.MagicMock())
    def gen():
        yield 1
        yield 2

    captured, patcher = _capture_patches()
    with patcher, tracing_context(enabled=True):
        g = gen()
        next(g)
        g.close()
    assert captured and captured[-1][0] == "cancelled"
    assert captured[-1][1]


def test_traceable_async_generator_closed_early_is_cancelled():
    from langsmith import traceable, tracing_context

    @traceable(client=mock.MagicMock())
    async def agen():
        yield 1
        yield 2

    async def main():
        g = agen()
        await g.__anext__()
        await g.aclose()

    captured, patcher = _capture_patches()
    with patcher, tracing_context(enabled=True):
        asyncio.run(main())
    assert captured and captured[-1][0] == "cancelled"


def test_traceable_generator_exhausted_or_failing_is_not_cancelled():
    from langsmith import traceable, tracing_context

    @traceable(client=mock.MagicMock())
    def ok():
        yield 1

    @traceable(client=mock.MagicMock())
    def boom():
        yield 1
        raise RuntimeError("x")

    captured, patcher = _capture_patches()
    with patcher, tracing_context(enabled=True):
        list(ok())
        try:
            list(boom())
        except RuntimeError:
            pass
    assert [c[0] for c in captured] == [None, None]
    assert captured[0][1] is None and captured[1][1]
