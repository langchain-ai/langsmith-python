"""Unit tests for copying LLM Gateway response metadata onto OpenAI runs."""

import json
from unittest.mock import MagicMock

import httpx
import pytest

openai = pytest.importorskip("openai")

from langsmith import run_trees  # noqa: E402
from langsmith.run_helpers import tracing_context  # noqa: E402
from langsmith.wrappers import wrap_openai  # noqa: E402

_GATEWAY_HEADER = {
    "request_id": "0199a1b2-0000-7000-8000-000000000001",
    "outcome": "success",
    "provider": "anthropic",
    "model": "claude-sonnet",
    "attempt_details": [{"candidate": 1, "status_code": 429}],
    "fallback_used": True,
    "source_api_type": "openai",
}
_COMPLETION = {
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


def _handler(gateway_header):
    def handle(request: httpx.Request) -> httpx.Response:
        headers = {}
        if gateway_header is not None:
            headers["x-langsmith-gateway-metadata"] = gateway_header
        return httpx.Response(200, json=_COMPLETION, headers=headers)

    return handle


def _capture_run():
    runs: list[run_trees.RunTree] = []
    extra = {"on_end": runs.append, "client": MagicMock()}
    return runs, extra


@pytest.mark.parametrize(
    "gateway_header, expected",
    [
        (
            json.dumps(_GATEWAY_HEADER),
            {k: v for k, v in _GATEWAY_HEADER.items() if k != "source_api_type"},
        ),
        (None, None),
        ("not-json", None),
    ],
)
def test_wrap_openai_copies_gateway_metadata(gateway_header, expected) -> None:
    client = wrap_openai(
        openai.OpenAI(
            api_key="test",
            http_client=httpx.Client(transport=httpx.MockTransport(_handler(gateway_header))),
        )
    )
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    assert runs[0].metadata.get("ls_gateway_info") == expected


def test_wrap_openai_adds_flat_filter_keys() -> None:
    header = {
        **_GATEWAY_HEADER,
        "outcome": "blocked",
        "selected_model": "claude-haiku",
        "attempts": 2,
        "blocking_policies": [
            {"id": "p1", "name": "No PII", "policy_type": "guard"},
            {"id": "p2", "name": "Budget", "policy_type": "spend_limit"},
        ],
    }
    client = wrap_openai(
        openai.OpenAI(
            api_key="test",
            http_client=httpx.Client(transport=httpx.MockTransport(_handler(json.dumps(header)))),
        )
    )
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    flat = {k: v for k, v in runs[0].metadata.items() if k.startswith("ls_gateway.")}
    assert flat == {
        "ls_gateway.request_id": header["request_id"],
        "ls_gateway.outcome": "blocked",
        "ls_gateway.provider": "anthropic",
        "ls_gateway.model": "claude-haiku",
        "ls_gateway.fallback_used": True,
        "ls_gateway.attempts": 2,
        "ls_gateway.blocking_policies": "No PII, Budget",
    }


async def test_wrap_async_openai_copies_gateway_metadata() -> None:
    client = wrap_openai(
        openai.AsyncOpenAI(
            api_key="test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(json.dumps(_GATEWAY_HEADER)))),
        )
    )
    runs, extra = _capture_run()

    with tracing_context(enabled=True):
        await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "hi"}],
            langsmith_extra=extra,
        )

    assert runs[0].metadata["ls_gateway_info"]["request_id"] == (_GATEWAY_HEADER["request_id"])


def test_wrapping_twice_adds_one_hook() -> None:
    http_client = httpx.Client(transport=httpx.MockTransport(_handler(None)))
    client = openai.OpenAI(api_key="test", http_client=http_client)

    wrap_openai(client)
    wrap_openai(client)

    assert len(http_client.event_hooks["response"]) == 1
