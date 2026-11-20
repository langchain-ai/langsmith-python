"""Unit tests for copying LLM Gateway response metadata onto wrapped client runs."""

import json
from unittest.mock import MagicMock

import httpx
import pytest

from langsmith import run_trees
from langsmith.run_helpers import trace, tracing_context

# A non-provider host keeps the VCR fixture from recording or replaying these calls.
_GATEWAY_URL = "http://gateway.test"
_GATEWAY_HEADER = {
    "request_id": "0199a1b2-0000-7000-8000-000000000001",
    "outcome": "success",
    "provider": "anthropic",
    "model": "claude-sonnet",
    "attempts": 2,
    "attempt_details": [{"candidate": 1, "status_code": 429}],
    "fallback_used": True,
    "guard_applied": True,
    "guard_redaction_applied": False,
    "source_api_type": "openai",
}
_EXPECTED_INFO = _GATEWAY_HEADER
_OPENAI_COMPLETION = {
    "id": "chatcmpl-1",
    "object": "chat.completion",
    "created": 0,
    "model": "gpt-4o-mini",
    "choices": [
        {
            "index": 0,
            "message": {"role": "assistant", "content": "hi"},
            "finish_reason": "stop",
        }
    ],
}
_ANTHROPIC_MESSAGE = {
    "id": "msg_1",
    "type": "message",
    "role": "assistant",
    "model": "claude-sonnet",
    "content": [{"type": "text", "text": "hi"}],
    "stop_reason": "end_turn",
    "usage": {"input_tokens": 1, "output_tokens": 1},
}
_ANTHROPIC_STREAM_EVENTS = [
    {"type": "message_start", "message": {**_ANTHROPIC_MESSAGE, "content": []}},
    {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}},
    {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "hi"}},
    {"type": "content_block_stop", "index": 0},
    {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 1}},
    {"type": "message_stop"},
]
_GEMINI_RESPONSE = {
    "candidates": [{"content": {"role": "model", "parts": [{"text": "hi"}]}, "finishReason": "STOP"}],
    "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "totalTokenCount": 2},
}


def _handler(gateway_header, body=_OPENAI_COMPLETION, events=None):
    def handle(request: httpx.Request) -> httpx.Response:
        headers = {}
        if gateway_header is not None:
            headers["x-langsmith-gateway-metadata"] = gateway_header
        if events is None:
            return httpx.Response(200, json=body, headers=headers)
        # Anthropic names each event; Gemini sends data lines only.
        sse = "".join((f"event: {e['type']}\n" if "type" in e else "") + f"data: {json.dumps(e)}\n\n" for e in events)
        headers["content-type"] = "text/event-stream"
        return httpx.Response(200, content=sse.encode(), headers=headers)

    return handle


def _capture_run():
    runs: list[run_trees.RunTree] = []
    extra = {"on_end": runs.append, "client": MagicMock()}
    return runs, extra


def _openai_client(gateway_header, is_async=False):
    openai = pytest.importorskip("openai")
    from langsmith.wrappers import wrap_openai

    transport = httpx.MockTransport(_handler(gateway_header))
    if is_async:
        return wrap_openai(
            openai.AsyncOpenAI(
                api_key="test", base_url=_GATEWAY_URL, http_client=httpx.AsyncClient(transport=transport)
            )
        )
    return wrap_openai(
        openai.OpenAI(api_key="test", base_url=_GATEWAY_URL, http_client=httpx.Client(transport=transport))
    )


@pytest.mark.parametrize(
    "gateway_header, expected",
    [
        (json.dumps(_GATEWAY_HEADER), _EXPECTED_INFO),
        (None, None),
        ("not-json", None),
    ],
)
def test_wrap_openai_copies_gateway_metadata(gateway_header, expected) -> None:
    client = _openai_client(gateway_header)
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    assert runs[0].metadata.get("ls_gateway_info") == expected


def test_wrap_openai_copies_whole_header() -> None:
    header = {
        **_GATEWAY_HEADER,
        "outcome": "blocked",
        "selected_model": "claude-haiku",
        "blocking_policies": [{"id": "p1", "name": "No PII", "policy_type": "guard"}],
    }
    client = _openai_client(json.dumps(header))
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    gateway_keys = {k: v for k, v in runs[0].metadata.items() if "gateway" in k}
    assert gateway_keys == {"ls_gateway_info": header}


async def test_wrap_async_openai_copies_gateway_metadata() -> None:
    client = _openai_client(json.dumps(_GATEWAY_HEADER), is_async=True)
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


def test_wrapping_twice_adds_one_hook() -> None:
    openai = pytest.importorskip("openai")
    from langsmith.wrappers import wrap_openai

    http_client = httpx.Client(transport=httpx.MockTransport(_handler(None)))
    client = openai.OpenAI(api_key="test", base_url=_GATEWAY_URL, http_client=http_client)

    wrap_openai(client)
    wrap_openai(client)

    assert len(http_client.event_hooks["response"]) == 1


def _anthropic_client(is_async=False, events=None):
    anthropic = pytest.importorskip("anthropic")
    from langsmith.wrappers import wrap_anthropic

    transport = httpx.MockTransport(_handler(json.dumps(_GATEWAY_HEADER), body=_ANTHROPIC_MESSAGE, events=events))
    if is_async:
        return wrap_anthropic(
            anthropic.AsyncAnthropic(
                api_key="test", base_url=_GATEWAY_URL, http_client=httpx.AsyncClient(transport=transport)
            )
        )
    return wrap_anthropic(
        anthropic.Anthropic(api_key="test", base_url=_GATEWAY_URL, http_client=httpx.Client(transport=transport))
    )


_ANTHROPIC_REQUEST = {
    "model": "claude-sonnet",
    "max_tokens": 10,
    "messages": [{"role": "user", "content": "hi"}],
}


def test_wrap_anthropic_copies_gateway_metadata() -> None:
    client = _anthropic_client()
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.messages.create(**_ANTHROPIC_REQUEST, langsmith_extra=extra)

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


async def test_wrap_async_anthropic_copies_gateway_metadata() -> None:
    client = _anthropic_client(is_async=True)
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        await client.messages.create(**_ANTHROPIC_REQUEST, langsmith_extra=extra)

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


def test_wrap_anthropic_stream_copies_gateway_metadata() -> None:
    # messages.stream() sends the request before its run starts, so the
    # metadata is read from the stream's response instead of the hook.
    client = _anthropic_client(events=_ANTHROPIC_STREAM_EVENTS)

    with tracing_context(enabled=True), trace("parent", client=MagicMock()) as parent:
        with client.messages.stream(**_ANTHROPIC_REQUEST) as stream:
            list(stream)

    assert "ls_gateway_info" not in parent.metadata
    assert parent.child_runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


async def test_wrap_async_anthropic_stream_copies_gateway_metadata() -> None:
    client = _anthropic_client(is_async=True, events=_ANTHROPIC_STREAM_EVENTS)

    with tracing_context(enabled=True), trace("parent", client=MagicMock()) as parent:
        async with client.messages.stream(**_ANTHROPIC_REQUEST) as stream:
            async for _ in stream:
                pass

    assert "ls_gateway_info" not in parent.metadata
    assert parent.child_runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


def _gemini_client(events=None):
    genai = pytest.importorskip("google.genai")
    from google.genai import types

    from langsmith.wrappers import wrap_gemini

    transport = httpx.MockTransport(_handler(json.dumps(_GATEWAY_HEADER), body=_GEMINI_RESPONSE, events=events))
    return wrap_gemini(
        genai.Client(
            api_key="test",
            http_options=types.HttpOptions(
                base_url=_GATEWAY_URL,
                httpx_client=httpx.Client(transport=transport),
                httpx_async_client=httpx.AsyncClient(transport=transport),
            ),
        )
    )


_GEMINI_STREAM_EVENTS = [_GEMINI_RESPONSE]


def test_wrap_gemini_copies_gateway_metadata() -> None:
    client = _gemini_client()
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.models.generate_content(model="gemini-2.5-flash", contents="hi", langsmith_extra=extra)

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


async def test_wrap_async_gemini_copies_gateway_metadata() -> None:
    client = _gemini_client()
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        await client.aio.models.generate_content(model="gemini-2.5-flash", contents="hi", langsmith_extra=extra)

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


def test_wrap_gemini_stream_copies_gateway_metadata() -> None:
    client = _gemini_client(events=_GEMINI_STREAM_EVENTS)
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        list(client.models.generate_content_stream(model="gemini-2.5-flash", contents="hi", langsmith_extra=extra))

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO


async def test_wrap_async_gemini_stream_copies_gateway_metadata() -> None:
    client = _gemini_client(events=_GEMINI_STREAM_EVENTS)
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        stream = await client.aio.models.generate_content_stream(
            model="gemini-2.5-flash", contents="hi", langsmith_extra=extra
        )
        async for _ in stream:
            pass

    assert runs[0].metadata["ls_gateway_info"] == _EXPECTED_INFO
