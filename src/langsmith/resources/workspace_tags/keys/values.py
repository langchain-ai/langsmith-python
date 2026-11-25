# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._httpx import httpx
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workspace_tags.keys import value_create_params, value_update_params
from ....types.workspace_tags.keys.tag_value import TagValue
from ....types.workspace_tags.keys.value_list_response import ValueListResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return ValuesResourceWithStreamingResponse(self)

    def create(
        self,
        tag_key_id: str,
        *,
        value: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Create Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        return self._post(
            path_template("/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values", tag_key_id=tag_key_id),
            body=maybe_transform(
                {
                    "value": value,
                    "description": description,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    def retrieve(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Get Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        return self._get(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    def update(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        description: Optional[str] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Update Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        return self._patch(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "value": value,
                },
                value_update_params.ValueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    def list(
        self,
        tag_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValueListResponse:
        """
        List Tag Values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        return self._get(
            path_template("/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values", tag_key_id=tag_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueListResponse,
        )

    def delete(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncValuesResourceWithStreamingResponse(self)

    async def create(
        self,
        tag_key_id: str,
        *,
        value: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Create Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        return await self._post(
            path_template("/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values", tag_key_id=tag_key_id),
            body=await async_maybe_transform(
                {
                    "value": value,
                    "description": description,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    async def retrieve(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Get Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        return await self._get(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    async def update(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        description: Optional[str] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagValue:
        """
        Update Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        return await self._patch(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "value": value,
                },
                value_update_params.ValueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagValue,
        )

    async def list(
        self,
        tag_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValueListResponse:
        """
        List Tag Values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        return await self._get(
            path_template("/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values", tag_key_id=tag_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueListResponse,
        )

    async def delete(
        self,
        tag_value_id: str,
        *,
        tag_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Tag Value

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag_key_id:
            raise ValueError(f"Expected a non-empty value for `tag_key_id` but received {tag_key_id!r}")
        if not tag_value_id:
            raise ValueError(f"Expected a non-empty value for `tag_value_id` but received {tag_value_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}",
                tag_key_id=tag_key_id,
                tag_value_id=tag_value_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_raw_response_wrapper(
            values.create,
        )
        self.retrieve = to_raw_response_wrapper(
            values.retrieve,
        )
        self.update = to_raw_response_wrapper(
            values.update,
        )
        self.list = to_raw_response_wrapper(
            values.list,
        )
        self.delete = to_raw_response_wrapper(
            values.delete,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_raw_response_wrapper(
            values.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            values.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            values.update,
        )
        self.list = async_to_raw_response_wrapper(
            values.list,
        )
        self.delete = async_to_raw_response_wrapper(
            values.delete,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_streamed_response_wrapper(
            values.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            values.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            values.update,
        )
        self.list = to_streamed_response_wrapper(
            values.list,
        )
        self.delete = to_streamed_response_wrapper(
            values.delete,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_streamed_response_wrapper(
            values.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            values.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            values.update,
        )
        self.list = async_to_streamed_response_wrapper(
            values.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            values.delete,
        )
