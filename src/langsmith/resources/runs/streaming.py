# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterator
from datetime import datetime
from typing_extensions import AsyncIterator

from ...types import RunType
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
from ...types.run import Run
from ..._streaming import Stream, AsyncStream
from ...types.runs import streaming_query_v2_params
from ..._base_client import make_request_options
from ...types.run_type import RunType
from ..._query_streaming import iter_query_stream, aiter_query_stream
from ...types.run_select_field import RunSelectField
from ...types.shared.query_patch_event import QueryPatchEvent
from ...types.runs.streaming_query_v2_response import StreamingQueryV2Response

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

    def query_v2(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        has_error: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_subtree_usage: bool | Omit = omit,
        is_root: bool | Omit = omit,
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        reference_examples: SequenceNotStr[str] | Omit = omit,
        run_type: RunType | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_id: str | Omit = omit,
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
        Returns a paginated list of runs for the given projects within min/max
        start_time. Supports filters, cursor pagination, and `selects` to select fields
        to return.

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
              at most 2000 UTF-8 bytes. Not supported on public dataset queries.

          cursor: `cursor` is the opaque string from a previous response's `next_cursor`. Treat it
              as opaque and pass it back unmodified.

          filter: `filter` narrows results to runs matching this LangSmith filter expression,
              evaluated against each individual run. For example: and(eq(run_type, "llm"),
              gt(latency, 5)) or eq(status, "error"). See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          has_error: `has_error` filters to runs that errored (true) or completed without error
              (false).

          ids: `ids` optionally limits the request to these run UUIDs.

          include_subtree_usage: `include_subtree_usage` enriches selected token and cost fields on root and
              intermediate runs with subtree totals, and selected `first_token_time` with the
              earliest observed subtree timestamp. Descendants contribute regardless of this
              request's filters or time bounds. Runs without observed descendants retain their
              original values. Defaults to false.

          is_root: `is_root` returns only root runs (true) or only non-root runs (false).

          max_feedback_modified_at: `max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`,
              or `tree_filter` (for example eq(feedback_key, "correctness")). Requires at
              least one feedback condition. Runs must still fall within the `start_time`
              window.

          max_start_time: `max_start_time` is the upper bound for run `start_time` (RFC3339). Defaults to
              now.

          min_feedback_modified_at: `min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`,
              or `tree_filter` (for example eq(feedback_key, "correctness")). Requires at
              least one feedback condition. Runs must still fall within the `start_time`
              window.

          min_start_time: `min_start_time` is the lower bound for run `start_time` (RFC3339). Defaults to
              1 day ago.

          page_size: `page_size` is the maximum number of runs to return in this response. Defaults
              to 100 when omitted; must be between 1 and 1000 inclusive when set.

          project_ids: `project_ids` lists tracing project UUIDs to query. Required unless
              `reference_dataset_id` is set. Mutually exclusive with `reference_dataset_id` —
              set exactly one of them.

          reference_dataset_id: `reference_dataset_id` resolves session IDs server-side from the dataset.
              Required unless `project_ids` is set. Mutually exclusive with `project_ids` —
              set exactly one of them. When provided and `min_start_time` is omitted, the
              server derives it from the earliest session creation date.

          reference_examples: `reference_examples` optionally limits to runs linked to these dataset example
              UUIDs.

          run_type: `run_type`, when set, restricts results to runs whose `run_type` equals this
              value.

          selects: `selects` lists which properties to include on each returned run. If omitted,
              only `id` is returned. Properties not listed are omitted from each run object.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          trace_filter: `trace_filter` narrows results to runs whose root trace matches this LangSmith
              filter expression. Use this to filter by properties of the trace's root run —
              for example eq(status, "success") to include only traces that completed without
              error. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_id: `trace_id` optionally limits results to runs belonging to this trace UUID.

          tree_filter: `tree_filter` narrows results to runs that belong to a trace containing at least
              one run matching this LangSmith filter expression anywhere in the run tree (not
              just the root). Use this to find runs inside traces that involved a specific
              tool, tag, or model — for example has(tags, "production") or eq(name,
              "my_tool"). See
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
            "/api/v2/runs/query",
            body=maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "filter": filter,
                    "has_error": has_error,
                    "ids": ids,
                    "include_subtree_usage": include_subtree_usage,
                    "is_root": is_root,
                    "max_feedback_modified_at": max_feedback_modified_at,
                    "max_start_time": max_start_time,
                    "min_feedback_modified_at": min_feedback_modified_at,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_ids": project_ids,
                    "reference_dataset_id": reference_dataset_id,
                    "reference_examples": reference_examples,
                    "run_type": run_type,
                    "selects": selects,
                    "sem_filter": sem_filter,
                    "trace_filter": trace_filter,
                    "trace_id": trace_id,
                    "tree_filter": tree_filter,
                },
                streaming_query_v2_params.StreamingQueryV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamingQueryV2Response,
            stream=True,
            stream_cls=Stream[QueryPatchEvent],
        )

    def query_v2_items(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        has_error: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_subtree_usage: bool | Omit = omit,
        is_root: bool | Omit = omit,
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        reference_examples: SequenceNotStr[str] | Omit = omit,
        run_type: RunType | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_id: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Iterator[Run]:
        """
        Streams the items of `query_v2` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return iter_query_stream(Run, self.query_v2, params)


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

    async def query_v2(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        has_error: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_subtree_usage: bool | Omit = omit,
        is_root: bool | Omit = omit,
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        reference_examples: SequenceNotStr[str] | Omit = omit,
        run_type: RunType | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_id: str | Omit = omit,
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
        Returns a paginated list of runs for the given projects within min/max
        start_time. Supports filters, cursor pagination, and `selects` to select fields
        to return.

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
              at most 2000 UTF-8 bytes. Not supported on public dataset queries.

          cursor: `cursor` is the opaque string from a previous response's `next_cursor`. Treat it
              as opaque and pass it back unmodified.

          filter: `filter` narrows results to runs matching this LangSmith filter expression,
              evaluated against each individual run. For example: and(eq(run_type, "llm"),
              gt(latency, 5)) or eq(status, "error"). See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          has_error: `has_error` filters to runs that errored (true) or completed without error
              (false).

          ids: `ids` optionally limits the request to these run UUIDs.

          include_subtree_usage: `include_subtree_usage` enriches selected token and cost fields on root and
              intermediate runs with subtree totals, and selected `first_token_time` with the
              earliest observed subtree timestamp. Descendants contribute regardless of this
              request's filters or time bounds. Runs without observed descendants retain their
              original values. Defaults to false.

          is_root: `is_root` returns only root runs (true) or only non-root runs (false).

          max_feedback_modified_at: `max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`,
              or `tree_filter` (for example eq(feedback_key, "correctness")). Requires at
              least one feedback condition. Runs must still fall within the `start_time`
              window.

          max_start_time: `max_start_time` is the upper bound for run `start_time` (RFC3339). Defaults to
              now.

          min_feedback_modified_at: `min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback
              `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`,
              or `tree_filter` (for example eq(feedback_key, "correctness")). Requires at
              least one feedback condition. Runs must still fall within the `start_time`
              window.

          min_start_time: `min_start_time` is the lower bound for run `start_time` (RFC3339). Defaults to
              1 day ago.

          page_size: `page_size` is the maximum number of runs to return in this response. Defaults
              to 100 when omitted; must be between 1 and 1000 inclusive when set.

          project_ids: `project_ids` lists tracing project UUIDs to query. Required unless
              `reference_dataset_id` is set. Mutually exclusive with `reference_dataset_id` —
              set exactly one of them.

          reference_dataset_id: `reference_dataset_id` resolves session IDs server-side from the dataset.
              Required unless `project_ids` is set. Mutually exclusive with `project_ids` —
              set exactly one of them. When provided and `min_start_time` is omitted, the
              server derives it from the earliest session creation date.

          reference_examples: `reference_examples` optionally limits to runs linked to these dataset example
              UUIDs.

          run_type: `run_type`, when set, restricts results to runs whose `run_type` equals this
              value.

          selects: `selects` lists which properties to include on each returned run. If omitted,
              only `id` is returned. Properties not listed are omitted from each run object.

          sem_filter: SemFilter evaluates a plain-language criterion against trajectory messages,
              AND-ed with structured filters.

          trace_filter: `trace_filter` narrows results to runs whose root trace matches this LangSmith
              filter expression. Use this to filter by properties of the trace's root run —
              for example eq(status, "success") to include only traces that completed without
              error. See
              https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
              for syntax.

          trace_id: `trace_id` optionally limits results to runs belonging to this trace UUID.

          tree_filter: `tree_filter` narrows results to runs that belong to a trace containing at least
              one run matching this LangSmith filter expression anywhere in the run tree (not
              just the root). Use this to find runs inside traces that involved a specific
              tool, tag, or model — for example has(tags, "production") or eq(name,
              "my_tool"). See
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
            "/api/v2/runs/query",
            body=await async_maybe_transform(
                {
                    "ai_search": ai_search,
                    "cursor": cursor,
                    "filter": filter,
                    "has_error": has_error,
                    "ids": ids,
                    "include_subtree_usage": include_subtree_usage,
                    "is_root": is_root,
                    "max_feedback_modified_at": max_feedback_modified_at,
                    "max_start_time": max_start_time,
                    "min_feedback_modified_at": min_feedback_modified_at,
                    "min_start_time": min_start_time,
                    "page_size": page_size,
                    "project_ids": project_ids,
                    "reference_dataset_id": reference_dataset_id,
                    "reference_examples": reference_examples,
                    "run_type": run_type,
                    "selects": selects,
                    "sem_filter": sem_filter,
                    "trace_filter": trace_filter,
                    "trace_id": trace_id,
                    "tree_filter": tree_filter,
                },
                streaming_query_v2_params.StreamingQueryV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamingQueryV2Response,
            stream=True,
            stream_cls=AsyncStream[QueryPatchEvent],
        )

    def query_v2_items(
        self,
        *,
        ai_search: str | Omit = omit,
        cursor: str | Omit = omit,
        filter: str | Omit = omit,
        has_error: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_subtree_usage: bool | Omit = omit,
        is_root: bool | Omit = omit,
        max_feedback_modified_at: Union[str, datetime] | Omit = omit,
        max_start_time: Union[str, datetime] | Omit = omit,
        min_feedback_modified_at: Union[str, datetime] | Omit = omit,
        min_start_time: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        reference_examples: SequenceNotStr[str] | Omit = omit,
        run_type: RunType | Omit = omit,
        selects: List[RunSelectField] | Omit = omit,
        sem_filter: str | Omit = omit,
        trace_filter: str | Omit = omit,
        trace_id: str | Omit = omit,
        tree_filter: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncIterator[Run]:
        """
        Streams the items of `query_v2` one at a time across pages, following `next_cursor`.
        """
        params: Dict[str, Any] = dict(locals())
        del params["self"]
        return aiter_query_stream(Run, self.query_v2, params)


class StreamingResourceWithRawResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

        self.query_v2 = to_raw_response_wrapper(
            streaming.query_v2,
        )


class AsyncStreamingResourceWithRawResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

        self.query_v2 = async_to_raw_response_wrapper(
            streaming.query_v2,
        )


class StreamingResourceWithStreamingResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

        self.query_v2 = to_streamed_response_wrapper(
            streaming.query_v2,
        )


class AsyncStreamingResourceWithStreamingResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

        self.query_v2 = async_to_streamed_response_wrapper(
            streaming.query_v2,
        )
