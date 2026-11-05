"""Unit tests for the feedback config client methods."""

import json
import uuid
from typing import Any
from unittest import mock

import pytest

from langsmith import AsyncClient, Client
from langsmith.schemas import FeedbackConfig

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


_TAGS: FeedbackConfig = {
    "type": "categorical",
    "categories": [{"value": 0, "label": "billing"}, {"value": 1, "label": "shipping"}],
    "allows_multiple_categories": True,
}


def _config_response(config_id: uuid.UUID) -> dict[str, Any]:
    return {
        "id": str(config_id),
        "feedback_key": "topics",
        "feedback_config": _TAGS,
        "tenant_id": str(uuid.uuid4()),
        "modified_at": "2026-11-04T00:00:00Z",
        "is_lower_score_better": False,
        "is_enforced": False,
        "is_first": False,
        "is_deleted": False,
    }


def _queue_response(queue_id: uuid.UUID, config_id: uuid.UUID) -> dict[str, Any]:
    return {
        "id": str(queue_id),
        "name": "source",
        "tenant_id": str(uuid.uuid4()),
        "created_at": "2026-11-04T00:00:00Z",
        "updated_at": "2026-11-04T00:00:00Z",
        "rubric_instructions": None,
        "rubric_items": [
            {
                "feedback_key": "resolved",
                "description": None,
                "value_descriptions": None,
                "score_descriptions": None,
                "is_required": True,
                "required_if": None,
                "visible_if": None,
                "is_assertion": None,
                "regex_validator": None,
                "feedback_config_id": None,
                "feedback_config": None,
            },
            {
                "feedback_key": "topics",
                "description": "Pick every topic that applies.",
                "value_descriptions": None,
                "score_descriptions": None,
                "is_required": False,
                "required_if": {
                    "join": "all",
                    "rules": [{"key": "resolved", "op": "is", "values": [0]}],
                },
                "visible_if": None,
                "is_assertion": None,
                "regex_validator": None,
                "feedback_config_id": str(config_id),
                "feedback_config": _config_response(config_id),
            },
        ],
    }


def test_feedback_config_reads_back_multi_select_and_id() -> None:
    config_id = uuid.uuid4()
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "request_with_retries") as request:
        request.return_value = mock.Mock(json=lambda: _config_response(config_id))
        config = client.create_feedback_config("topics", feedback_config=_TAGS)

    assert request.call_args.kwargs["json"]["feedback_config"]["allows_multiple_categories"] is True
    assert config.id == config_id
    assert config.feedback_config["allows_multiple_categories"] is True


def test_update_feedback_config_targets_config_id() -> None:
    config_id = uuid.uuid4()
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "request_with_retries") as request:
        request.return_value = mock.Mock(json=lambda: _config_response(config_id))
        client.update_feedback_config("topics", feedback_config=_TAGS, config_id=config_id)
        update_body = request.call_args.kwargs["json"]
        client.add_feedback_categories("topics", [{"value": 2, "label": "returns"}], config_id=str(config_id))
        add_body = request.call_args.kwargs["json"]
        client.remove_feedback_categories("topics", [2])
        remove_body = request.call_args.kwargs["json"]

    assert update_body == {"feedback_key": "topics", "id": str(config_id), "feedback_config": _TAGS}
    assert add_body == {
        "feedback_key": "topics",
        "id": str(config_id),
        "add_categories": [{"value": 2, "label": "returns"}],
    }
    # Without config_id the server picks the key's config.
    assert remove_body == {"feedback_key": "topics", "remove_categories": [2]}


@pytest.mark.asyncio
async def test_async_category_helpers_target_config_id() -> None:
    config_id = uuid.uuid4()
    client = AsyncClient(api_url="http://localhost:1984", api_key="123")
    with mock.patch.object(AsyncClient, "_arequest_with_retries", new_callable=mock.AsyncMock) as request:
        request.return_value = mock.Mock(json=lambda: _config_response(config_id))
        await client.add_feedback_categories("topics", [{"value": 2, "label": "returns"}], config_id=config_id)
        add_body = request.call_args.kwargs["json"]
        await client.remove_feedback_categories("topics", [2], config_id=config_id)
        remove_body = request.call_args.kwargs["json"]

    assert add_body["id"] == str(config_id)
    assert add_body["add_categories"] == [{"value": 2, "label": "returns"}]
    assert remove_body == {"feedback_key": "topics", "id": str(config_id), "remove_categories": [2]}


def test_list_feedback_configs_include_all_configs() -> None:
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "_get_paginated_list", return_value=iter([])) as paginate:
        list(client.list_feedback_configs(feedback_key=["topics"], include_all_configs=True))

    params = paginate.call_args.kwargs["params"]
    assert params["include_all_configs"] is True
    assert params["key"] == ["topics"]


def test_delete_feedback_config_by_id() -> None:
    config_id = uuid.uuid4()
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "request_with_retries") as request:
        client.delete_feedback_config(config_id=config_id)

    assert request.call_args.kwargs["params"] == {"id": str(config_id)}
    with pytest.raises(ValueError):
        client.delete_feedback_config("topics", config_id=config_id)
    with pytest.raises(ValueError):
        client.delete_feedback_config()


def test_copy_rubric_keeps_feedback_config_ids() -> None:
    source_id, config_id = uuid.uuid4(), uuid.uuid4()
    client = Client(api_url="http://localhost:1984", api_key="123", session=mock.Mock())
    with mock.patch.object(Client, "request_with_retries") as request:
        request.return_value = mock.Mock(json=lambda: _queue_response(source_id, config_id))
        source = client.read_annotation_queue(source_id)
        assert source.rubric_items is not None
        client.create_annotation_queue(name="copy", rubric_items=source.rubric_items)
        create_body = json.loads(request.call_args.kwargs["data"])
        client.update_annotation_queue(uuid.uuid4(), rubric_items=source.rubric_items)
        update_body = json.loads(request.call_args.kwargs["data"])

    topics = source.rubric_items[1]
    assert topics["feedback_config_id"] == config_id
    assert topics["feedback_config"] is not None
    assert topics["feedback_config"].feedback_config["allows_multiple_categories"] is True
    assert topics["required_if"] == {"join": "all", "rules": [{"key": "resolved", "op": "is", "values": [0]}]}
    for body in (create_body, update_body):
        sent = body["rubric_items"][1]
        assert sent["feedback_config_id"] == str(config_id)
        assert sent["required_if"] == topics["required_if"]


@pytest.mark.asyncio
async def test_async_copy_rubric_keeps_feedback_config_ids() -> None:
    source_id, config_id = uuid.uuid4(), uuid.uuid4()
    client = AsyncClient(api_url="http://localhost:1984", api_key="123")
    with mock.patch.object(AsyncClient, "_arequest_with_retries", new_callable=mock.AsyncMock) as request:
        request.return_value = mock.Mock(json=lambda: _queue_response(source_id, config_id))
        source = await client.read_annotation_queue(source_id)
        assert source.rubric_items is not None
        await client.create_annotation_queue(name="copy", rubric_items=source.rubric_items)
        create_body = json.loads(request.call_args.kwargs["content"])

    assert request.call_args_list[0].args == ("GET", f"/annotation-queues/{source_id}")
    assert create_body["rubric_items"][1]["feedback_config_id"] == str(config_id)
