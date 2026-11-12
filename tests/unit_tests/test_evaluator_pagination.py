"""Keep versioned rule listing compatible with the public evaluator API."""

import pytest

from langsmith import APIStatusError, AsyncLangsmith, Langsmith
from langsmith._httpx import httpx
from langsmith.types import EvaluatorListParams, EvaluatorListResponse
from langsmith.types.evaluator_list_response import EvaluatorListResponse as ModuleResponse
from langsmith.types.rule import Rule

IDS = [f"00000000-0000-4000-8000-00000000000{value}" for value in (1, 2, 3)]
TAGS = [f"00000000-0000-4000-8000-00000000000{value}" for value in (4, 5)]
PROJECT = "00000000-0000-4000-8000-000000000006"
CURSOR = "opaque+/=cursor"
FILTERS = {
    "id": IDS,
    "tag_value_id": TAGS,
    "project_id": PROJECT,
    "page_size": 2,
    "type": "PROJECT",
    "name_contains": "Test % _",
    "include_backfill_progress": True,
}


def _rule(index):
    return {
        "id": IDS[index],
        "tenant_id": "00000000-0000-4000-8000-000000000007",
        "project_id": PROJECT,
        "created_at": "2026-01-01T12:00:00Z",
        "updated_at": "2026-01-01T12:00:00Z",
        "display_name": "Synthetic rule",
        "evaluator_version": 1,
        "sampling_rate": 1,
        "add_to_dataset_prefer_correction": False,
        "extend_only": False,
        "include_extended_stats": False,
        "is_enabled": True,
        "is_managed_evaluator": False,
        "is_tracing_disabled": False,
        "transient": False,
        "use_corrections_dataset": False,
        "evaluator_type": "CODE",
        "code_evaluators": [
            {
                "code": "return 1",
                "require_attachments": False,
                "code_evaluator_input": "TRAJECTORY",
                "advanced_features_enabled": True,
            }
        ],
    }


def _options(http_client):
    return {
        "api_key": "test",
        "tenant_id": "test",
        "base_url": "https://rules.test.invalid",
        "max_retries": 0,
        "_strict_response_validation": True,
        "http_client": http_client,
    }


def _pages(scenario):
    requests = []

    def handle(request):
        requests.append(request)
        assert request.method == "GET"
        assert request.url.path == "/api/v2/runs/rules"
        assert len(requests) <= (1 if scenario == "empty" else 2)
        query = request.url.params
        assert query.get_list("id") == IDS
        assert query.get_list("tag_value_id") == TAGS
        assert query["project_id"] == PROJECT
        assert query["page_size"] == "2"
        assert query["type"] == "PROJECT"
        assert query["name_contains"] == FILTERS["name_contains"]
        assert query["include_backfill_progress"] == "true"
        assert query.get("cursor") == (None if len(requests) == 1 else CURSOR)
        if scenario == "empty":
            return httpx.Response(200, json={"items": [], "next_cursor": None})
        if len(requests) == 1:
            return httpx.Response(200, json={"items": [_rule(0), _rule(1)], "next_cursor": CURSOR})
        if scenario == "failure":
            return httpx.Response(503, json={"detail": "Please retry later"})
        return httpx.Response(200, json={"items": [_rule(2)], "next_cursor": None})

    return requests, handle


def _assert_items(items, requests, scenario):
    expected = [] if scenario == "empty" else IDS[:2] if scenario == "failure" else IDS
    assert [item.id for item in items] == expected
    assert len(requests) == (1 if scenario == "empty" else 2)
    for item in items:
        assert isinstance(item, Rule)
        assert item.project_id == PROJECT
        assert item.evaluator_type == "CODE"
        assert item.code_evaluators is not None
        assert item.code_evaluators[0].code_evaluator_input == "TRAJECTORY"
        assert item.code_evaluators[0].advanced_features_enabled is True
    assert "cursor" not in FILTERS


@pytest.mark.parametrize("scenario", ["pages", "empty", "failure"])
def test_list_v2_pagination(scenario):
    requests, handle = _pages(scenario)
    items = []
    with Langsmith(**_options(httpx.Client(transport=httpx.MockTransport(handle)))) as client:
        try:
            items.extend(client.evaluators.list_v2(**FILTERS))
        except APIStatusError as error:
            assert scenario == "failure" and error.status_code == 503
        else:
            assert scenario != "failure"
    _assert_items(items, requests, scenario)


@pytest.mark.asyncio
@pytest.mark.parametrize("scenario", ["pages", "empty", "failure"])
async def test_async_list_v2_pagination(scenario):
    requests, handle = _pages(scenario)
    items = []
    async with AsyncLangsmith(**_options(httpx.AsyncClient(transport=httpx.MockTransport(handle)))) as client:
        try:
            async for item in client.evaluators.list_v2(**FILTERS):
                items.append(item)
        except APIStatusError as error:
            assert scenario == "failure" and error.status_code == 503
        else:
            assert scenario != "failure"
    _assert_items(items, requests, scenario)


def _legacy_response(request):
    assert request.method == "GET"
    assert request.url.path == "/api/v1/runs/rules"
    assert request.url.params["session_id"] == PROJECT
    assert request.url.params.get_list("id") == IDS
    item = _rule(0)
    item.pop("project_id")
    item.update({"session_id": PROJECT, "webhooks": None})
    # V1 returns enum values in snake_case.
    item["code_evaluators"][0]["code_evaluator_input"] = "trajectory"
    item["evaluator_type"] = "code"
    return httpx.Response(200, json=[item])


def test_v1_list_preserves_public_types_and_route():
    assert EvaluatorListResponse is ModuleResponse
    params: EvaluatorListParams = {"session_id": PROJECT, "id": IDS}
    with Langsmith(**_options(httpx.Client(transport=httpx.MockTransport(_legacy_response)))) as client:
        with pytest.warns(DeprecationWarning):
            response: EvaluatorListResponse = client.evaluators.list(**params)
    assert isinstance(response, list)
    assert response[0].session_id == PROJECT


@pytest.mark.asyncio
async def test_async_v1_list_preserves_public_types_and_route():
    params: EvaluatorListParams = {"session_id": PROJECT, "id": IDS}
    async with AsyncLangsmith(**_options(httpx.AsyncClient(transport=httpx.MockTransport(_legacy_response)))) as client:
        with pytest.warns(DeprecationWarning):
            response: EvaluatorListResponse = await client.evaluators.list(**params)
    assert isinstance(response, list)
    assert response[0].session_id == PROJECT
