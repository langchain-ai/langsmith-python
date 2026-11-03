"""Exercise dashboard requests without a running API server."""

import json

import pytest

from langsmith import AsyncLangsmith, Langsmith
from langsmith._httpx import httpx
from langsmith.types.custom_charts_section import CustomChartsSection


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_session_dashboard(asynchronous):
    session_id = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
    payload = {"start_time": "2026-10-01T00:00:00Z", "omit_data": True}
    dashboard = {"id": session_id, "session_id": session_id, "title": "Project", "charts": [], "sub_sections": []}

    def handle(request):
        assert request.method == "POST"
        assert request.url.path == f"/api/v1/sessions/{session_id}/dashboard"
        assert json.loads(request.content) == payload
        return httpx.Response(200, json=dashboard)

    if asynchronous:
        async with AsyncLangsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
        ) as client:
            result = await client.sessions.dashboard(session_id, **payload)
    else:
        with Langsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.Client(transport=httpx.MockTransport(handle)),
        ) as client:
            result = client.sessions.dashboard(session_id, **payload)

    assert isinstance(result, CustomChartsSection)
    assert result.id == session_id
    assert result.session_id == session_id
    assert result.title == "Project"
    assert result.charts == []
    assert result.sub_sections == []
