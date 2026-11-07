"""Unit tests for OpenAI wrapper processing functions."""

from types import SimpleNamespace

import pytest

from langsmith import run_helpers
from langsmith.wrappers._openai import (
    _infer_invocation_params,
    _process_chat_completion,
    _reduce_chat,
    _reduce_response_events,
    _traceable_kwargs_with_ls_agent_type,
)

# ---------------------------------------------------------------------------
# _infer_invocation_params
# ---------------------------------------------------------------------------


def test_infer_invocation_params_copies_request_metadata():
    result = _infer_invocation_params(
        "chat",
        "openai",
        {},
        False,
        {
            "model": "gpt-4o-mini",
            "metadata": {
                "customer_id": "customer-123",
                "environment": "test",
            },
        },
    )

    assert result["customer_id"] == "customer-123"
    assert result["environment"] == "test"
    assert "metadata" not in result["ls_invocation_params"]


def test_infer_invocation_params_protects_langsmith_metadata():
    result = _infer_invocation_params(
        "chat",
        "openai",
        {},
        False,
        {
            "model": "gpt-4o-mini",
            "metadata": {
                "ls_provider": "other",
                "ls_model_name": "other-model",
            },
        },
    )

    assert result["ls_provider"] == "openai"
    assert result["ls_model_name"] == "gpt-4o-mini"


@pytest.mark.parametrize("metadata", [None, "invalid", ["invalid"]])
def test_infer_invocation_params_ignores_non_mapping_metadata(metadata):
    result = _infer_invocation_params(
        "chat",
        "openai",
        {},
        False,
        {"model": "gpt-4o-mini", "metadata": metadata},
    )

    assert result["ls_provider"] == "openai"
    assert result["ls_model_name"] == "gpt-4o-mini"


def test_infer_invocation_params_no_longer_stamps_ls_agent_type():
    result = _infer_invocation_params("chat", "openai", {}, False, {"model": "gpt-4o-mini"})
    assert "ls_agent_type" not in result


def test_per_call_kwargs_metadata_ls_agent_type_flows_through():
    result = _infer_invocation_params(
        "chat",
        "openai",
        {},
        False,
        {"model": "gpt-4o-mini", "metadata": {"ls_agent_type": "middleware"}},
    )
    assert result["ls_agent_type"] == "middleware"


# ---------------------------------------------------------------------------
# _traceable_kwargs_with_ls_agent_type
# ---------------------------------------------------------------------------


def test_traceable_kwargs_stamps_root_at_top_level(monkeypatch):
    monkeypatch.setattr(run_helpers, "get_current_run_tree", lambda: None)
    result = _traceable_kwargs_with_ls_agent_type({})
    assert result["metadata"]["ls_agent_type"] == "root"


@pytest.mark.parametrize("wrapper_tag", ["root", "middleware", "subagent", "compaction"])
def test_traceable_kwargs_preserves_user_supplied_tag(monkeypatch, wrapper_tag):
    monkeypatch.setattr(run_helpers, "get_current_run_tree", lambda: None)
    result = _traceable_kwargs_with_ls_agent_type({"metadata": {"ls_agent_type": wrapper_tag}})
    assert result["metadata"]["ls_agent_type"] == wrapper_tag


def test_traceable_kwargs_preserves_none_opt_out(monkeypatch):
    """None passes through so traceable's .update() sets ls_agent_type=None on
    the run, overriding any propagated parent tag."""
    monkeypatch.setattr(run_helpers, "get_current_run_tree", lambda: None)
    result = _traceable_kwargs_with_ls_agent_type({"metadata": {"ls_agent_type": None}})
    assert result["metadata"]["ls_agent_type"] is None


def test_traceable_kwargs_does_not_mutate_input(monkeypatch):
    monkeypatch.setattr(run_helpers, "get_current_run_tree", lambda: None)
    original: dict = {"metadata": {"custom": "value"}}
    original_metadata = original["metadata"]
    _traceable_kwargs_with_ls_agent_type(original)
    assert original == {"metadata": {"custom": "value"}}
    assert original["metadata"] is original_metadata


def test_traceable_kwargs_preserves_other_user_metadata(monkeypatch):
    monkeypatch.setattr(run_helpers, "get_current_run_tree", lambda: None)
    result = _traceable_kwargs_with_ls_agent_type({"metadata": {"customer_id": "cust-123"}})
    assert result["metadata"]["customer_id"] == "cust-123"
    assert result["metadata"]["ls_agent_type"] == "root"


# ---------------------------------------------------------------------------
# End-to-end (helper decision + traceable outer_metadata merge)
# ---------------------------------------------------------------------------


def _simulate_child_metadata(parent_metadata, wrapper_metadata=None):
    from langsmith._internal import _context

    parent_runtree = SimpleNamespace(extra={"metadata": parent_metadata})
    token = _context._METADATA.set(dict(parent_metadata))
    prev_get = run_helpers.get_current_run_tree
    run_helpers.get_current_run_tree = lambda: parent_runtree
    try:
        helper_out = _traceable_kwargs_with_ls_agent_type(wrapper_metadata or {})
        child_metadata = {**(_context._METADATA.get() or {})}
        child_metadata.update(helper_out.get("metadata") or {})
        return {"helper_output": helper_out, "child_metadata": child_metadata}
    finally:
        _context._METADATA.reset(token)
        run_helpers.get_current_run_tree = prev_get


@pytest.mark.parametrize("parent_tag", ["root", "middleware", "subagent", "compaction"])
def test_propagation_carries_parent_tag_to_nested_llm_run(parent_tag):
    result = _simulate_child_metadata({"ls_agent_type": parent_tag})
    assert "ls_agent_type" not in result["helper_output"]["metadata"]
    assert result["child_metadata"].get("ls_agent_type") == parent_tag


def test_no_tag_on_nested_when_parent_untagged():
    result = _simulate_child_metadata({})
    assert "ls_agent_type" not in result["helper_output"]["metadata"]
    assert "ls_agent_type" not in result["child_metadata"]


def test_user_wrapper_tag_overrides_propagation():
    result = _simulate_child_metadata(
        parent_metadata={"ls_agent_type": "root"},
        wrapper_metadata={"metadata": {"ls_agent_type": "middleware"}},
    )
    assert result["child_metadata"].get("ls_agent_type") == "middleware"


def test_nested_none_opt_out_overrides_propagated_tag():
    """User's None at wrapper level overrides a propagated middleware tag,
    landing ls_agent_type=None on the child (backend treats null as no-tag).
    """
    result = _simulate_child_metadata(
        parent_metadata={"ls_agent_type": "middleware"},
        wrapper_metadata={"metadata": {"ls_agent_type": None}},
    )
    assert "ls_agent_type" in result["child_metadata"]
    assert result["child_metadata"]["ls_agent_type"] is None


# ---------------------------------------------------------------------------
# _reduce_response_events
# ---------------------------------------------------------------------------


def _response_event(event_type: str, status: str, **response_fields):
    from openai.types.responses import Response
    from openai.types.responses import (
        ResponseCompletedEvent,
        ResponseFailedEvent,
        ResponseIncompleteEvent,
    )

    event_cls = {
        "response.completed": ResponseCompletedEvent,
        "response.incomplete": ResponseIncompleteEvent,
        "response.failed": ResponseFailedEvent,
    }[event_type]
    response = Response(
        id="resp_1",
        created_at=0,
        model="gpt-4o-mini",
        object="response",
        output=response_fields.pop("output", []),
        parallel_tool_calls=True,
        tool_choice="auto",
        tools=[],
        status=status,
        **response_fields,
    )
    return event_cls(type=event_type, response=response, sequence_number=1)


def _usage():
    return {
        "input_tokens": 12,
        "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
        "output_tokens": 7,
        "output_tokens_details": {"reasoning_tokens": 0},
        "total_tokens": 19,
    }


def test_reduce_response_events_completed():
    event = _response_event("response.completed", "completed", usage=_usage())

    outputs = _reduce_response_events([event])

    assert outputs["status"] == "completed"
    assert outputs["usage_metadata"]["total_tokens"] == 19


def test_reduce_response_events_keeps_incomplete_response():
    event = _response_event(
        "response.incomplete",
        "incomplete",
        usage=_usage(),
        incomplete_details={"reason": "max_output_tokens"},
    )

    outputs = _reduce_response_events([event])

    assert outputs["status"] == "incomplete"
    assert outputs["incomplete_details"] == {"reason": "max_output_tokens"}
    assert outputs["usage_metadata"]["output_tokens"] == 7


def test_reduce_response_events_keeps_failed_response():
    event = _response_event(
        "response.failed",
        "failed",
        error={"code": "server_error", "message": "boom"},
    )

    outputs = _reduce_response_events([event])

    assert outputs["status"] == "failed"
    assert outputs["error"]["message"] == "boom"


def test_reduce_response_events_without_terminal_event():
    assert _reduce_response_events([]) == {}


def test_wrap_openai_tracing_extra_address_reaches_the_run():
    from unittest import mock

    import langsmith as ls
    from langsmith import Client
    from langsmith.wrappers._openai import _get_wrapper

    address = ls.agent_address("support", "production")
    client = Client(session=mock.MagicMock(), api_key="test", api_url="http://x")
    seen = {}

    def create(**kwargs):
        seen["address"] = run_helpers.get_current_run_tree().address
        return {}

    wrapped = _get_wrapper(
        create,
        "ChatOpenAI",
        lambda chunks: {},
        tracing_extra={"client": client, "address": address},
    )
    with ls.tracing_context(enabled=True):
        wrapped(model="gpt-4o-mini")

    assert seen["address"] == address


# ---------------------------------------------------------------------------
# service tier usage metadata
# ---------------------------------------------------------------------------


def _chat_chunks(service_tier):
    from openai.types.chat import ChatCompletionChunk
    from openai.types.chat.chat_completion_chunk import Choice, ChoiceDelta
    from openai.types.completion_usage import (
        CompletionTokensDetails,
        CompletionUsage,
        PromptTokensDetails,
    )

    common = dict(
        id="chatcmpl-1",
        created=0,
        model="gpt-5",
        object="chat.completion.chunk",
        service_tier=service_tier,
    )
    return [
        ChatCompletionChunk(
            choices=[
                Choice(
                    index=0,
                    delta=ChoiceDelta(role="assistant", content="hi"),
                    finish_reason="stop",
                )
            ],
            **common,
        ),
        ChatCompletionChunk(
            choices=[],
            usage=CompletionUsage(
                prompt_tokens=100,
                completion_tokens=50,
                total_tokens=150,
                prompt_tokens_details=PromptTokensDetails(cached_tokens=20),
                completion_tokens_details=CompletionTokensDetails(reasoning_tokens=10),
            ),
            **common,
        ),
    ]


@pytest.mark.parametrize("tier", ["priority", "flex"])
def test_streamed_chat_usage_uses_service_tier(tier):
    usage = _reduce_chat(_chat_chunks(tier))["usage_metadata"]

    assert usage["input_token_details"] == {f"{tier}_cache_read": 20, tier: 80}
    assert usage["output_token_details"] == {f"{tier}_reasoning": 10, tier: 40}


@pytest.mark.parametrize("tier", ["priority", "flex"])
def test_streamed_and_non_streamed_chat_usage_match(tier):
    from openai.types.chat import ChatCompletion

    chunks = _chat_chunks(tier)
    completion = ChatCompletion(
        id="chatcmpl-1",
        created=0,
        model="gpt-5",
        object="chat.completion",
        service_tier=tier,
        choices=[
            {
                "index": 0,
                "finish_reason": "stop",
                "message": {"role": "assistant", "content": "hi"},
            }
        ],
        usage=chunks[-1].usage,
    )

    assert _reduce_chat(chunks)["usage_metadata"] == _process_chat_completion(completion)["usage_metadata"]
