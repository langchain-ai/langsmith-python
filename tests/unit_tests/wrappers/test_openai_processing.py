"""Unit tests for OpenAI wrapper processing functions."""

from types import SimpleNamespace

import pytest

from langsmith import run_helpers
from langsmith.wrappers._openai import (
    _infer_invocation_params,
    _reduce_chat,
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
# _reduce_chat: streamed tool calls
# ---------------------------------------------------------------------------


def _tool_call_chunks(*tool_call_deltas, finish_reason="tool_calls"):
    """Stream the deltas through a real OpenAI client, which parses SSE chunks
    without validation (as it does for provider responses)."""
    import json

    import httpx
    import openai

    def sse_chunk(delta, finish=None):
        chunk = {
            "id": "chatcmpl-1",
            "object": "chat.completion.chunk",
            "created": 0,
            "model": "test-model",
            "choices": [{"index": 0, "delta": delta, "finish_reason": finish}],
        }
        return f"data: {json.dumps(chunk)}\n\n"

    body = "".join(sse_chunk({"role": "assistant", "tool_calls": [tc]}) for tc in tool_call_deltas)
    body += sse_chunk({}, finish_reason) + "data: [DONE]\n\n"
    transport = httpx.MockTransport(
        lambda request: httpx.Response(200, headers={"content-type": "text/event-stream"}, content=body.encode())
    )
    client = openai.OpenAI(
        api_key="test", base_url="http://localhost/v1", http_client=httpx.Client(transport=transport)
    )
    stream = client.chat.completions.create(
        model="test-model", messages=[{"role": "user", "content": "hi"}], stream=True
    )
    return list(stream)


def _traced_tool_calls(chunks):
    tool_calls = _reduce_chat(chunks)["choices"][0]["message"]["tool_calls"]
    return [(tc["id"], tc["function"]["name"], tc["function"]["arguments"]) for tc in tool_calls]


def test_reduce_chat_parallel_tool_calls_with_index():
    chunks = _tool_call_chunks(
        {"index": 0, "id": "call_paris", "type": "function", "function": {"name": "get_weather", "arguments": ""}},
        {"index": 0, "function": {"arguments": '{"city":'}},
        {"index": 1, "id": "call_tokyo", "type": "function", "function": {"name": "get_weather", "arguments": ""}},
        {"index": 0, "function": {"arguments": '"Paris"}'}},
        {"index": 1, "function": {"arguments": '{"city":"Tokyo"}'}},
    )
    assert _traced_tool_calls(chunks) == [
        ("call_paris", "get_weather", '{"city":"Paris"}'),
        ("call_tokyo", "get_weather", '{"city":"Tokyo"}'),
    ]


def test_reduce_chat_parallel_tool_calls_without_index():
    # Gemini's OpenAI-compatible API (shape from a captured gemini-3.5-flash stream):
    # each parallel call arrives whole in its own chunk, with no index, and the
    # turn ends with finish_reason "stop".
    chunks = _tool_call_chunks(
        {
            "extra_content": {"google": {"thought_signature": "Ev4ECvsE"}},
            "function": {"arguments": '{"city":"Paris"}', "name": "get_weather"},
            "id": "call_4234484",
            "type": "function",
        },
        {
            "function": {"arguments": '{"city":"Tokyo"}', "name": "get_weather"},
            "id": "call_4234487",
            "type": "function",
        },
        finish_reason="stop",
    )
    assert _traced_tool_calls(chunks) == [
        ("call_4234484", "get_weather", '{"city":"Paris"}'),
        ("call_4234487", "get_weather", '{"city":"Tokyo"}'),
    ]


def test_reduce_chat_unindexed_tool_call_fragments_continue_latest_call():
    chunks = _tool_call_chunks(
        {"id": "call_paris", "type": "function", "function": {"name": "get_weather", "arguments": '{"city":'}},
        {"function": {"arguments": '"Paris"}'}},
    )
    assert _traced_tool_calls(chunks) == [("call_paris", "get_weather", '{"city":"Paris"}')]


def test_reduce_chat_unindexed_fragments_repeating_the_same_id_stay_one_call():
    chunks = _tool_call_chunks(
        {"id": "call_paris", "type": "function", "function": {"name": "get_weather", "arguments": '{"city":'}},
        {"id": "call_paris", "function": {"arguments": '"Paris"}'}},
    )
    assert _traced_tool_calls(chunks) == [("call_paris", "get_weather", '{"city":"Paris"}')]
