"""Test the async dataset split API against the synchronous client's contract."""

import json
from collections.abc import AsyncIterator
from datetime import datetime, timezone
from uuid import UUID, uuid4

import pytest
import respx

from langsmith import AsyncClient
from langsmith import utils as ls_utils

API_URL = "http://localhost:1984/api/v1"
DATASET_ID = UUID("c58674b8-f584-4694-a397-392bf3b14d48")
SPLITS_URL = f"{API_URL}/datasets/{DATASET_ID}/splits"


@pytest.fixture
async def split_client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
        api_url=API_URL,
        api_key="test-api-key",
        disable_prompt_cache=True,
        retry_config={"max_retries": 1},
    ) as client:
        yield client


@pytest.mark.parametrize(
    ("as_of", "expected_params"),
    [
        (None, {}),
        ("release-v1", {"as_of": "release-v1"}),
        (datetime(2026, 1, 2, 3, 4, 5), {"as_of": "2026-01-02T03:04:05"}),
        (datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc), {"as_of": "2026-01-02T03:04:05+00:00"}),
    ],
)
async def test_list_dataset_splits_version(split_client, respx_mock, as_of, expected_params):
    route = respx_mock.get(SPLITS_URL).respond(200, json=["train", "test"])

    assert await split_client.list_dataset_splits(dataset_id=DATASET_ID, as_of=as_of) == ["train", "test"]
    assert dict(route.calls.last.request.url.params) == expected_params
    assert route.call_count == 1


async def test_list_dataset_splits_empty(split_client, respx_mock):
    respx_mock.get(SPLITS_URL).respond(200, json=[])

    assert await split_client.list_dataset_splits(dataset_id=DATASET_ID) == []


@pytest.mark.parametrize("remove", [None, False, True])
@pytest.mark.parametrize("empty", [False, True])
async def test_update_dataset_splits_payload(split_client, respx_mock, remove, empty):
    example_ids = [] if empty else [uuid4(), uuid4().hex.upper()]
    # An empty response is valid: updates must not attempt to decode JSON.
    route = respx_mock.put(SPLITS_URL).respond(204)
    kwargs = {} if remove is None else {"remove": remove}

    result = await split_client.update_dataset_splits(
        dataset_id=DATASET_ID, split_name="test", example_ids=example_ids, **kwargs
    )

    assert result is None
    assert route.call_count == 1
    assert json.loads(route.calls.last.request.content) == {
        "split_name": "test",
        "examples": [str(UUID(str(example_id))) for example_id in example_ids],
        "remove": False if remove is None else remove,
    }


@pytest.mark.parametrize("operation", ["list_dataset_splits", "update_dataset_splits"])
@pytest.mark.parametrize("selector", ["id", "name", "both"])
async def test_dataset_splits_resolve_dataset(split_client, respx_mock, operation, selector):
    kwargs = {}
    if selector in ("id", "both"):
        kwargs["dataset_id"] = DATASET_ID.hex.upper()
    if selector in ("name", "both"):
        kwargs["dataset_name"] = "dataset name"
    if selector == "name":
        respx_mock.get(f"{API_URL}/datasets", params={"name": "dataset name"}).respond(
            200,
            json=[{"id": str(DATASET_ID), "name": "dataset name", "created_at": "2026-01-01T00:00:00Z"}],
        )
    if operation == "update_dataset_splits":
        kwargs.update(split_name="train", example_ids=[])
        respx_mock.put(SPLITS_URL).respond(204)
    else:
        respx_mock.get(SPLITS_URL).respond(200, json=["train"])

    await getattr(split_client, operation)(**kwargs)

    # An explicit ID takes precedence, so only the name-only case needs a lookup.
    assert respx_mock.calls.call_count == (2 if selector == "name" else 1)


@pytest.mark.parametrize("operation", ["list_dataset_splits", "update_dataset_splits"])
async def test_dataset_splits_require_dataset(split_client, respx_mock, operation):
    kwargs = {"split_name": "test", "example_ids": []} if operation == "update_dataset_splits" else {}

    with pytest.raises(ValueError, match="Must provide dataset name or ID"):
        await getattr(split_client, operation)(**kwargs)

    assert not respx_mock.calls


@pytest.mark.parametrize("operation", ["list_dataset_splits", "update_dataset_splits"])
@pytest.mark.parametrize("dataset_id", ["", "invalid-id"])
async def test_dataset_splits_validate_dataset_id(split_client, respx_mock, operation, dataset_id):
    kwargs = {"split_name": "test", "example_ids": []} if operation == "update_dataset_splits" else {}

    with pytest.raises(ls_utils.LangSmithUserError, match="dataset_id must be a valid UUID"):
        await getattr(split_client, operation)(dataset_id=dataset_id, **kwargs)

    assert not respx_mock.calls


async def test_update_dataset_splits_validate_example_ids(split_client, respx_mock):
    with pytest.raises(ls_utils.LangSmithUserError, match=r"example_ids\[1\] must be a valid UUID"):
        await split_client.update_dataset_splits(
            dataset_id=DATASET_ID, split_name="test", example_ids=[uuid4(), "invalid-id"]
        )

    assert not respx_mock.calls


@pytest.mark.parametrize("operation", ["list_dataset_splits", "update_dataset_splits"])
async def test_dataset_splits_unknown_dataset_name(split_client, respx_mock, operation):
    route = respx_mock.get(f"{API_URL}/datasets", params={"name": "missing"}).respond(200, json=[])
    kwargs = {"split_name": "test", "example_ids": []} if operation == "update_dataset_splits" else {}

    with pytest.raises(ls_utils.LangSmithNotFoundError, match="Dataset missing not found"):
        await getattr(split_client, operation)(dataset_name="missing", **kwargs)

    assert route.call_count == 1
    assert respx_mock.calls.call_count == 1


@pytest.mark.parametrize("operation", ["list_dataset_splits", "update_dataset_splits"])
@pytest.mark.parametrize(
    ("status", "error"),
    [(401, ls_utils.LangSmithAuthError), (404, ls_utils.LangSmithNotFoundError), (500, ls_utils.LangSmithAPIError)],
)
async def test_dataset_splits_api_errors(split_client, respx_mock: respx.MockRouter, operation, status, error):
    method = "PUT" if operation == "update_dataset_splits" else "GET"
    route = respx_mock.request(method, SPLITS_URL).respond(status, json={"detail": "request failed"})
    kwargs = {"split_name": "test", "example_ids": []} if operation == "update_dataset_splits" else {}

    with pytest.raises(error):
        await getattr(split_client, operation)(dataset_id=DATASET_ID, **kwargs)

    assert route.call_count == 1
