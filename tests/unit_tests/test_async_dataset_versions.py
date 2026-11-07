"""Test async dataset version retrieval and pagination."""

from collections.abc import AsyncIterator
from datetime import datetime, timedelta, timezone
from uuid import UUID

import httpx
import pytest

from langsmith import AsyncClient
from langsmith import schemas as ls_schemas
from langsmith import utils as ls_utils

API_URL = "http://localhost:1984/api/v1"
DATASET_ID = UUID("c58674b8-f584-4694-a397-392bf3b14d48")
VERSIONS_URL = f"{API_URL}/datasets/{DATASET_ID}/versions"
VERSION_URL = f"{API_URL}/datasets/{DATASET_ID}/version"
VERSION = {"as_of": "2026-01-02T03:04:05+00:00", "tags": ["prod", "latest"]}


@pytest.fixture
async def version_client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
        api_url=API_URL,
        api_key="test-api-key",
        disable_prompt_cache=True,
        retry_config={"max_retries": 1},
    ) as client:
        yield client


async def _get_versions(client, operation, **kwargs):
    if operation == "list":
        return [version async for version in client.list_dataset_versions(**kwargs)]
    return await client.read_dataset_version(tag="latest", **kwargs)


@pytest.mark.parametrize("operation", ["list", "read"])
@pytest.mark.parametrize("selector", ["uuid", "string", "name", "both"])
async def test_dataset_versions_resolve_dataset(version_client, respx_mock, operation, selector):
    kwargs = {}
    if selector == "uuid":
        kwargs["dataset_id"] = DATASET_ID
    elif selector in ("string", "both"):
        kwargs["dataset_id"] = DATASET_ID.hex.upper()
    if selector in ("name", "both"):
        kwargs["dataset_name"] = "dataset name"
    if selector == "name":
        respx_mock.get(f"{API_URL}/datasets", params={"name": "dataset name"}).respond(
            200,
            json=[{"id": str(DATASET_ID), "name": "dataset name", "created_at": "2026-01-01T00:00:00Z"}],
        )
    route = respx_mock.get(VERSIONS_URL if operation == "list" else VERSION_URL).respond(
        200, json=[VERSION] if operation == "list" else VERSION
    )

    result = await _get_versions(version_client, operation, **kwargs)

    expected = ls_schemas.DatasetVersion(**VERSION)
    assert result == ([expected] if operation == "list" else expected)
    assert route.call_count == 1
    # An explicit ID takes precedence over a name, avoiding a lookup.
    assert respx_mock.calls.call_count == (2 if selector == "name" else 1)
    assert dict(route.calls.last.request.url.params) == (
        {"limit": "100", "offset": "0"} if operation == "list" else {"tag": "latest"}
    )


@pytest.mark.parametrize(
    ("limit", "total", "expected_count", "expected_offsets"),
    [
        (None, 0, 0, [0]),
        (None, 203, 203, [0, 100, 200]),
        (None, 100, 100, [0, 100]),
        (1, 203, 1, [0]),
        (2, 203, 2, [0]),
        (100, 203, 100, [0]),
        (101, 203, 101, [0, 100]),
        (150, 203, 150, [0, 100]),
        (250, 203, 203, [0, 100, 200]),
    ],
)
async def test_list_dataset_versions_pagination(
    version_client, respx_mock, limit, total, expected_count, expected_offsets
):
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    versions = [{"as_of": (start + timedelta(seconds=i)).isoformat()} for i in range(total)]
    page_size = min(limit, 100) if limit is not None else 100

    def respond(request):
        params = request.url.params
        assert params["search"] == "release v1"
        assert int(params["limit"]) == page_size
        offset = int(params["offset"])
        return httpx.Response(200, json=versions[offset : offset + page_size])

    route = respx_mock.get(VERSIONS_URL).mock(side_effect=respond)

    result = [
        version
        async for version in version_client.list_dataset_versions(
            dataset_id=DATASET_ID, search="release v1", limit=limit
        )
    ]

    assert result == [ls_schemas.DatasetVersion(**version) for version in versions[:expected_count]]
    assert [int(call.request.url.params["offset"]) for call in route.calls] == expected_offsets


async def test_list_dataset_versions_stops_at_limit_with_oversized_page(version_client, respx_mock):
    route = respx_mock.get(VERSIONS_URL).respond(200, json=[VERSION] * 3)

    result = [version async for version in version_client.list_dataset_versions(dataset_id=DATASET_ID, limit=2)]

    assert len(result) == 2
    assert route.call_count == 1


@pytest.mark.parametrize("limit", [0, -1])
async def test_list_dataset_versions_forwards_nonpositive_limit(version_client, respx_mock, limit):
    # Match the sync client: let the API handle the supplied page size.
    route = respx_mock.get(VERSIONS_URL).respond(200, json=[])

    assert [version async for version in version_client.list_dataset_versions(dataset_id=DATASET_ID, limit=limit)] == []
    assert route.calls.last.request.url.params["limit"] == str(limit)


async def test_list_dataset_versions_is_lazy(version_client, respx_mock):
    route = respx_mock.get(VERSIONS_URL).respond(200, json=[VERSION] * 100)
    versions = version_client.list_dataset_versions(dataset_id=DATASET_ID)

    assert not respx_mock.calls
    assert await anext(versions) == ls_schemas.DatasetVersion(**VERSION)
    await versions.aclose()

    assert route.call_count == 1


@pytest.mark.parametrize(
    ("selector", "expected_params"),
    [
        ({"tag": "release / v1"}, {"tag": "release / v1"}),
        ({"as_of": datetime(2026, 1, 2, 3, 4, 5)}, {"as_of": "2026-01-02 03:04:05"}),
        (
            {"as_of": datetime(2026, 1, 2, 3, 4, 5, 123456, tzinfo=timezone(timedelta(hours=5, minutes=30)))},
            {"as_of": "2026-01-02 03:04:05.123456+05:30"},
        ),
    ],
)
async def test_read_dataset_version_selector(version_client, respx_mock, selector, expected_params):
    route = respx_mock.get(VERSION_URL).respond(200, json=VERSION)

    result = await version_client.read_dataset_version(dataset_id=DATASET_ID, **selector)

    assert result == ls_schemas.DatasetVersion(**VERSION)
    assert dict(route.calls.last.request.url.params) == expected_params


@pytest.mark.parametrize("selector", [{}, {"as_of": datetime(2026, 1, 1), "tag": "prod"}])
async def test_read_dataset_version_requires_one_selector(version_client, respx_mock, selector):
    with pytest.raises(ValueError, match="Exactly one of as_of and tag must be specified"):
        await version_client.read_dataset_version(dataset_id=DATASET_ID, **selector)

    assert not respx_mock.calls


@pytest.mark.parametrize("operation", ["list", "read"])
async def test_dataset_versions_require_dataset(version_client, respx_mock, operation):
    with pytest.raises(ValueError, match="Either dataset_name or dataset_id must be provided"):
        await _get_versions(version_client, operation)

    assert not respx_mock.calls


@pytest.mark.parametrize("operation", ["list", "read"])
@pytest.mark.parametrize("dataset_id", ["", "invalid-id"])
async def test_dataset_versions_validate_dataset_id(version_client, respx_mock, operation, dataset_id):
    with pytest.raises(ls_utils.LangSmithUserError, match="dataset_id must be a valid UUID"):
        await _get_versions(version_client, operation, dataset_id=dataset_id)

    assert not respx_mock.calls


@pytest.mark.parametrize("operation", ["list", "read"])
async def test_dataset_versions_unknown_dataset_name(version_client, respx_mock, operation):
    route = respx_mock.get(f"{API_URL}/datasets", params={"name": "missing"}).respond(200, json=[])

    with pytest.raises(ls_utils.LangSmithNotFoundError, match="Dataset missing not found"):
        await _get_versions(version_client, operation, dataset_name="missing")

    assert route.call_count == 1
    assert respx_mock.calls.call_count == 1


@pytest.mark.parametrize("operation", ["list", "read"])
@pytest.mark.parametrize(
    ("status", "error"),
    [(401, ls_utils.LangSmithAuthError), (404, ls_utils.LangSmithNotFoundError), (500, ls_utils.LangSmithAPIError)],
)
async def test_dataset_versions_api_errors(version_client, respx_mock, operation, status, error):
    route = respx_mock.get(VERSIONS_URL if operation == "list" else VERSION_URL).respond(
        status, json={"detail": "request failed"}
    )

    with pytest.raises(error):
        await _get_versions(version_client, operation, dataset_id=DATASET_ID)

    assert route.call_count == 1
