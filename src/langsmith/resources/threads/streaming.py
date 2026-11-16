# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterator
from datetime import datetime
from typing_extensions import AsyncIterator

from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.thread import Thread
from ...types.threads import streaming_query_params
from ..._query_streaming import iter_query_stream, aiter_query_stream
from ...types.shared.query_patch_event import QueryPatchEvent
from ...types.threads.streaming_query_response import StreamingQueryResponse

__all__ = ["StreamingResource", "AsyncStreamingResource"]


class StreamingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StreamingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return StreamingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return StreamingResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        sem_filter: str | Omit = omit,
        thread_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[QueryPatchEvent]:
        """GET with body payload — no resources created.

        Returns the threads in a tracing
        project matching the query passed as the request payload. Results are filtered
        by the given time range and optional filters, with cursor-based pagination.

        `ai_search` cannot be combined with `sem_filter`. With full AI search enabled,
        `ai_search` translates natural language into query filters and time bounds and
        cannot be combined with explicit filter expressions. Otherwise, `ai_search`
        retains legacy semantic-only behavior. Use `sem_filter` for semantic-only
        matching combined with structured filters. AI search requires organization
        consent. When semantic matching is needed, `Accept: text/event-stream` is
        required; requests without it return 406. AI search is unavailable on
        deployments that route queries to the v1 backend and returns 501 there.

        Self-hosted deployments require LangSmith `v0.16` or later.

        Args:
          ai_search: `ai_search` translates natural language into structured filters, semantic
              criteria and time bounds. Cannot be combined with sem_filter. With full AI
              search enabled, also cannot be combined with explicit filter expressions;
              otherwise retains legacy semantic-only behavior. Must contain nonempty text of
              at most 2000 UTF-8 bytes.

          cursor: `cursor` is the opaque string from a previous response's `next_cursor`. Omit on
              the first request; pass the returned cursor to fetch the next page.

          filter: `filter` narrows which threads are returned, using a LangSmith filter expression
              evaluated against each thread's root run. For example: has(tags, "production")
              or eq(status, "error"). See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          max_start_time: `max_start_time` is the exclusive upper bound on thread activity (RFC3339
              date-time). Defaults to now (UTC) when omitted.

          min_start_time: `min_start_time` is the inclusive lower bound on thread activity (RFC3339
              date-time). Defaults to 1 day before now (UTC) when omitted.

          page_size: `page_size` is the maximum number of threads to return in this response.
              Defaults to 20 when omitted; must be between 1 and 100 inclusive when set. The
              response may contain fewer threads than `page_size` even when `next_cursor` is
              non-null.

          project_id: `project_id` is the tracing project UUID.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          thread_filter: `thread_filter` narrows results using a LangSmith filter expression evaluated
              against each complete thread summary. Self-hosted deployments require LangSmith
              v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_filter: `trace_filter` narrows results to threads containing at least one trace whose
              root run matches this LangSmith filter expression. Trace-level aggregate fields
              are evaluated using the complete trace summary. Self-hosted deployments require
              LangSmith v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          tree_filter: `tree_filter` narrows results to threads containing at least one trace with a
              matching run anywhere in its run tree. Self-hosted deployments require LangSmith
              v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **{key: value for key, value in {"Accept": accept}.items() if is_given(value)},
            **(extra_headers or {}),
        }
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/api/v2/threads/query",
            body=maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "filter": filter,
                    "max_start_time": max_start_time,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_id": project_id,
                    "sem_filter": sem_filter,
                    "thread_filter": thread_filter,
                    "trace_filter": trace_filter,
                    "tree_filter": tree_filter,
                },
                streaming_query_params.StreamingQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamingQueryResponse,
            stream=True,
            stream_cls=Stream[QueryPatchEvent],
        )

    def query_items(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        sem_filter: str | Omit = omit,
        thread_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Iterator[Thread]:
        """
        Streams the items of `query` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return iter_query_stream(Thread, self.query, params)


class AsyncStreamingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStreamingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncStreamingResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        sem_filter: str | Omit = omit,
        thread_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[QueryPatchEvent]:
        """GET with body payload — no resources created.

        Returns the threads in a tracing
        project matching the query passed as the request payload. Results are filtered
        by the given time range and optional filters, with cursor-based pagination.

        `ai_search` cannot be combined with `sem_filter`. With full AI search enabled,
        `ai_search` translates natural language into query filters and time bounds and
        cannot be combined with explicit filter expressions. Otherwise, `ai_search`
        retains legacy semantic-only behavior. Use `sem_filter` for semantic-only
        matching combined with structured filters. AI search requires organization
        consent. When semantic matching is needed, `Accept: text/event-stream` is
        required; requests without it return 406. AI search is unavailable on
        deployments that route queries to the v1 backend and returns 501 there.

        Self-hosted deployments require LangSmith `v0.16` or later.

        Args:
          ai_search: `ai_search` translates natural language into structured filters, semantic
              criteria and time bounds. Cannot be combined with sem_filter. With full AI
              search enabled, also cannot be combined with explicit filter expressions;
              otherwise retains legacy semantic-only behavior. Must contain nonempty text of
              at most 2000 UTF-8 bytes.

          cursor: `cursor` is the opaque string from a previous response's `next_cursor`. Omit on
              the first request; pass the returned cursor to fetch the next page.

          filter: `filter` narrows which threads are returned, using a LangSmith filter expression
              evaluated against each thread's root run. For example: has(tags, "production")
              or eq(status, "error"). See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          max_start_time: `max_start_time` is the exclusive upper bound on thread activity (RFC3339
              date-time). Defaults to now (UTC) when omitted.

          min_start_time: `min_start_time` is the inclusive lower bound on thread activity (RFC3339
              date-time). Defaults to 1 day before now (UTC) when omitted.

          page_size: `page_size` is the maximum number of threads to return in this response.
              Defaults to 20 when omitted; must be between 1 and 100 inclusive when set. The
              response may contain fewer threads than `page_size` even when `next_cursor` is
              non-null.

          project_id: `project_id` is the tracing project UUID.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          thread_filter: `thread_filter` narrows results using a LangSmith filter expression evaluated
              against each complete thread summary. Self-hosted deployments require LangSmith
              v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_filter: `trace_filter` narrows results to threads containing at least one trace whose
              root run matches this LangSmith filter expression. Trace-level aggregate fields
              are evaluated using the complete trace summary. Self-hosted deployments require
              LangSmith v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          tree_filter: `tree_filter` narrows results to threads containing at least one trace with a
              matching run anywhere in its run tree. Self-hosted deployments require LangSmith
              v0.17 or later; unsupported deployments return 501. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **{key: value for key, value in {"Accept": accept}.items() if is_given(value)},
            **(extra_headers or {}),
        }
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/api/v2/threads/query",
            body=await async_maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "filter": filter,
                    "max_start_time": max_start_time,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_id": project_id,
                    "sem_filter": sem_filter,
                    "thread_filter": thread_filter,
                    "trace_filter": trace_filter,
                    "tree_filter": tree_filter,
                },
                streaming_query_params.StreamingQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamingQueryResponse,
            stream=True,
            stream_cls=AsyncStream[QueryPatchEvent],
        )

    def query_items(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        sem_filter: str | Omit = omit,
        thread_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncIterator[Thread]:
        """
        Streams the items of `query` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return aiter_query_stream(Thread, self.query, params)


class StreamingResourceWithRawResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

        self.query = to_raw_response_wrapper(
            streaming.query,
        )


class AsyncStreamingResourceWithRawResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

        self.query = async_to_raw_response_wrapper(
            streaming.query,
        )


class StreamingResourceWithStreamingResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

        self.query = to_streamed_response_wrapper(
            streaming.query,
        )


class AsyncStreamingResourceWithStreamingResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

        self.query = async_to_streamed_response_wrapper(
            streaming.query,
        )
