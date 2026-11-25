# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

from ..._httpx import httpx
from ..._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.datasets import example_update_metadata_params
from ...types.datasets.example_update_metadata_response import ExampleUpdateMetadataResponse

__all__ = ["ExamplesResource", "AsyncExamplesResource"]


class ExamplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return ExamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return ExamplesResourceWithStreamingResponse(self)

    def delete(
        self,
        example_id: str,
        *,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete an example, preserving prior versions and their attachments.

        If the
        latest version is already deleted, the request succeeds without creating another
        version. Deletion is recorded at the current time or just after the latest
        version, whichever is later. For future-dated versions, latest reads reflect
        deletion immediately; timestamp reads reflect deletion only at or after the
        recorded deletion timestamp.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not example_id:
            raise ValueError(f"Expected a non-empty value for `example_id` but received {example_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/platform/datasets/{dataset_id}/examples/{example_id}",
                dataset_id=dataset_id,
                example_id=example_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_metadata(
        self,
        dataset_id: str,
        *,
        example_ids: SequenceNotStr[str],
        operations: Iterable[example_update_metadata_params.Operation],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExampleUpdateMetadataResponse:
        """
        Applies the same metadata changes, in order, to every listed example in a
        dataset. Examples that are not in the dataset or were deleted are skipped; the
        rest are updated together, so if the update fails none of them change. Answers
        207 with one status per submitted example ID: UPDATED, or NOT_FOUND for a
        skipped example. Metadata keys the operations do not name keep their values. To
        add examples to a split or remove them from one, use ARRAY_ADD or ARRAY_REMOVE
        on the dataset_split key. Requires permission to update datasets.

        Args:
          example_ids: The IDs of the examples to change; at most 10000. IDs of examples that are not
              in the dataset, or were deleted, are skipped and reported as NOT_FOUND.

          operations: The metadata changes to apply, in order; at most 50, of which at most 10 are
              array operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._patch(
            path_template("/api/v1/platform/datasets/{dataset_id}/examples/metadata", dataset_id=dataset_id),
            body=maybe_transform(
                {
                    "example_ids": example_ids,
                    "operations": operations,
                },
                example_update_metadata_params.ExampleUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExampleUpdateMetadataResponse,
        )


class AsyncExamplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncExamplesResourceWithStreamingResponse(self)

    async def delete(
        self,
        example_id: str,
        *,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete an example, preserving prior versions and their attachments.

        If the
        latest version is already deleted, the request succeeds without creating another
        version. Deletion is recorded at the current time or just after the latest
        version, whichever is later. For future-dated versions, latest reads reflect
        deletion immediately; timestamp reads reflect deletion only at or after the
        recorded deletion timestamp.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not example_id:
            raise ValueError(f"Expected a non-empty value for `example_id` but received {example_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/platform/datasets/{dataset_id}/examples/{example_id}",
                dataset_id=dataset_id,
                example_id=example_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_metadata(
        self,
        dataset_id: str,
        *,
        example_ids: SequenceNotStr[str],
        operations: Iterable[example_update_metadata_params.Operation],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExampleUpdateMetadataResponse:
        """
        Applies the same metadata changes, in order, to every listed example in a
        dataset. Examples that are not in the dataset or were deleted are skipped; the
        rest are updated together, so if the update fails none of them change. Answers
        207 with one status per submitted example ID: UPDATED, or NOT_FOUND for a
        skipped example. Metadata keys the operations do not name keep their values. To
        add examples to a split or remove them from one, use ARRAY_ADD or ARRAY_REMOVE
        on the dataset_split key. Requires permission to update datasets.

        Args:
          example_ids: The IDs of the examples to change; at most 10000. IDs of examples that are not
              in the dataset, or were deleted, are skipped and reported as NOT_FOUND.

          operations: The metadata changes to apply, in order; at most 50, of which at most 10 are
              array operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._patch(
            path_template("/api/v1/platform/datasets/{dataset_id}/examples/metadata", dataset_id=dataset_id),
            body=await async_maybe_transform(
                {
                    "example_ids": example_ids,
                    "operations": operations,
                },
                example_update_metadata_params.ExampleUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExampleUpdateMetadataResponse,
        )


class ExamplesResourceWithRawResponse:
    def __init__(self, examples: ExamplesResource) -> None:
        self._examples = examples

        self.delete = to_raw_response_wrapper(
            examples.delete,
        )
        self.update_metadata = to_raw_response_wrapper(
            examples.update_metadata,
        )


class AsyncExamplesResourceWithRawResponse:
    def __init__(self, examples: AsyncExamplesResource) -> None:
        self._examples = examples

        self.delete = async_to_raw_response_wrapper(
            examples.delete,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            examples.update_metadata,
        )


class ExamplesResourceWithStreamingResponse:
    def __init__(self, examples: ExamplesResource) -> None:
        self._examples = examples

        self.delete = to_streamed_response_wrapper(
            examples.delete,
        )
        self.update_metadata = to_streamed_response_wrapper(
            examples.update_metadata,
        )


class AsyncExamplesResourceWithStreamingResponse:
    def __init__(self, examples: AsyncExamplesResource) -> None:
        self._examples = examples

        self.delete = async_to_streamed_response_wrapper(
            examples.delete,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            examples.update_metadata,
        )
