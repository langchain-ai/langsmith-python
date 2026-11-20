# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith._utils import parse_datetime
from langsmith.pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from langsmith.types.annotation_queues import (
    ItemListResponse,
    ItemCreateResponse,
    ItemUpdateResponse,
    ItemSetFinalResponse,
    ItemDeleteAllResponse,
    ItemCreateStatusResponse,
    ItemRetrieveCountResponse,
    ItemRetrieveReviewsResponse,
    AnnotationQueueItemKeyReviews,
    ItemRetrievePlacementResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.create(
            queue_id="queue_id",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.create(
            queue_id="queue_id",
            extend_trace_retention=True,
            items=[
                {
                    "item_type": "RUN",
                    "project_id": "project_id",
                    "run_id": "run_id",
                    "session_id": "session_id",
                    "source_proposed_example_id": "source_proposed_example_id",
                    "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "thread_id": "thread_id",
                }
            ],
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.create(
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.create(
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.create(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.update(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.update(
            item_id="item_id",
            queue_id="queue_id",
            added_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_reviewed_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.update(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.update(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.update(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.update(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.list(
            queue_id="queue_id",
            status="needs_my_review",
        )
        assert_matches_type(SyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.list(
            queue_id="queue_id",
            status="needs_my_review",
            agreement="disagreed",
            cursor="cursor",
            direction="forward",
            has_unresolved_keys=True,
            item_type="RUN",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
        )
        assert_matches_type(SyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.list(
            queue_id="queue_id",
            status="needs_my_review",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.list(
            queue_id="queue_id",
            status="needs_my_review",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.list(
                queue_id="",
                status="needs_my_review",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clear_final(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clear_final(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clear_final(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clear_final(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.clear_final(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.clear_final(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.annotation_queues.items.with_raw_response.clear_final(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_status(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.create_status(
            queue_item_id="queue_item_id",
        )
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_status_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.create_status(
            queue_item_id="queue_item_id",
            override_added_at="override_added_at",
            status="viewed",
        )
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_status(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.create_status(
            queue_item_id="queue_item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_status(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.create_status(
            queue_item_id="queue_item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_status(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.create_status(
                queue_item_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.delete_all(
            queue_id="queue_id",
        )
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.delete_all(
            queue_id="queue_id",
            item_ids=["string"],
        )
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.delete_all(
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.delete_all(
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.delete_all(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_count(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.retrieve_count(
            queue_id="queue_id",
            status="status",
        )
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_count_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.retrieve_count(
            queue_id="queue_id",
            status="status",
            agreement="disagreed",
            end_time="end_time",
            has_unresolved_keys=True,
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time="start_time",
        )
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_count(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.retrieve_count(
            queue_id="queue_id",
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_count(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.retrieve_count(
            queue_id="queue_id",
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_count(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.retrieve_count(
                queue_id="",
                status="status",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_placement(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_placement(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_placement(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_placement(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.retrieve_placement(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.retrieve_placement(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_reviews(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_reviews(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_reviews(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_reviews(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.retrieve_reviews(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.retrieve_reviews(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_final(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_final_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
            score=0,
            value="value",
            values=["string"],
        )
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_final(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_final(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemSetFinalResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_final(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.set_final(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.set_final(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.annotation_queues.items.with_raw_response.set_final(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_review(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_review_with_all_params(self, client: Langsmith) -> None:
        item = client.annotation_queues.items.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
            score=0,
            value="value",
            values=["string"],
        )
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_review(self, client: Langsmith) -> None:

        response = client.annotation_queues.items.with_raw_response.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_review(self, client: Langsmith) -> None:
        with client.annotation_queues.items.with_streaming_response.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_review(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.annotation_queues.items.with_raw_response.set_review(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.annotation_queues.items.with_raw_response.set_review(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.annotation_queues.items.with_raw_response.set_review(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.create(
            queue_id="queue_id",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.create(
            queue_id="queue_id",
            extend_trace_retention=True,
            items=[
                {
                    "item_type": "RUN",
                    "project_id": "project_id",
                    "run_id": "run_id",
                    "session_id": "session_id",
                    "source_proposed_example_id": "source_proposed_example_id",
                    "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "thread_id": "thread_id",
                }
            ],
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.create(
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.create(
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.create(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.update(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.update(
            item_id="item_id",
            queue_id="queue_id",
            added_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_reviewed_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.update(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.update(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.update(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.update(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.list(
            queue_id="queue_id",
            status="needs_my_review",
        )
        assert_matches_type(AsyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.list(
            queue_id="queue_id",
            status="needs_my_review",
            agreement="disagreed",
            cursor="cursor",
            direction="forward",
            has_unresolved_keys=True,
            item_type="RUN",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
        )
        assert_matches_type(AsyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.list(
            queue_id="queue_id",
            status="needs_my_review",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.list(
            queue_id="queue_id",
            status="needs_my_review",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.list(
                queue_id="",
                status="needs_my_review",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clear_final(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clear_final(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clear_final(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.clear_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clear_final(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.clear_final(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.clear_final(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.clear_final(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_status(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.create_status(
            queue_item_id="queue_item_id",
        )
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_status_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.create_status(
            queue_item_id="queue_item_id",
            override_added_at="override_added_at",
            status="viewed",
        )
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_status(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.create_status(
            queue_item_id="queue_item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_status(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.create_status(
            queue_item_id="queue_item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateStatusResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.create_status(
                queue_item_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.delete_all(
            queue_id="queue_id",
        )
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.delete_all(
            queue_id="queue_id",
            item_ids=["string"],
        )
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.delete_all(
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.delete_all(
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemDeleteAllResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.delete_all(
                queue_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.retrieve_count(
            queue_id="queue_id",
            status="status",
        )
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_count_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.retrieve_count(
            queue_id="queue_id",
            status="status",
            agreement="disagreed",
            end_time="end_time",
            has_unresolved_keys=True,
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time="start_time",
        )
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_count(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.retrieve_count(
            queue_id="queue_id",
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.retrieve_count(
            queue_id="queue_id",
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemRetrieveCountResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.retrieve_count(
                queue_id="",
                status="status",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_placement(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_placement(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_placement(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.retrieve_placement(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemRetrievePlacementResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_placement(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.retrieve_placement(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.retrieve_placement(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_reviews(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        )
        assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_reviews(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_reviews(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.retrieve_reviews(
            item_id="item_id",
            queue_id="queue_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemRetrieveReviewsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_reviews(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.retrieve_reviews(
                item_id="item_id",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.retrieve_reviews(
                item_id="",
                queue_id="queue_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_final(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_final_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
            score=0,
            value="value",
            values=["string"],
        )
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_final(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemSetFinalResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_final(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.set_final(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemSetFinalResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_final(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_final(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_final(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_final(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_review(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_review_with_all_params(self, async_client: AsyncLangsmith) -> None:
        item = await async_client.annotation_queues.items.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
            score=0,
            value="value",
            values=["string"],
        )
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_review(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.annotation_queues.items.with_raw_response.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_review(self, async_client: AsyncLangsmith) -> None:
        async with async_client.annotation_queues.items.with_streaming_response.set_review(
            key="key",
            queue_id="queue_id",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AnnotationQueueItemKeyReviews, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_review(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_review(
                key="key",
                queue_id="",
                item_id="item_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_review(
                key="key",
                queue_id="queue_id",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.annotation_queues.items.with_raw_response.set_review(
                key="",
                queue_id="queue_id",
                item_id="item_id",
            )
