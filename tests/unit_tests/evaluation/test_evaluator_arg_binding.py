"""Evaluators with extra defaulted params must still get the right inputs."""

import inspect
from unittest.mock import MagicMock

import pytest

from langsmith.evaluation import evaluator as ls_evaluator
from langsmith.evaluation._runner import _evaluator_uses_attachments
from langsmith.evaluation.evaluator import (
    _normalize_comparison_evaluator_func,
    _normalize_evaluator_func,
)

OUTPUTS = {"answer": "x"}
REFERENCE = {"answer": "y"}


@pytest.fixture
def run():
    run = MagicMock()
    run.inputs = {"q": 1}
    run.outputs = OUTPUTS
    return run


@pytest.fixture
def example():
    example = MagicMock()
    example.inputs = {"q": 1}
    example.outputs = REFERENCE
    example.attachments = {}
    return example


def _check(outputs, threshold, reference_outputs):
    assert threshold == 0.5
    assert reference_outputs == REFERENCE
    return {"key": "k", "score": 1}


def ev_skip_middle(outputs, threshold=0.5, reference_outputs=None):
    return _check(outputs, threshold, reference_outputs)


def ev_skip_middle_kwonly(outputs, threshold=0.5, *, reference_outputs=None):
    return _check(outputs, threshold, reference_outputs)


def ev_skip_middle_posonly(outputs, threshold=0.5, reference_outputs=None, /):
    return _check(outputs, threshold, reference_outputs)


def ev_default_last(outputs, reference_outputs, threshold=0.5):
    return _check(outputs, threshold, reference_outputs)


ROW_EVALUATORS = [
    ev_skip_middle,
    ev_skip_middle_kwonly,
    ev_skip_middle_posonly,
    ev_default_last,
]


@pytest.mark.parametrize("func", ROW_EVALUATORS)
def test_row_evaluator_binds_mapped_args_by_name(func, run, example):
    wrapper, prepare_inputs = _normalize_evaluator_func(func)
    assert wrapper(run, example) == {"key": "k", "score": 1}
    assert prepare_inputs is not None
    _, _, traced = prepare_inputs(run, example)
    assert traced == {"outputs": OUTPUTS, "reference_outputs": REFERENCE}


@pytest.mark.parametrize("func", ROW_EVALUATORS)
async def test_async_row_evaluator_binds_mapped_args_by_name(func, run, example):
    async def afunc(*args, **kwargs):
        return func(*args, **kwargs)

    afunc.__signature__ = inspect.signature(func)  # type: ignore[attr-defined]
    wrapper, _ = _normalize_evaluator_func(afunc)
    assert await wrapper(run, example) == {"key": "k", "score": 1}


def cmp_skip_middle(outputs, threshold=0.5, reference_outputs=None):
    assert outputs == [OUTPUTS, OUTPUTS]
    assert threshold == 0.5
    assert reference_outputs == REFERENCE
    return {"key": "k", "scores": {}}


@pytest.mark.parametrize("is_async", [False, True])
async def test_comparison_evaluator_binds_mapped_args_by_name(is_async, run, example):
    func = cmp_skip_middle
    if is_async:

        async def afunc(*args, **kwargs):
            return cmp_skip_middle(*args, **kwargs)

        afunc.__signature__ = inspect.signature(cmp_skip_middle)  # type: ignore[attr-defined]
        func = afunc  # type: ignore[assignment]
    wrapper, _ = _normalize_comparison_evaluator_func(func)
    result = wrapper([run, run], example)
    if is_async:
        result = await result  # type: ignore[misc]
    assert result == {"key": "k", "scores": {}}


@pytest.mark.parametrize(
    "func",
    [
        lambda outputs, threshold=0.5, reference_outputs=None: None,
        lambda outputs, threshold=0.5, /, reference_outputs=None: None,
    ],
)
def test_summary_style_binding(func):
    # Same helper the summary evaluator wrapper uses.
    arg_map = {"outputs": [OUTPUTS], "reference_outputs": [REFERENCE]}
    args, kwargs = ls_evaluator._bind_mapped_args(inspect.signature(func), arg_map)
    bound = inspect.signature(func).bind(*args, **kwargs)
    bound.apply_defaults()
    assert bound.arguments == {
        "outputs": [OUTPUTS],
        "threshold": 0.5,
        "reference_outputs": [REFERENCE],
    }


def test_bind_mapped_args_keeps_plain_positional_calls():
    def ev(outputs, reference_outputs, *, run=None):
        pass

    args, kwargs = ls_evaluator._bind_mapped_args(
        inspect.signature(ev),
        {"outputs": 1, "reference_outputs": 2, "run": 3},
    )
    assert args == [1, 2]
    assert kwargs == {"run": 3}


def _ev_attachments_positional(outputs, attachments):
    pass


def _ev_attachments_kwonly(outputs, *, attachments):
    pass


def _ev_no_attachments(outputs, *, reference_outputs):
    pass


def _ev_attachments_var_kw(outputs, **attachments):
    pass


@pytest.mark.parametrize(
    "func, expected",
    [
        (_ev_attachments_positional, True),
        (_ev_attachments_kwonly, True),
        (_ev_no_attachments, False),
        (_ev_attachments_var_kw, False),
    ],
)
def test_evaluator_uses_attachments(func, expected):
    assert _evaluator_uses_attachments(func) is expected
