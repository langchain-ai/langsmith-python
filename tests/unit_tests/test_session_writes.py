import json
from datetime import datetime, timezone

import httpx
import pytest

from langsmith import AsyncLangsmith, Langsmith
from langsmith.types import TracerSession


@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("operation", ["create", "update"])
@pytest.mark.parametrize("include_stats", [False, True])
async def test_session_write_uses_v1(async_client: bool, operation: str, include_stats: bool) -> None:
    resource = {
        "id": "019a0000-0000-7000-8000-000000000001",
        "tenant_id": "019a0000-0000-7000-8000-000000000002",
        "name": "test-project",
        "start_time": "2026-10-26T00:00:00Z",
        "last_run_start_time": "2026-10-26T00:00:00Z",
        "run_count": 3 if include_stats else None,
        "total_cost": "0.12" if include_stats else None,
    }

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.method == ("POST" if operation == "create" else "PATCH")
        expected_path = "/api/v1/sessions"
        if operation == "create":
            assert request.url.params["upsert"] == "true"
        else:
            expected_path += "/" + resource["id"]
        assert request.url.path == expected_path
        assert json.loads(request.content) == {"name": "test-project"}
        return httpx.Response(200, json=resource)

    transport = httpx.MockTransport(handle)
    if async_client:
        async with AsyncLangsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=transport),
        ) as async_api:
            if operation == "create":
                result = await async_api.sessions.create(name="test-project", upsert=True)
            else:
                result = await async_api.sessions.update(resource["id"], name="test-project")
    else:
        with Langsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.Client(transport=transport),
        ) as api:
            if operation == "create":
                result = api.sessions.create(name="test-project", upsert=True)
            else:
                result = api.sessions.update(resource["id"], name="test-project")

    assert result.id == resource["id"]
    assert isinstance(result, TracerSession)
    assert result.start_time == datetime(2026, 10, 26, tzinfo=timezone.utc)
    assert result.last_run_start_time == datetime(2026, 10, 26, tzinfo=timezone.utc)
    assert result.run_count == resource["run_count"]
    assert result.total_cost == resource["total_cost"]
