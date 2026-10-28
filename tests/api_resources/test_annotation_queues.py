# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    AnnotationQueueSchema,
    AnnotationQueueSizeSchema,
    AnnotationQueueRetrieveResponse,
    RunSchemaWithAnnotationQueueInfo,
    AnnotationQueueRetrieveQueuesResponse,
    AnnotationQueueRetrieveAnnotationQueuesResponse,
)
from langsmith._utils import parse_datetime
from langsmith.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotationQueues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enable_reservations=True,
            metadata={"foo": "bar"},
            name="name",
            num_reviewers_per_item=0,
            reservation_minutes=0,
            reviewer_access_mode="any",
            rubric_instructions="rubric_instructions",
            rubric_items=[
                {
                    "feedback_key": "feedback_key",
                    "description": "description",
                    "feedback_config": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "feedback_config": {
                            "type": "continuous",
                            "allows_multiple_categories": True,
                            "categories": [
                                {
                                    "value": 0,
                                    "label": "x",
                                }
                            ],
                            "max": 0,
                            "min": 0,
                        },
                        "feedback_key": "feedback_key",
                        "modified_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "tenant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_deleted": True,
                        "is_enforced": True,
                        "is_first": True,
                        "is_lower_score_better": True,
                    },
                    "feedback_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_assertion": True,
                    "is_required": True,
                    "regex_validator": "string",
                    "required_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                    "score_descriptions": {"foo": "string"},
                    "value_descriptions": {"foo": "string"},
                    "visible_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                }
            ],
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.with_raw_response.update(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_annotation_queues(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.annotation_queues(
            name="name",
        )
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_annotation_queues_with_all_params(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.annotation_queues(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            default_dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enable_reservations=True,
            metadata={"foo": "bar"},
            num_reviewers_per_item=0,
            reservation_minutes=0,
            reviewer_access_mode="reviewer_access_mode",
            rubric_instructions="rubric_instructions",
            rubric_items=[
                {
                    "feedback_key": "feedback_key",
                    "description": "description",
                    "feedback_config": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "feedback_config": {
                            "type": "continuous",
                            "allows_multiple_categories": True,
                            "categories": [
                                {
                                    "value": 0,
                                    "label": "x",
                                }
                            ],
                            "max": 0,
                            "min": 0,
                        },
                        "feedback_key": "feedback_key",
                        "modified_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "tenant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_deleted": True,
                        "is_enforced": True,
                        "is_first": True,
                        "is_lower_score_better": True,
                    },
                    "feedback_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_assertion": True,
                    "is_required": True,
                    "regex_validator": "string",
                    "required_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                    "score_descriptions": {"foo": "string"},
                    "value_descriptions": {"foo": "string"},
                    "visible_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                }
            ],
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_annotation_queues(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.annotation_queues(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_annotation_queues(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.annotation_queues(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_run_status(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_run_status_with_all_params(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                override_added_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="status",
            )

        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_run_status(self, client: Langsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = client.annotation_queues.with_raw_response.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_run_status(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with client.annotation_queues.with_streaming_response.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = response.parse()
                assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_run_status(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(
                ValueError, match=r"Expected a non-empty value for `annotation_queue_run_id` but received ''"
            ):
                client.annotation_queues.with_raw_response.create_run_status(
                    annotation_queue_run_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_annotator_detail=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_export(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.with_raw_response.export(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_populate(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_populate_with_all_params(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            extend_trace_retention=True,
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_populate(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_populate(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_annotation_queues(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.retrieve_annotation_queues()
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_annotation_queues_with_all_params(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.retrieve_annotation_queues(
            assigned_to_me=True,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            queue_type="single",
            sort_by="sort_by",
            sort_by_desc=True,
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_annotation_queues(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.retrieve_annotation_queues()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_annotation_queues(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.retrieve_annotation_queues() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(
                SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
                annotation_queue,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_queues(self, client: Langsmith) -> None:
        annotation_queue = client.annotation_queues.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_queues(self, client: Langsmith) -> None:

        response = client.annotation_queues.with_raw_response.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_queues(self, client: Langsmith) -> None:
        with client.annotation_queues.with_streaming_response.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = response.parse()
            assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_queues(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.annotation_queues.with_raw_response.retrieve_queues(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run_with_all_params(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                include_extra=True,
            )

        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run(self, client: Langsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = client.annotation_queues.with_raw_response.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with client.annotation_queues.with_streaming_response.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = response.parse()
                assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_run(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                client.annotation_queues.with_raw_response.retrieve_run(
                    index=0,
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_size_with_all_params(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                status="needs_my_review",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_size(self, client: Langsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = client.annotation_queues.with_raw_response.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with client.annotation_queues.with_streaming_response.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                client.annotation_queues.with_raw_response.retrieve_size(
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_total_archived(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_total_archived_with_all_params(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_total_archived(self, client: Langsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = client.annotation_queues.with_raw_response.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_total_archived(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with client.annotation_queues.with_streaming_response.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_total_archived(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                client.annotation_queues.with_raw_response.retrieve_total_archived(
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_total_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = client.annotation_queues.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_total_size(self, client: Langsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = client.annotation_queues.with_raw_response.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_total_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with client.annotation_queues.with_streaming_response.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_total_size(self, client: Langsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                client.annotation_queues.with_raw_response.retrieve_total_size(
                    "",
                )


class TestAsyncAnnotationQueues:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(AnnotationQueueRetrieveResponse, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enable_reservations=True,
            metadata={"foo": "bar"},
            name="name",
            num_reviewers_per_item=0,
            reservation_minutes=0,
            reviewer_access_mode="any",
            rubric_instructions="rubric_instructions",
            rubric_items=[
                {
                    "feedback_key": "feedback_key",
                    "description": "description",
                    "feedback_config": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "feedback_config": {
                            "type": "continuous",
                            "allows_multiple_categories": True,
                            "categories": [
                                {
                                    "value": 0,
                                    "label": "x",
                                }
                            ],
                            "max": 0,
                            "min": 0,
                        },
                        "feedback_key": "feedback_key",
                        "modified_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "tenant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_deleted": True,
                        "is_enforced": True,
                        "is_first": True,
                        "is_lower_score_better": True,
                    },
                    "feedback_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_assertion": True,
                    "is_required": True,
                    "regex_validator": "string",
                    "required_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                    "score_descriptions": {"foo": "string"},
                    "value_descriptions": {"foo": "string"},
                    "visible_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                }
            ],
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.update(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.with_raw_response.update(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_annotation_queues(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.annotation_queues(
            name="name",
        )
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_annotation_queues_with_all_params(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.annotation_queues(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            default_dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            enable_reservations=True,
            metadata={"foo": "bar"},
            num_reviewers_per_item=0,
            reservation_minutes=0,
            reviewer_access_mode="reviewer_access_mode",
            rubric_instructions="rubric_instructions",
            rubric_items=[
                {
                    "feedback_key": "feedback_key",
                    "description": "description",
                    "feedback_config": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "feedback_config": {
                            "type": "continuous",
                            "allows_multiple_categories": True,
                            "categories": [
                                {
                                    "value": 0,
                                    "label": "x",
                                }
                            ],
                            "max": 0,
                            "min": 0,
                        },
                        "feedback_key": "feedback_key",
                        "modified_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "tenant_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "is_deleted": True,
                        "is_enforced": True,
                        "is_first": True,
                        "is_lower_score_better": True,
                    },
                    "feedback_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "is_assertion": True,
                    "is_required": True,
                    "regex_validator": "string",
                    "required_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                    "score_descriptions": {"foo": "string"},
                    "value_descriptions": {"foo": "string"},
                    "visible_if": {
                        "join": "all",
                        "rules": [
                            {
                                "key": "key",
                                "op": "is",
                                "values": [0],
                            }
                        ],
                    },
                }
            ],
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_annotation_queues(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.annotation_queues(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_annotation_queues(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.annotation_queues(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(AnnotationQueueSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_run_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_run_status_with_all_params(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                override_added_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                status="status",
            )

        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_run_status(self, async_client: AsyncLangsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = await async_client.annotation_queues.with_raw_response.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_run_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.annotation_queues.with_streaming_response.create_run_status(
                annotation_queue_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = await response.parse()
                assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_run_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(
                ValueError, match=r"Expected a non-empty value for `annotation_queue_run_id` but received ''"
            ):
                await async_client.annotation_queues.with_raw_response.create_run_status(
                    annotation_queue_run_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_annotator_detail=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.export(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.with_raw_response.export(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_populate(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_populate_with_all_params(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            extend_trace_retention=True,
        )
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_populate(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(object, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_populate(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.populate(
            queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(object, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_annotation_queues(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.retrieve_annotation_queues()
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_annotation_queues_with_all_params(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.retrieve_annotation_queues(
            assigned_to_me=True,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            queue_type="single",
            sort_by="sort_by",
            sort_by_desc=True,
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_annotation_queues(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.retrieve_annotation_queues()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
            annotation_queue,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_annotation_queues(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.retrieve_annotation_queues() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(
                AsyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse],
                annotation_queue,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_queues(self, async_client: AsyncLangsmith) -> None:
        annotation_queue = await async_client.annotation_queues.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_queues(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.with_raw_response.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_queues(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.with_streaming_response.retrieve_queues(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_queue = await response.parse()
            assert_matches_type(AnnotationQueueRetrieveQueuesResponse, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_queues(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.annotation_queues.with_raw_response.retrieve_queues(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run_with_all_params(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                include_extra=True,
            )

        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run(self, async_client: AsyncLangsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = await async_client.annotation_queues.with_raw_response.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.annotation_queues.with_streaming_response.retrieve_run(
                index=0,
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = await response.parse()
                assert_matches_type(RunSchemaWithAnnotationQueueInfo, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_run(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                await async_client.annotation_queues.with_raw_response.retrieve_run(
                    index=0,
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_size_with_all_params(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                status="needs_my_review",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_size(self, async_client: AsyncLangsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = await async_client.annotation_queues.with_raw_response.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.annotation_queues.with_streaming_response.retrieve_size(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = await response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                await async_client.annotation_queues.with_raw_response.retrieve_size(
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_total_archived(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_total_archived_with_all_params(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_total_archived(self, async_client: AsyncLangsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = await async_client.annotation_queues.with_raw_response.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_total_archived(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.annotation_queues.with_streaming_response.retrieve_total_archived(
                queue_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = await response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_total_archived(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                await async_client.annotation_queues.with_raw_response.retrieve_total_archived(
                    queue_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_total_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            annotation_queue = await async_client.annotation_queues.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_total_size(self, async_client: AsyncLangsmith) -> None:

        with pytest.warns(DeprecationWarning):
            response = await async_client.annotation_queues.with_raw_response.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_queue = await response.parse()
        assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_total_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.annotation_queues.with_streaming_response.retrieve_total_size(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                annotation_queue = await response.parse()
                assert_matches_type(AnnotationQueueSizeSchema, annotation_queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_total_size(self, async_client: AsyncLangsmith) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
                await async_client.annotation_queues.with_raw_response.retrieve_total_size(
                    "",
                )
