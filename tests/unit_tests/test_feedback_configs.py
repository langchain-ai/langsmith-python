"""Unit tests for the feedback config client methods."""

import uuid
from unittest import mock

import pytest

from langsmith import AsyncClient, Client

_CONFIG = {"type": "continuous", "min": 0.0, "max": 1.0}


def _enforced_config_response():
    return {
        "feedback_key": "correctness",
        "feedback_config": _CONFIG,
        "tenant_id": str(uuid.uuid4()),
        "modified_at": "2026-10-19T00:00:00Z",
        "is_lower_score_better": False,
        "is_enforced": True,
    }


def test_create_feedback_config_sends_is_enforced() -> None:
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "request_with_retries") as request:
        request.return_value = mock.Mock(json=_enforced_config_response)
        config = client.create_feedback_config("correctness", feedback_config=_CONFIG, is_enforced=True)

    body = request.call_args.kwargs["json"]
    assert body["is_enforced"] is True
    # Omitted, so the key keeps its existing score direction.
    assert "is_lower_score_better" not in body
    assert config.is_enforced is True


@pytest.mark.asyncio
async def test_async_create_feedback_config_sends_is_enforced() -> None:
    client = AsyncClient(api_url="http://localhost:1984", api_key="123")
    with mock.patch.object(AsyncClient, "_arequest_with_retries", new_callable=mock.AsyncMock) as request:
        request.return_value = mock.Mock(json=_enforced_config_response)
        config = await client.create_feedback_config("correctness", feedback_config=_CONFIG, is_enforced=True)

    body = request.call_args.kwargs["json"]
    assert body["is_enforced"] is True
    # Omitted, so the key keeps its existing score direction.
    assert "is_lower_score_better" not in body
    assert config.is_enforced is True
