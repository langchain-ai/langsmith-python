# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import session_create_params, session_update_params, session_resolve_params
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.tracer_session import TracerSession
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

    def update(
        self,
        project_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
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

    async def update(
        self,
        project_id: str,
        *,
        default_dataset_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        extra: Optional[Dict[str, object]] | Omit = omit,
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


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.resolve = to_raw_response_wrapper(
            sessions.resolve,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.resolve = async_to_raw_response_wrapper(
            sessions.resolve,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.resolve = to_streamed_response_wrapper(
            sessions.resolve,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.resolve = async_to_streamed_response_wrapper(
            sessions.resolve,
        )
