# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterator
from datetime import datetime
from typing_extensions import AsyncIterator

from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.trace import Trace
from ..._base_client import make_request_options
from ...types.traces import streaming_query_params
from ..._query_streaming import iter_query_stream, aiter_query_stream
from ...types.run_select_field import RunSelectField
from ...types.shared.query_patch_event import QueryPatchEvent
from ...types.traces.streaming_query_response import StreamingQueryResponse

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
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_ids: SequenceNotStr[str] | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[QueryPatchEvent]:
        """
        Returns a paginated list of traces (root runs) for a single tracing project.
        Each item carries the trace's root run plus optional trace-wide aggregates
        (`total_tokens`, `total_cost`, `first_token_time`) under `trace_aggregates`, so
        clients never have to merge by `trace_id`.

        Traces are scanned within a `start_time` window: `min_start_time` defaults to 24
        hours before the request, `max_start_time` defaults to the request time. Set
        either explicitly to widen or narrow the window.

        Supports filters (`trace_filter`, `tree_filter`), cursor pagination (`cursor`),
        and field projection (`selects`).

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

          cursor: `cursor` is the opaque string returned in a previous response's `next_cursor`.

          max_feedback_modified_at: `max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `trace_filter` or
              `tree_filter` (for example eq(feedback_key, "correctness")). Requires at least
              one feedback condition. Root runs must still fall within the `start_time`
              window.

          max_start_time: `max_start_time` is the exclusive upper bound for the root-run start time scan
              (RFC3339). Defaults to the request time when omitted.

          min_feedback_modified_at: `min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `trace_filter` or
              `tree_filter` (for example eq(feedback_key, "correctness")). Requires at least
              one feedback condition. Root runs must still fall within the `start_time`
              window.

          min_start_time: `min_start_time` is the inclusive lower bound for the root-run start time scan
              (RFC3339). Defaults to 24 hours before the request when omitted.

          page_size: `page_size` is the maximum number of traces to return per page. Defaults to 20;
              must be between 1 and 100 when set.

          project_id: `project_id` is the UUID of the tracing project that owns the traces. Required.

          selects: `selects` lists which properties to include on each returned trace. Properties
              listed here are routed to the appropriate sub-object on each item:
              `total_tokens`, `total_cost`, and `first_token_time` appear under
              `trace_aggregates`; everything else appears under `root_run`. If omitted, only
              `id` is returned on `root_run`.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          trace_filter: `trace_filter` narrows results to traces whose root run matches this LangSmith
              filter expression. This filter targets root runs only — `is_root = true` is
              implied. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_ids: `trace_ids` is an optional fast-path restriction to a known set of trace UUIDs.
              Equivalent in result to including each UUID in a `trace_filter`, but more
              efficient at scale.

          tree_filter: `tree_filter` narrows results to traces containing at least one run anywhere in
              the run tree (root or descendant) that matches this LangSmith filter expression.

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
            "/api/v2/traces/query",
            body=maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "max_feedback_modified_at": max_feedback_modified_at,
                    "max_start_time": max_start_time,
                    "min_feedback_modified_at": min_feedback_modified_at,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_id": project_id,
                    "selects": selects,
                    "sem_filter": sem_filter,
                    "trace_filter": trace_filter,
                    "trace_ids": trace_ids,
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
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_ids: SequenceNotStr[str] | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Iterator[Trace]:
        """
        Streams the items of `query` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return iter_query_stream(Trace, self.query, params)


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
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_ids: SequenceNotStr[str] | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[QueryPatchEvent]:
        """
        Returns a paginated list of traces (root runs) for a single tracing project.
        Each item carries the trace's root run plus optional trace-wide aggregates
        (`total_tokens`, `total_cost`, `first_token_time`) under `trace_aggregates`, so
        clients never have to merge by `trace_id`.

        Traces are scanned within a `start_time` window: `min_start_time` defaults to 24
        hours before the request, `max_start_time` defaults to the request time. Set
        either explicitly to widen or narrow the window.

        Supports filters (`trace_filter`, `tree_filter`), cursor pagination (`cursor`),
        and field projection (`selects`).

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

          cursor: `cursor` is the opaque string returned in a previous response's `next_cursor`.

          max_feedback_modified_at: `max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `trace_filter` or
              `tree_filter` (for example eq(feedback_key, "correctness")). Requires at least
              one feedback condition. Root runs must still fall within the `start_time`
              window.

          max_start_time: `max_start_time` is the exclusive upper bound for the root-run start time scan
              (RFC3339). Defaults to the request time when omitted.

          min_feedback_modified_at: `min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `trace_filter` or
              `tree_filter` (for example eq(feedback_key, "correctness")). Requires at least
              one feedback condition. Root runs must still fall within the `start_time`
              window.

          min_start_time: `min_start_time` is the inclusive lower bound for the root-run start time scan
              (RFC3339). Defaults to 24 hours before the request when omitted.

          page_size: `page_size` is the maximum number of traces to return per page. Defaults to 20;
              must be between 1 and 100 when set.

          project_id: `project_id` is the UUID of the tracing project that owns the traces. Required.

          selects: `selects` lists which properties to include on each returned trace. Properties
              listed here are routed to the appropriate sub-object on each item:
              `total_tokens`, `total_cost`, and `first_token_time` appear under
              `trace_aggregates`; everything else appears under `root_run`. If omitted, only
              `id` is returned on `root_run`.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          trace_filter: `trace_filter` narrows results to traces whose root run matches this LangSmith
              filter expression. This filter targets root runs only — `is_root = true` is
              implied. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_ids: `trace_ids` is an optional fast-path restriction to a known set of trace UUIDs.
              Equivalent in result to including each UUID in a `trace_filter`, but more
              efficient at scale.

          tree_filter: `tree_filter` narrows results to traces containing at least one run anywhere in
              the run tree (root or descendant) that matches this LangSmith filter expression.

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
            "/api/v2/traces/query",
            body=await async_maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "max_feedback_modified_at": max_feedback_modified_at,
                    "max_start_time": max_start_time,
                    "min_feedback_modified_at": min_feedback_modified_at,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_id": project_id,
                    "selects": selects,
                    "sem_filter": sem_filter,
                    "trace_filter": trace_filter,
                    "trace_ids": trace_ids,
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
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_ids: SequenceNotStr[str] | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncIterator[Trace]:
        """
        Streams the items of `query` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return aiter_query_stream(Trace, self.query, params)


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
