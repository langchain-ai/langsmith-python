# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..types import ai_search_parse_params
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ai_search_parse_response import AISearchParseResponse

__all__ = ["AISearchResource", "AsyncAISearchResource"]


class AISearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AISearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AISearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AISearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AISearchResourceWithStreamingResponse(self)

    def parse(
        self,
        *,
        ai_search: str,
        project_ids: SequenceNotStr[str],
        allow_clarification: bool | Omit = omit,
        scope: Literal["runs", "traces", "threads"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISearchParseResponse:
        """
        Translates a natural-language search into the scope, filters, semantic criterion
        and time bounds for the runs, traces or threads query API, without running the
        search. No resources are created. Send the returned fields to the query API
        named by scope, with the same projects. When scope is omitted, it is inferred
        from the search and defaults to traces. A time period in the search sets
        min_start_time or max_start_time; bounds the search does not mention are omitted
        so you can keep your own time range. Requires AI search to be enabled for the
        organization and read access to every project. Returns a single JSON response.

        Args:
          ai_search: Natural-language description of the runs, traces or threads to find, at most
              2000 UTF-8 bytes.

          project_ids: Tracing project UUIDs used to interpret the search. Send the same projects to
              the query API.

          allow_clarification: When true, an ambiguous search returns clarification options instead of a single
              plan. Defaults to false.

          scope: Query API to plan for: runs, traces or threads. When omitted, it is inferred
              from the search and defaults to traces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/ai-search/parse",
            body=maybe_transform(
                {
                    "ai_search": ai_search,
                    "project_ids": project_ids,
                    "allow_clarification": allow_clarification,
                    "scope": scope,
                },
                ai_search_parse_params.AISearchParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISearchParseResponse,
        )


class AsyncAISearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAISearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAISearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAISearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncAISearchResourceWithStreamingResponse(self)

    async def parse(
        self,
        *,
        ai_search: str,
        project_ids: SequenceNotStr[str],
        allow_clarification: bool | Omit = omit,
        scope: Literal["runs", "traces", "threads"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISearchParseResponse:
        """
        Translates a natural-language search into the scope, filters, semantic criterion
        and time bounds for the runs, traces or threads query API, without running the
        search. No resources are created. Send the returned fields to the query API
        named by scope, with the same projects. When scope is omitted, it is inferred
        from the search and defaults to traces. A time period in the search sets
        min_start_time or max_start_time; bounds the search does not mention are omitted
        so you can keep your own time range. Requires AI search to be enabled for the
        organization and read access to every project. Returns a single JSON response.

        Args:
          ai_search: Natural-language description of the runs, traces or threads to find, at most
              2000 UTF-8 bytes.

          project_ids: Tracing project UUIDs used to interpret the search. Send the same projects to
              the query API.

          allow_clarification: When true, an ambiguous search returns clarification options instead of a single
              plan. Defaults to false.

          scope: Query API to plan for: runs, traces or threads. When omitted, it is inferred
              from the search and defaults to traces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/ai-search/parse",
            body=await async_maybe_transform(
                {
                    "ai_search": ai_search,
                    "project_ids": project_ids,
                    "allow_clarification": allow_clarification,
                    "scope": scope,
                },
                ai_search_parse_params.AISearchParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISearchParseResponse,
        )


class AISearchResourceWithRawResponse:
    def __init__(self, ai_search: AISearchResource) -> None:
        self._ai_search = ai_search

        self.parse = to_raw_response_wrapper(
            ai_search.parse,
        )


class AsyncAISearchResourceWithRawResponse:
    def __init__(self, ai_search: AsyncAISearchResource) -> None:
        self._ai_search = ai_search

        self.parse = async_to_raw_response_wrapper(
            ai_search.parse,
        )


class AISearchResourceWithStreamingResponse:
    def __init__(self, ai_search: AISearchResource) -> None:
        self._ai_search = ai_search

        self.parse = to_streamed_response_wrapper(
            ai_search.parse,
        )


class AsyncAISearchResourceWithStreamingResponse:
    def __init__(self, ai_search: AsyncAISearchResource) -> None:
        self._ai_search = ai_search

        self.parse = async_to_streamed_response_wrapper(
            ai_search.parse,
        )
