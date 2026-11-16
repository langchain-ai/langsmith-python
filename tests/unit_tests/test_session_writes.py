import json
from datetime import datetime, timezone

import pytest

from langsmith import AsyncLangsmith, Langsmith
from langsmith._httpx import httpx
from langsmith.types import Session, TracerSession


@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("operation", ["create", "update", "create_v2", "update_v2"])
@pytest.mark.parametrize("include_stats", [False, True])
@pytest.mark.parametrize("tier", ["longlived", "shortlived"])
async def test_session_write_contract(async_client: bool, operation: str, include_stats: bool, tier: str) -> None:
    is_create = operation in {"create", "create_v2"}
    is_v2 = operation.endswith("_v2")
    trace_tier = {"longlived": "LONG_LIVED", "shortlived": "SHORT_LIVED"}[tier] if is_v2 else tier
    resource = {
        "id": "019a0000-0000-7000-8000-000000000001",
        "tenant_id": "019a0000-0000-7000-8000-000000000002",
        "name": "test-project",
        "start_time": "2026-10-26T00:00:00Z",
        "last_run_start_time": "2026-10-26T00:00:00Z",
        "run_count": 3 if include_stats else None,
        "total_cost": 0.12 if include_stats else None,
        "trace_tier": trace_tier,
    }

    if is_v2:
        resource["type"] = "PROJECT"
    create_kwargs = {"type": "PROJECT"} if is_v2 and is_create else {}

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.method == ("POST" if is_create else "PATCH")
        expected_path = "/api/v2/sessions" if is_v2 else "/api/v1/sessions"
        if is_create:
            assert request.url.params["upsert"] == "true"
        else:
            expected_path += "/" + resource["id"]
        assert request.url.path == expected_path
        assert json.loads(request.content) == {"name": "test-project", "trace_tier": trace_tier, **create_kwargs}
        return httpx.Response(200, json=resource)

    transport = httpx.MockTransport(handle)
    if async_client:
        async with AsyncLangsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=transport),
        ) as async_api:
            write_session = getattr(async_api.sessions, operation)
            for _ in range(2 if is_v2 else 1):
                if is_create:
                    result = await write_session(
                        name="test-project", upsert=True, trace_tier=trace_tier, **create_kwargs
                    )
                else:
                    result = await write_session(resource["id"], name="test-project", trace_tier=trace_tier)
                trace_tier = result.trace_tier
    else:
        with Langsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.Client(transport=transport),
        ) as api:
            write_session = getattr(api.sessions, operation)
            for _ in range(2 if is_v2 else 1):
                if is_create:
                    result = write_session(name="test-project", upsert=True, trace_tier=trace_tier, **create_kwargs)
                else:
                    result = write_session(resource["id"], name="test-project", trace_tier=trace_tier)
                trace_tier = result.trace_tier

    assert result.id == resource["id"]
    assert isinstance(result, Session if is_v2 else TracerSession)
    assert result.start_time == datetime(2026, 10, 26, tzinfo=timezone.utc)
    assert result.last_run_start_time == datetime(2026, 10, 26, tzinfo=timezone.utc)
    assert result.run_count == resource["run_count"]
    assert result.total_cost == resource["total_cost"]
    assert result.trace_tier == resource["trace_tier"]


@pytest.mark.parametrize("session_type", ["PROJECT", "AGENT", "EXPERIMENT"])
def test_create_v2_explicit_type(session_type: str) -> None:
    body = {"type": session_type, "name": "typed-session"}
    if session_type == "EXPERIMENT":
        body["reference_dataset_id"] = "019a0000-0000-7000-8000-000000000003"

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v2/sessions"
        assert json.loads(request.content) == body
        return httpx.Response(201, json={**body, "id": "019a0000-0000-7000-8000-000000000001"})

    with Langsmith(
        api_key="test", base_url="https://example.test", http_client=httpx.Client(transport=httpx.MockTransport(handle))
    ) as api:
        result = api.sessions.create_v2(**body)
    assert result.type == session_type
