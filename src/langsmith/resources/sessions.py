# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import (
    session_create_params,
    session_update_params,
    session_list_v2_params,
    session_resolve_params,
    session_retrieve_params,
    session_create_v2_params,
    session_dashboard_params,
    session_update_v2_params,
    session_retrieve_v2_params,
)
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.session import Session
from ..types.tracer_session import TracerSession
from ..types.custom_charts_section import CustomChartsSection
from ..types.timedelta_input_param import TimedeltaInputParam
from ..types.run_stats_group_by_param import RunStatsGroupByParam
from ..types.session_resolve_response import SessionResolveResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        upsert: bool | Omit = omit,
        id: Optional[str] | Omit = omit,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        evaluator_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
        kicked_off_by: Optional[str] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        num_examples: Optional[int] | Omit = omit,
        num_repetitions: Optional[int] | Omit = omit,
        reference_dataset_id: Optional[str] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        tag_value_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        trace_tier: Optional[Literal["longlived", "shortlived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Create a new project.

        Args:
          longlived_ttl_days: Retention in days for traces while trace_tier is longlived. One of the
              deployment's allowed values (allowed_longlived_ttl_days in /info), up to the
              maximum of the deployment. The value is kept while trace_tier is shortlived.
              Null means the project uses the workspace retention.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/sessions",
            body=maybe_transform(
                {
                    "id": id,
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "evaluator_keys": evaluator_keys,
                    "extra": extra,
                    "kicked_off_by": kicked_off_by,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "num_examples": num_examples,
                    "num_repetitions": num_repetitions,
                    "reference_dataset_id": reference_dataset_id,
                    "start_time": start_time,
                    "tag_value_ids": tag_value_ids,
                    "trace_tier": trace_tier,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"upsert": upsert}, session_create_params.SessionCreateParams),
            ),
            cast_to=TracerSession,
        )

    def retrieve(
        self,
        project_id: str,
        *,
        include_stats: bool | Omit = omit,
        stats_start_time: Union[str, datetime, None] | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Get a specific project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return self._get(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_stats": include_stats,
                        "stats_start_time": stats_start_time,
                    },
                    session_retrieve_params.SessionRetrieveParams,
                ),
            ),
            cast_to=TracerSession,
        )

    def update(
        self,
        project_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        trace_tier: Optional[Literal["longlived", "shortlived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Update a project.

        Args:
          longlived_ttl_days: Retention in days for traces while trace_tier is longlived. One of the
              deployment's allowed values (allowed_longlived_ttl_days in /info), up to the
              maximum of the deployment. The value is kept while trace_tier is shortlived.
              Null means the project uses the workspace retention. Omit the field to keep the
              current value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._patch(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            body=maybe_transform(
                {
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "extra": extra,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "trace_tier": trace_tier,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TracerSession,
        )

    def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a specific project.

        Returns 202 when deletion is accepted.

        Cleanup runs asynchronously. Location
        identifies the affected project, not a cleanup-status endpoint. For a caller
        with read access, GET at that URL returns 200 with the project while it is still
        available, or 404 after the project is removed. A 404 does not confirm that
        background trace cleanup has finished. Polling for cleanup completion is not
        supported.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_v2(
        self,
        *,
        type: Literal["PROJECT", "AGENT", "EXPERIMENT"],
        upsert: bool | Omit = omit,
        id: str | Omit = omit,
        default_dataset_id: str | Omit = omit,
        description: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        evaluator_keys: SequenceNotStr[str] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        kicked_off_by: str | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        num_examples: int | Omit = omit,
        num_repetitions: int | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        tag_value_ids: SequenceNotStr[str] | Omit = omit,
        trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a session, or update an existing session with the same name when upsert
        is true. Returns the refreshed session representation without optional run
        statistics.

        Args:
          type: Type identifies a tracing project, Agent tracing project, or experiment.

          upsert: Update an existing session with the same name

          longlived_ttl_days: LonglivedTTLDays overrides long-lived trace retention. Null restores the
              workspace default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/sessions",
            body=maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "evaluator_keys": evaluator_keys,
                    "extra": extra,
                    "kicked_off_by": kicked_off_by,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "num_examples": num_examples,
                    "num_repetitions": num_repetitions,
                    "reference_dataset_id": reference_dataset_id,
                    "start_time": start_time,
                    "tag_value_ids": tag_value_ids,
                    "trace_tier": trace_tier,
                },
                session_create_v2_params.SessionCreateV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"upsert": upsert}, session_create_v2_params.SessionCreateV2Params),
            ),
            cast_to=Session,
        )

    def dashboard(
        self,
        session_id: str,
        *,
        end_time: Union[str, datetime, None] | Omit = omit,
        group_by: Optional[RunStatsGroupByParam] | Omit = omit,
        omit_data: bool | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        stride: TimedeltaInputParam | Omit = omit,
        timezone: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChartsSection:
        """GET with body payload — no resources created.

        Returns the prebuilt dashboard for
        the tracing project matching the query passed as the request payload.

        Args:
          group_by: Group by param for run stats.

          stride: Timedelta input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return self._post(
            path_template("/api/v1/sessions/{session_id}/dashboard", session_id=session_id),
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "group_by": group_by,
                    "omit_data": omit_data,
                    "start_time": start_time,
                    "stride": stride,
                    "timezone": timezone,
                },
                session_dashboard_params.SessionDashboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChartsSection,
        )

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_version: Union[str, datetime] | Omit = omit,
        filter: str | Omit = omit,
        include_facets: bool | Omit = omit,
        include_stats: bool | Omit = omit,
        metadata: str | Omit = omit,
        name: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        reference_dataset_id: SequenceNotStr[str] | Omit = omit,
        sort_by: Literal[
            "NAME", "START_TIME", "LAST_RUN_START_TIME", "ERROR_RATE", "LATENCY_P50", "LATENCY_P99", "FEEDBACK"
        ]
        | Omit = omit,
        sort_by_feedback_key: str | Omit = omit,
        sort_by_feedback_source: Literal["RUN", "SESSION"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        stats_filter: str | Omit = omit,
        stats_select: SequenceNotStr[str] | Omit = omit,
        stats_start_time: Union[str, datetime] | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        type: List[Literal["PROJECT", "AGENT", "EXPERIMENT"]] | Omit = omit,
        use_approx_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[Session]:
        """Returns a page of the workspace's tracing projects and experiments.

        Pass the
        response's next_cursor as cursor to fetch the next page; next_cursor is null on
        the last page. A cursor is valid only with the same query parameters as the
        request that returned it.

        Args:
          id: Only return projects with these IDs

          cursor: next_cursor from the previous page; omit for the first page

          dataset_version: Only return experiments run against this dataset version (RFC 3339 timestamp)

          filter: Filter expression, for example eq(name, 'my-project')

          include_facets: Include run facets

          include_stats: Include run statistics

          metadata: JSON object the project metadata must contain

          name: Only return the project with this exact name

          name_contains: Only return projects whose name contains this substring

          page_size: Number of projects per page

          reference_dataset_id: Only return experiments run against these dataset IDs

          sort_by: Sort column. FEEDBACK requires reference_dataset_id

          sort_by_feedback_key: Feedback key to sort by; required when sort_by is FEEDBACK

          sort_by_feedback_source: Where the sort feedback is recorded; defaults to RUN when sort_by is FEEDBACK

          sort_order: Sort direction

          stats_filter: Run filter expression that scopes the statistics

          stats_select: Statistics to include when include_stats is true; defaults to all

          stats_start_time: Only aggregate statistics at or after this time, within the last 31 days

          tag_value_id: Only return projects tagged with all of these tag value IDs

          type: Only return projects of these types

          use_approx_stats: Compute statistics from pre-aggregated data, which is faster but up to an hour
              stale

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/sessions",
            page=SyncItemsCursorGetPagination[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "dataset_version": dataset_version,
                        "filter": filter,
                        "include_facets": include_facets,
                        "include_stats": include_stats,
                        "metadata": metadata,
                        "name": name,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "reference_dataset_id": reference_dataset_id,
                        "sort_by": sort_by,
                        "sort_by_feedback_key": sort_by_feedback_key,
                        "sort_by_feedback_source": sort_by_feedback_source,
                        "sort_order": sort_order,
                        "stats_filter": stats_filter,
                        "stats_select": stats_select,
                        "stats_start_time": stats_start_time,
                        "tag_value_id": tag_value_id,
                        "type": type,
                        "use_approx_stats": use_approx_stats,
                    },
                    session_list_v2_params.SessionListV2Params,
                ),
            ),
            model=Session,
        )

    def resolve(
        self,
        *,
        kind: Literal["AGENT", "EXPERIMENT", "EVALUATOR"],
        id: str | Omit = omit,
        environment: Literal["LOCAL", "DEVELOPMENT", "STAGING", "PRODUCTION"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResolveResponse:
        """Returns the tracing project (session) an address names.

        An address is an AGENT
        (`id` and `environment`), an EXPERIMENT (`id`), or an EVALUATOR (no `id`:
        evaluator traces share one project per workspace). Send `kind` and `environment`
        in upper case, as listed; they are matched case-insensitively, while the Agent
        `id` is case-sensitive. An address that does not exist, or whose project you
        cannot read, is a 404. Pass the returned `session_id` to any endpoint that takes
        a project (session) ID. This is not supported on a BYOC data plane yet, and is a
        501 there. Self-hosted deployments need LangSmith v0.18 or later.

        Args:
          kind: The kind of address.

          id: The Agent's user-assigned id for AGENT, or the experiment's id for EXPERIMENT.
              Not set for EVALUATOR.

          environment: The Agent environment. Only set for AGENT.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/sessions/resolutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kind": kind,
                        "id": id,
                        "environment": environment,
                    },
                    session_resolve_params.SessionResolveParams,
                ),
            ),
            cast_to=SessionResolveResponse,
        )

    def retrieve_v2(
        self,
        session_id: str,
        *,
        include_stats: bool | Omit = omit,
        stats_start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """Returns one tracing project or experiment by ID.

        Pass include_stats=true to
        include run statistics.

        Args:
          include_stats: Include run statistics

          stats_start_time: Only aggregate statistics at or after this time, within the last 31 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v2/sessions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_stats": include_stats,
                        "stats_start_time": stats_start_time,
                    },
                    session_retrieve_v2_params.SessionRetrieveV2Params,
                ),
            ),
            cast_to=Session,
        )

    def update_v2(
        self,
        session_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[object] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Updates supplied fields and returns the refreshed resource without optional run
        statistics. Omitted fields remain unchanged. Null clears description,
        default_dataset_id, end_time, or extra. Extra merges top-level keys; null values
        remove keys.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            path_template("/api/v2/sessions/{session_id}", session_id=session_id),
            body=maybe_transform(
                {
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "extra": extra,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "trace_tier": trace_tier,
                },
                session_update_v2_params.SessionUpdateV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        upsert: bool | Omit = omit,
        id: Optional[str] | Omit = omit,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        evaluator_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
        kicked_off_by: Optional[str] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        num_examples: Optional[int] | Omit = omit,
        num_repetitions: Optional[int] | Omit = omit,
        reference_dataset_id: Optional[str] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        tag_value_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        trace_tier: Optional[Literal["longlived", "shortlived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Create a new project.

        Args:
          longlived_ttl_days: Retention in days for traces while trace_tier is longlived. One of the
              deployment's allowed values (allowed_longlived_ttl_days in /info), up to the
              maximum of the deployment. The value is kept while trace_tier is shortlived.
              Null means the project uses the workspace retention.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/sessions",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "evaluator_keys": evaluator_keys,
                    "extra": extra,
                    "kicked_off_by": kicked_off_by,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "num_examples": num_examples,
                    "num_repetitions": num_repetitions,
                    "reference_dataset_id": reference_dataset_id,
                    "start_time": start_time,
                    "tag_value_ids": tag_value_ids,
                    "trace_tier": trace_tier,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"upsert": upsert}, session_create_params.SessionCreateParams),
            ),
            cast_to=TracerSession,
        )

    async def retrieve(
        self,
        project_id: str,
        *,
        include_stats: bool | Omit = omit,
        stats_start_time: Union[str, datetime, None] | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Get a specific project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return await self._get(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_stats": include_stats,
                        "stats_start_time": stats_start_time,
                    },
                    session_retrieve_params.SessionRetrieveParams,
                ),
            ),
            cast_to=TracerSession,
        )

    async def update(
        self,
        project_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        trace_tier: Optional[Literal["longlived", "shortlived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TracerSession:
        """
        Update a project.

        Args:
          longlived_ttl_days: Retention in days for traces while trace_tier is longlived. One of the
              deployment's allowed values (allowed_longlived_ttl_days in /info), up to the
              maximum of the deployment. The value is kept while trace_tier is shortlived.
              Null means the project uses the workspace retention. Omit the field to keep the
              current value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._patch(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "extra": extra,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "trace_tier": trace_tier,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TracerSession,
        )

    async def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a specific project.

        Returns 202 when deletion is accepted.

        Cleanup runs asynchronously. Location
        identifies the affected project, not a cleanup-status endpoint. For a caller
        with read access, GET at that URL returns 200 with the project while it is still
        available, or 404 after the project is removed. A 404 does not confirm that
        background trace cleanup has finished. Polling for cleanup completion is not
        supported.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/sessions/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_v2(
        self,
        *,
        type: Literal["PROJECT", "AGENT", "EXPERIMENT"],
        upsert: bool | Omit = omit,
        id: str | Omit = omit,
        default_dataset_id: str | Omit = omit,
        description: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        evaluator_keys: SequenceNotStr[str] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        kicked_off_by: str | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        num_examples: int | Omit = omit,
        num_repetitions: int | Omit = omit,
        reference_dataset_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        tag_value_ids: SequenceNotStr[str] | Omit = omit,
        trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a session, or update an existing session with the same name when upsert
        is true. Returns the refreshed session representation without optional run
        statistics.

        Args:
          type: Type identifies a tracing project, Agent tracing project, or experiment.

          upsert: Update an existing session with the same name

          longlived_ttl_days: LonglivedTTLDays overrides long-lived trace retention. Null restores the
              workspace default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/sessions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "evaluator_keys": evaluator_keys,
                    "extra": extra,
                    "kicked_off_by": kicked_off_by,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "num_examples": num_examples,
                    "num_repetitions": num_repetitions,
                    "reference_dataset_id": reference_dataset_id,
                    "start_time": start_time,
                    "tag_value_ids": tag_value_ids,
                    "trace_tier": trace_tier,
                },
                session_create_v2_params.SessionCreateV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"upsert": upsert}, session_create_v2_params.SessionCreateV2Params),
            ),
            cast_to=Session,
        )

    async def dashboard(
        self,
        session_id: str,
        *,
        end_time: Union[str, datetime, None] | Omit = omit,
        group_by: Optional[RunStatsGroupByParam] | Omit = omit,
        omit_data: bool | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        stride: TimedeltaInputParam | Omit = omit,
        timezone: str | Omit = omit,
        accept: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChartsSection:
        """GET with body payload — no resources created.

        Returns the prebuilt dashboard for
        the tracing project matching the query passed as the request payload.

        Args:
          group_by: Group by param for run stats.

          stride: Timedelta input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return await self._post(
            path_template("/api/v1/sessions/{session_id}/dashboard", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "group_by": group_by,
                    "omit_data": omit_data,
                    "start_time": start_time,
                    "stride": stride,
                    "timezone": timezone,
                },
                session_dashboard_params.SessionDashboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChartsSection,
        )

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_version: Union[str, datetime] | Omit = omit,
        filter: str | Omit = omit,
        include_facets: bool | Omit = omit,
        include_stats: bool | Omit = omit,
        metadata: str | Omit = omit,
        name: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        reference_dataset_id: SequenceNotStr[str] | Omit = omit,
        sort_by: Literal[
            "NAME", "START_TIME", "LAST_RUN_START_TIME", "ERROR_RATE", "LATENCY_P50", "LATENCY_P99", "FEEDBACK"
        ]
        | Omit = omit,
        sort_by_feedback_key: str | Omit = omit,
        sort_by_feedback_source: Literal["RUN", "SESSION"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        stats_filter: str | Omit = omit,
        stats_select: SequenceNotStr[str] | Omit = omit,
        stats_start_time: Union[str, datetime] | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        type: List[Literal["PROJECT", "AGENT", "EXPERIMENT"]] | Omit = omit,
        use_approx_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Session, AsyncItemsCursorGetPagination[Session]]:
        """Returns a page of the workspace's tracing projects and experiments.

        Pass the
        response's next_cursor as cursor to fetch the next page; next_cursor is null on
        the last page. A cursor is valid only with the same query parameters as the
        request that returned it.

        Args:
          id: Only return projects with these IDs

          cursor: next_cursor from the previous page; omit for the first page

          dataset_version: Only return experiments run against this dataset version (RFC 3339 timestamp)

          filter: Filter expression, for example eq(name, 'my-project')

          include_facets: Include run facets

          include_stats: Include run statistics

          metadata: JSON object the project metadata must contain

          name: Only return the project with this exact name

          name_contains: Only return projects whose name contains this substring

          page_size: Number of projects per page

          reference_dataset_id: Only return experiments run against these dataset IDs

          sort_by: Sort column. FEEDBACK requires reference_dataset_id

          sort_by_feedback_key: Feedback key to sort by; required when sort_by is FEEDBACK

          sort_by_feedback_source: Where the sort feedback is recorded; defaults to RUN when sort_by is FEEDBACK

          sort_order: Sort direction

          stats_filter: Run filter expression that scopes the statistics

          stats_select: Statistics to include when include_stats is true; defaults to all

          stats_start_time: Only aggregate statistics at or after this time, within the last 31 days

          tag_value_id: Only return projects tagged with all of these tag value IDs

          type: Only return projects of these types

          use_approx_stats: Compute statistics from pre-aggregated data, which is faster but up to an hour
              stale

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/sessions",
            page=AsyncItemsCursorGetPagination[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "dataset_version": dataset_version,
                        "filter": filter,
                        "include_facets": include_facets,
                        "include_stats": include_stats,
                        "metadata": metadata,
                        "name": name,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "reference_dataset_id": reference_dataset_id,
                        "sort_by": sort_by,
                        "sort_by_feedback_key": sort_by_feedback_key,
                        "sort_by_feedback_source": sort_by_feedback_source,
                        "sort_order": sort_order,
                        "stats_filter": stats_filter,
                        "stats_select": stats_select,
                        "stats_start_time": stats_start_time,
                        "tag_value_id": tag_value_id,
                        "type": type,
                        "use_approx_stats": use_approx_stats,
                    },
                    session_list_v2_params.SessionListV2Params,
                ),
            ),
            model=Session,
        )

    async def resolve(
        self,
        *,
        kind: Literal["AGENT", "EXPERIMENT", "EVALUATOR"],
        id: str | Omit = omit,
        environment: Literal["LOCAL", "DEVELOPMENT", "STAGING", "PRODUCTION"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResolveResponse:
        """Returns the tracing project (session) an address names.

        An address is an AGENT
        (`id` and `environment`), an EXPERIMENT (`id`), or an EVALUATOR (no `id`:
        evaluator traces share one project per workspace). Send `kind` and `environment`
        in upper case, as listed; they are matched case-insensitively, while the Agent
        `id` is case-sensitive. An address that does not exist, or whose project you
        cannot read, is a 404. Pass the returned `session_id` to any endpoint that takes
        a project (session) ID. This is not supported on a BYOC data plane yet, and is a
        501 there. Self-hosted deployments need LangSmith v0.18 or later.

        Args:
          kind: The kind of address.

          id: The Agent's user-assigned id for AGENT, or the experiment's id for EXPERIMENT.
              Not set for EVALUATOR.

          environment: The Agent environment. Only set for AGENT.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/sessions/resolutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "kind": kind,
                        "id": id,
                        "environment": environment,
                    },
                    session_resolve_params.SessionResolveParams,
                ),
            ),
            cast_to=SessionResolveResponse,
        )

    async def retrieve_v2(
        self,
        session_id: str,
        *,
        include_stats: bool | Omit = omit,
        stats_start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """Returns one tracing project or experiment by ID.

        Pass include_stats=true to
        include run statistics.

        Args:
          include_stats: Include run statistics

          stats_start_time: Only aggregate statistics at or after this time, within the last 31 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v2/sessions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_stats": include_stats,
                        "stats_start_time": stats_start_time,
                    },
                    session_retrieve_v2_params.SessionRetrieveV2Params,
                ),
            ),
            cast_to=Session,
        )

    async def update_v2(
        self,
        session_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[object] | Omit = omit,
        longlived_ttl_days: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Updates supplied fields and returns the refreshed resource without optional run
        statistics. Omitted fields remain unchanged. Null clears description,
        default_dataset_id, end_time, or extra. Extra merges top-level keys; null values
        remove keys.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            path_template("/api/v2/sessions/{session_id}", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "default_dataset_id": default_dataset_id,
                    "description": description,
                    "end_time": end_time,
                    "extra": extra,
                    "longlived_ttl_days": longlived_ttl_days,
                    "name": name,
                    "trace_tier": trace_tier,
                },
                session_update_v2_params.SessionUpdateV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.create_v2 = to_raw_response_wrapper(
            sessions.create_v2,
        )
        self.dashboard = to_raw_response_wrapper(
            sessions.dashboard,
        )
        self.list_v2 = to_raw_response_wrapper(
            sessions.list_v2,
        )
        self.resolve = to_raw_response_wrapper(
            sessions.resolve,
        )
        self.retrieve_v2 = to_raw_response_wrapper(
            sessions.retrieve_v2,
        )
        self.update_v2 = to_raw_response_wrapper(
            sessions.update_v2,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.create_v2 = async_to_raw_response_wrapper(
            sessions.create_v2,
        )
        self.dashboard = async_to_raw_response_wrapper(
            sessions.dashboard,
        )
        self.list_v2 = async_to_raw_response_wrapper(
            sessions.list_v2,
        )
        self.resolve = async_to_raw_response_wrapper(
            sessions.resolve,
        )
        self.retrieve_v2 = async_to_raw_response_wrapper(
            sessions.retrieve_v2,
        )
        self.update_v2 = async_to_raw_response_wrapper(
            sessions.update_v2,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.create_v2 = to_streamed_response_wrapper(
            sessions.create_v2,
        )
        self.dashboard = to_streamed_response_wrapper(
            sessions.dashboard,
        )
        self.list_v2 = to_streamed_response_wrapper(
            sessions.list_v2,
        )
        self.resolve = to_streamed_response_wrapper(
            sessions.resolve,
        )
        self.retrieve_v2 = to_streamed_response_wrapper(
            sessions.retrieve_v2,
        )
        self.update_v2 = to_streamed_response_wrapper(
            sessions.update_v2,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.create_v2 = async_to_streamed_response_wrapper(
            sessions.create_v2,
        )
        self.dashboard = async_to_streamed_response_wrapper(
            sessions.dashboard,
        )
        self.list_v2 = async_to_streamed_response_wrapper(
            sessions.list_v2,
        )
        self.resolve = async_to_streamed_response_wrapper(
            sessions.resolve,
        )
        self.retrieve_v2 = async_to_streamed_response_wrapper(
            sessions.retrieve_v2,
        )
        self.update_v2 = async_to_streamed_response_wrapper(
            sessions.update_v2,
        )
