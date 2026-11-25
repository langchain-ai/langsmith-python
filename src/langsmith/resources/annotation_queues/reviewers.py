# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.annotation_queues import reviewer_list_params
from ...types.annotation_queues.reviewer_list_response import ReviewerListResponse

__all__ = ["ReviewersResource", "AsyncReviewersResource"]


class ReviewersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return ReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return ReviewersResourceWithStreamingResponse(self)

    def list(
        self,
        queue_id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[ReviewerListResponse]:
        """
        List a queue's reviewers with how many reviews each has waiting, how many they
        have completed, and when they last completed one. Includes everyone on the
        queue's roster and anyone else who has reviewed on the queue, such as people
        removed from the roster; is_on_roster tells them apart. name and email are left
        out when a reviewer cannot be looked up. Only single queues are supported, and
        the endpoint returns 501 unless multi-reviewer is on for the workspace.

        Args:
          cursor: Opaque pagination cursor

          page_size: Page size (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/reviewers", queue_id=queue_id),
            page=SyncItemsCursorGetPagination[ReviewerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    reviewer_list_params.ReviewerListParams,
                ),
            ),
            model=ReviewerListResponse,
        )


class AsyncReviewersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncReviewersResourceWithStreamingResponse(self)

    def list(
        self,
        queue_id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReviewerListResponse, AsyncItemsCursorGetPagination[ReviewerListResponse]]:
        """
        List a queue's reviewers with how many reviews each has waiting, how many they
        have completed, and when they last completed one. Includes everyone on the
        queue's roster and anyone else who has reviewed on the queue, such as people
        removed from the roster; is_on_roster tells them apart. name and email are left
        out when a reviewer cannot be looked up. Only single queues are supported, and
        the endpoint returns 501 unless multi-reviewer is on for the workspace.

        Args:
          cursor: Opaque pagination cursor

          page_size: Page size (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template("/api/v1/platform/annotation-queues/{queue_id}/reviewers", queue_id=queue_id),
            page=AsyncItemsCursorGetPagination[ReviewerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    reviewer_list_params.ReviewerListParams,
                ),
            ),
            model=ReviewerListResponse,
        )


class ReviewersResourceWithRawResponse:
    def __init__(self, reviewers: ReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = to_raw_response_wrapper(
            reviewers.list,
        )


class AsyncReviewersResourceWithRawResponse:
    def __init__(self, reviewers: AsyncReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = async_to_raw_response_wrapper(
            reviewers.list,
        )


class ReviewersResourceWithStreamingResponse:
    def __init__(self, reviewers: ReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = to_streamed_response_wrapper(
            reviewers.list,
        )


class AsyncReviewersResourceWithStreamingResponse:
    def __init__(self, reviewers: AsyncReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = async_to_streamed_response_wrapper(
            reviewers.list,
        )
