# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.annotation_queues import (
    item_list_params,
    item_create_params,
    item_update_params,
    item_set_final_params,
    item_delete_all_params,
    item_create_status_params,
    item_retrieve_count_params,
)
from ...types.annotation_queues.item_list_response import ItemListResponse
from ...types.annotation_queues.item_create_response import ItemCreateResponse
from ...types.annotation_queues.item_update_response import ItemUpdateResponse
from ...types.annotation_queues.item_set_final_response import ItemSetFinalResponse
from ...types.annotation_queues.item_delete_all_response import ItemDeleteAllResponse
from ...types.annotation_queues.item_create_status_response import ItemCreateStatusResponse
from ...types.annotation_queues.item_retrieve_count_response import ItemRetrieveCountResponse
from ...types.annotation_queues.item_retrieve_placement_response import ItemRetrievePlacementResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def create(
        self,
        queue_id: str,
        *,
        extend_trace_retention: bool | Omit = omit,
        items: Iterable[item_create_params.Item] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateResponse:
        """Add RUN or THREAD items to a single annotation queue.

        RUN items require run_id
        unless they are created from a suggested example. THREAD items require thread_id
        and project_id.

        Args:
          extend_trace_retention: Defaults to false. When true, upgrade the traces of added runs from base to
              extended retention. Thread items are not upgraded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._post(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items", queue_id=queue_id),
            body=maybe_transform({"items": items}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"extend_trace_retention": extend_trace_retention}, item_create_params.ItemCreateParams
                ),
            ),
            cast_to=ItemCreateResponse,
        )

    def update(
        self,
        item_id: str,
        *,
        queue_id: str,
        added_at: Union[str, datetime] | Omit = omit,
        last_reviewed_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUpdateResponse:
        """
        Partially update mutable timestamps (added_at, last_reviewed_time) for a RUN or
        THREAD annotation queue item. Omit a field, or pass JSON null, to leave it
        unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._patch(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}", queue_id=queue_id, item_id=item_id
            ),
            body=maybe_transform(
                {
                    "added_at": added_at,
                    "last_reviewed_time": last_reviewed_time,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemUpdateResponse,
        )

    def list(
        self,
        queue_id: str,
        *,
        status: Literal["needs_my_review", "needs_others_review", "archived"],
        agreement: Literal["disagreed"] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["forward", "backward"] | Omit = omit,
        has_unresolved_keys: bool | Omit = omit,
        item_type: Literal["RUN", "THREAD"] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[ItemListResponse]:
        """
        List RUN and THREAD items in a single annotation queue for one review status
        section, with opaque cursor pagination. Optional item_type=RUN|THREAD filters
        the page. Optional min_start_time/max_start_time bound the item's trace start
        time; items with no start time are excluded when either bound is set.
        direction=backward returns items before the supplied cursor. The response
        contains item metadata only, not expanded run or thread payloads.
        status=archived returns items whose queue review requirements have been
        satisfied, not merely items the caller personally marked completed.

        Args:
          status: Review section: needs_my_review, needs_others_review, or archived

          agreement: Only completed items whose reviewers disagreed on at least one rubric key.
              Returns 501 unless multi-reviewer queues are on for the workspace. Requires
              status=archived

          cursor: Opaque pagination cursor

          direction: Pagination direction. backward requires cursor

          has_unresolved_keys: Only completed items that do (true) or do not (false) still have a disagreed
              rubric key with no final answer. Items with no agreement result match neither
              value. Returns 501 unless multi-reviewer queues are on for the workspace.
              Requires status=archived

          item_type: Filter to RUN or THREAD

          max_start_time: Only items whose trace start time is at or before this timestamp. Omit or send
              the zero time for no bound

          min_start_time: Only items whose trace start time is at or after this timestamp. Omit or send
              the zero time for no bound

          page_size: Page size (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items", queue_id=queue_id),
            page=SyncItemsCursorGetPagination[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "agreement": agreement,
                        "cursor": cursor,
                        "direction": direction,
                        "has_unresolved_keys": has_unresolved_keys,
                        "item_type": item_type,
                        "max_start_time": max_start_time,
                        "min_start_time": min_start_time,
                        "page_size": page_size,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    def clear_final(
        self,
        key: str,
        *,
        queue_id: str,
        item_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the final for one rubric key.

        The key's answer goes back to the
        reviewers' majority, or null when they disagreed. Clearing a key that has no
        final succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/finals/{key}",
                queue_id=queue_id,
                item_id=item_id,
                key=key,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_status(
        self,
        queue_item_id: str,
        *,
        override_added_at: str | Omit = omit,
        status: Literal["viewed", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateStatusResponse:
        """Log the caller's reviewer status for a RUN or THREAD annotation queue item.

        A
        null status re-shows the item for this reviewer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_item_id:
            raise ValueError(f"Expected a non-empty value for `queue_item_id` but received {queue_item_id!r}")
        return self._post(
            path_template(
                "/api/v1/platform/annotation-queues/items/{queue_item_id}/status", queue_item_id=queue_item_id
            ),
            body=maybe_transform(
                {
                    "override_added_at": override_added_at,
                    "status": status,
                },
                item_create_status_params.ItemCreateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateStatusResponse,
        )

    def delete_all(
        self,
        queue_id: str,
        *,
        item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteAllResponse:
        """Remove RUN or THREAD items from a single annotation queue by item ID.

        Both
        active and completed items can be removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._post(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items/delete", queue_id=queue_id),
            body=maybe_transform({"item_ids": item_ids}, item_delete_all_params.ItemDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteAllResponse,
        )

    def retrieve_count(
        self,
        queue_id: str,
        *,
        status: str,
        agreement: Literal["disagreed"] | Omit = omit,
        end_time: str | Omit = omit,
        has_unresolved_keys: bool | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        start_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveCountResponse:
        """Returns the number of annotation queue items in one status bucket.

        The two time
        windows are independent: start_time/end_time bound when an item was archived,
        min_start_time/max_start_time bound when its trace ran. Items with no trace
        start time are excluded when either of the latter is set.

        Args:
          status: Count bucket: all, needs_my_review, needs_others_review, or archived.

          agreement: Count only completed items whose reviewers disagreed on at least one rubric key.
              Returns 501 unless multi-reviewer queues are on for the workspace. Requires
              status=archived

          end_time: Archived strictly before this time. Only used when status=archived

          has_unresolved_keys: Count only completed items that do (true) or do not (false) still have a
              disagreed rubric key with no final answer. Items with no agreement result match
              neither value. Returns 501 unless multi-reviewer queues are on for the
              workspace. Requires status=archived

          max_start_time: Trace started at or before this time

          min_start_time: Trace started at or after this time

          start_time: Archived strictly after this time. Only used when status=archived

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items/count", queue_id=queue_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "agreement": agreement,
                        "end_time": end_time,
                        "has_unresolved_keys": has_unresolved_keys,
                        "max_start_time": max_start_time,
                        "min_start_time": min_start_time,
                        "start_time": start_time,
                    },
                    item_retrieve_count_params.ItemRetrieveCountParams,
                ),
            ),
            cast_to=ItemRetrieveCountResponse,
        )

    def retrieve_placement(
        self,
        item_id: str,
        *,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrievePlacementResponse:
        """
        Resolve a RUN or THREAD item to its current review section and zero-based
        position for deep linking. The returned cursor counts RUN and THREAD items
        together, so it is only valid for a list request with no item_type or start-time
        filter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/placement",
                queue_id=queue_id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrievePlacementResponse,
        )

    def set_final(
        self,
        key: str,
        *,
        queue_id: str,
        item_id: str,
        score: float | Omit = omit,
        value: str | Omit = omit,
        values: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemSetFinalResponse:
        """
        Set the answer downstream uses for one rubric key when the item's reviewers
        disagreed. A key that already has a final can be changed even after reviewers
        come to agree. Multi-select keys take a list of category labels in values.
        final_set_by is empty for API key callers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._put(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/finals/{key}",
                queue_id=queue_id,
                item_id=item_id,
                key=key,
            ),
            body=maybe_transform(
                {
                    "score": score,
                    "value": value,
                    "values": values,
                },
                item_set_final_params.ItemSetFinalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemSetFinalResponse,
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        queue_id: str,
        *,
        extend_trace_retention: bool | Omit = omit,
        items: Iterable[item_create_params.Item] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateResponse:
        """Add RUN or THREAD items to a single annotation queue.

        RUN items require run_id
        unless they are created from a suggested example. THREAD items require thread_id
        and project_id.

        Args:
          extend_trace_retention: Defaults to false. When true, upgrade the traces of added runs from base to
              extended retention. Thread items are not upgraded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._post(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items", queue_id=queue_id),
            body=await async_maybe_transform({"items": items}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"extend_trace_retention": extend_trace_retention}, item_create_params.ItemCreateParams
                ),
            ),
            cast_to=ItemCreateResponse,
        )

    async def update(
        self,
        item_id: str,
        *,
        queue_id: str,
        added_at: Union[str, datetime] | Omit = omit,
        last_reviewed_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUpdateResponse:
        """
        Partially update mutable timestamps (added_at, last_reviewed_time) for a RUN or
        THREAD annotation queue item. Omit a field, or pass JSON null, to leave it
        unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._patch(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}", queue_id=queue_id, item_id=item_id
            ),
            body=await async_maybe_transform(
                {
                    "added_at": added_at,
                    "last_reviewed_time": last_reviewed_time,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemUpdateResponse,
        )

    def list(
        self,
        queue_id: str,
        *,
        status: Literal["needs_my_review", "needs_others_review", "archived"],
        agreement: Literal["disagreed"] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["forward", "backward"] | Omit = omit,
        has_unresolved_keys: bool | Omit = omit,
        item_type: Literal["RUN", "THREAD"] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ItemListResponse, AsyncItemsCursorGetPagination[ItemListResponse]]:
        """
        List RUN and THREAD items in a single annotation queue for one review status
        section, with opaque cursor pagination. Optional item_type=RUN|THREAD filters
        the page. Optional min_start_time/max_start_time bound the item's trace start
        time; items with no start time are excluded when either bound is set.
        direction=backward returns items before the supplied cursor. The response
        contains item metadata only, not expanded run or thread payloads.
        status=archived returns items whose queue review requirements have been
        satisfied, not merely items the caller personally marked completed.

        Args:
          status: Review section: needs_my_review, needs_others_review, or archived

          agreement: Only completed items whose reviewers disagreed on at least one rubric key.
              Returns 501 unless multi-reviewer queues are on for the workspace. Requires
              status=archived

          cursor: Opaque pagination cursor

          direction: Pagination direction. backward requires cursor

          has_unresolved_keys: Only completed items that do (true) or do not (false) still have a disagreed
              rubric key with no final answer. Items with no agreement result match neither
              value. Returns 501 unless multi-reviewer queues are on for the workspace.
              Requires status=archived

          item_type: Filter to RUN or THREAD

          max_start_time: Only items whose trace start time is at or before this timestamp. Omit or send
              the zero time for no bound

          min_start_time: Only items whose trace start time is at or after this timestamp. Omit or send
              the zero time for no bound

          page_size: Page size (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items", queue_id=queue_id),
            page=AsyncItemsCursorGetPagination[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "agreement": agreement,
                        "cursor": cursor,
                        "direction": direction,
                        "has_unresolved_keys": has_unresolved_keys,
                        "item_type": item_type,
                        "max_start_time": max_start_time,
                        "min_start_time": min_start_time,
                        "page_size": page_size,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    async def clear_final(
        self,
        key: str,
        *,
        queue_id: str,
        item_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the final for one rubric key.

        The key's answer goes back to the
        reviewers' majority, or null when they disagreed. Clearing a key that has no
        final succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/finals/{key}",
                queue_id=queue_id,
                item_id=item_id,
                key=key,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_status(
        self,
        queue_item_id: str,
        *,
        override_added_at: str | Omit = omit,
        status: Literal["viewed", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateStatusResponse:
        """Log the caller's reviewer status for a RUN or THREAD annotation queue item.

        A
        null status re-shows the item for this reviewer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_item_id:
            raise ValueError(f"Expected a non-empty value for `queue_item_id` but received {queue_item_id!r}")
        return await self._post(
            path_template(
                "/api/v1/platform/annotation-queues/items/{queue_item_id}/status", queue_item_id=queue_item_id
            ),
            body=await async_maybe_transform(
                {
                    "override_added_at": override_added_at,
                    "status": status,
                },
                item_create_status_params.ItemCreateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateStatusResponse,
        )

    async def delete_all(
        self,
        queue_id: str,
        *,
        item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteAllResponse:
        """Remove RUN or THREAD items from a single annotation queue by item ID.

        Both
        active and completed items can be removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._post(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items/delete", queue_id=queue_id),
            body=await async_maybe_transform({"item_ids": item_ids}, item_delete_all_params.ItemDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteAllResponse,
        )

    async def retrieve_count(
        self,
        queue_id: str,
        *,
        status: str,
        agreement: Literal["disagreed"] | Omit = omit,
        end_time: str | Omit = omit,
        has_unresolved_keys: bool | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        start_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveCountResponse:
        """Returns the number of annotation queue items in one status bucket.

        The two time
        windows are independent: start_time/end_time bound when an item was archived,
        min_start_time/max_start_time bound when its trace ran. Items with no trace
        start time are excluded when either of the latter is set.

        Args:
          status: Count bucket: all, needs_my_review, needs_others_review, or archived.

          agreement: Count only completed items whose reviewers disagreed on at least one rubric key.
              Returns 501 unless multi-reviewer queues are on for the workspace. Requires
              status=archived

          end_time: Archived strictly before this time. Only used when status=archived

          has_unresolved_keys: Count only completed items that do (true) or do not (false) still have a
              disagreed rubric key with no final answer. Items with no agreement result match
              neither value. Returns 501 unless multi-reviewer queues are on for the
              workspace. Requires status=archived

          max_start_time: Trace started at or before this time

          min_start_time: Trace started at or after this time

          start_time: Archived strictly after this time. Only used when status=archived

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._get(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/items/count", queue_id=queue_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "status": status,
                        "agreement": agreement,
                        "end_time": end_time,
                        "has_unresolved_keys": has_unresolved_keys,
                        "max_start_time": max_start_time,
                        "min_start_time": min_start_time,
                        "start_time": start_time,
                    },
                    item_retrieve_count_params.ItemRetrieveCountParams,
                ),
            ),
            cast_to=ItemRetrieveCountResponse,
        )

    async def retrieve_placement(
        self,
        item_id: str,
        *,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrievePlacementResponse:
        """
        Resolve a RUN or THREAD item to its current review section and zero-based
        position for deep linking. The returned cursor counts RUN and THREAD items
        together, so it is only valid for a list request with no item_type or start-time
        filter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/placement",
                queue_id=queue_id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrievePlacementResponse,
        )

    async def set_final(
        self,
        key: str,
        *,
        queue_id: str,
        item_id: str,
        score: float | Omit = omit,
        value: str | Omit = omit,
        values: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemSetFinalResponse:
        """
        Set the answer downstream uses for one rubric key when the item's reviewers
        disagreed. A key that already has a final can be changed even after reviewers
        come to agree. Multi-select keys take a list of category labels in values.
        final_set_by is empty for API key callers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._put(
            path_template(
                "/api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/finals/{key}",
                queue_id=queue_id,
                item_id=item_id,
                key=key,
            ),
            body=await async_maybe_transform(
                {
                    "score": score,
                    "value": value,
                    "values": values,
                },
                item_set_final_params.ItemSetFinalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemSetFinalResponse,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_raw_response_wrapper(
            items.create,
        )
        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.list = to_raw_response_wrapper(
            items.list,
        )
        self.clear_final = to_raw_response_wrapper(
            items.clear_final,
        )
        self.create_status = to_raw_response_wrapper(
            items.create_status,
        )
        self.delete_all = to_raw_response_wrapper(
            items.delete_all,
        )
        self.retrieve_count = to_raw_response_wrapper(
            items.retrieve_count,
        )
        self.retrieve_placement = to_raw_response_wrapper(
            items.retrieve_placement,
        )
        self.set_final = to_raw_response_wrapper(
            items.set_final,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_raw_response_wrapper(
            items.create,
        )
        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.list = async_to_raw_response_wrapper(
            items.list,
        )
        self.clear_final = async_to_raw_response_wrapper(
            items.clear_final,
        )
        self.create_status = async_to_raw_response_wrapper(
            items.create_status,
        )
        self.delete_all = async_to_raw_response_wrapper(
            items.delete_all,
        )
        self.retrieve_count = async_to_raw_response_wrapper(
            items.retrieve_count,
        )
        self.retrieve_placement = async_to_raw_response_wrapper(
            items.retrieve_placement,
        )
        self.set_final = async_to_raw_response_wrapper(
            items.set_final,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_streamed_response_wrapper(
            items.create,
        )
        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.list = to_streamed_response_wrapper(
            items.list,
        )
        self.clear_final = to_streamed_response_wrapper(
            items.clear_final,
        )
        self.create_status = to_streamed_response_wrapper(
            items.create_status,
        )
        self.delete_all = to_streamed_response_wrapper(
            items.delete_all,
        )
        self.retrieve_count = to_streamed_response_wrapper(
            items.retrieve_count,
        )
        self.retrieve_placement = to_streamed_response_wrapper(
            items.retrieve_placement,
        )
        self.set_final = to_streamed_response_wrapper(
            items.set_final,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_streamed_response_wrapper(
            items.create,
        )
        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
        self.clear_final = async_to_streamed_response_wrapper(
            items.clear_final,
        )
        self.create_status = async_to_streamed_response_wrapper(
            items.create_status,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            items.delete_all,
        )
        self.retrieve_count = async_to_streamed_response_wrapper(
            items.retrieve_count,
        )
        self.retrieve_placement = async_to_streamed_response_wrapper(
            items.retrieve_placement,
        )
        self.set_final = async_to_streamed_response_wrapper(
            items.set_final,
        )
