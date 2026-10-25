# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..types import agent_list_params, agent_create_params, agent_update_params, agent_retrieve_params
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from ..types.agent import Agent
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] = "EXTERNAL",
        agent_type: Literal["CUSTOM", "CODING"] | Omit = omit,
        name: str | Omit = omit,
        production_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Creates an Agent with a caller-assigned ID.

        Returns 409 if the ID already
        exists. Creates all four environments unless production_only is set for a FLEET
        agent. agent_type defaults to CUSTOM. The authenticated user becomes the owner
        when available. Requires permission to create projects. The response does not
        include runtime bindings.

        Args:
          id: Unique agent identifier: 1-63 lowercase letters, digits, or hyphens, starting
              with a letter and ending with a letter or digit.

          source_type: Agent runtime kind. Defaults to EXTERNAL for an application hosted outside LangSmith.

          agent_type: AgentType defaults to CUSTOM when omitted.

          name: Display name. Defaults to the agent ID.

          production_only: ProductionOnly creates only the PRODUCTION environment. It is accepted only when
              SourceType is FLEET; other sources always get all four environments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/agents",
            body=maybe_transform(
                {
                    "id": id,
                    "source_type": source_type,
                    "agent_type": agent_type,
                    "name": name,
                    "production_only": production_only,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        include: Literal["runtime_bindings"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Returns an Agent with the environments visible to the caller.

        The path value is
        the user-assigned Agent ID. Pass include=runtime_bindings to embed each
        environment's runtime bindings.

        Args:
          include: Relation to embed. runtime_bindings adds each environment's runtime bindings; an
              empty array means no runtime is linked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, agent_retrieve_params.AgentRetrieveParams),
            ),
            cast_to=Agent,
        )

    def update(
        self,
        agent_id: str,
        *,
        agent_type: Literal["CUSTOM", "CODING"] | Omit = omit,
        name: str | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Updates an Agent's name, source_type, agent_type, or owner_id.

        Omitted fields
        keep their values. Changing or clearing owner_id additionally requires
        workspaces:manage; assigning an owner also requires workspaces:read and active
        workspace membership. Fleet ownership cannot be changed through this endpoint.
        Changing agent_type requires workspaces:manage in addition to project update
        access; repeating the current type is a no-op. Source type can change only for
        an EXTERNAL Agent without runtime bindings. The id is immutable and is rejected
        when present. Requires update permission on every environment project.

        Args:
          agent_type: New classification. Omit to keep the current classification.

          name: New display name. Omit to keep the current name.

          owner_id: Omit to leave the owner unchanged; null clears it.

          source_type: New runtime kind. Only EXTERNAL agents without runtime bindings can change kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            body=maybe_transform(
                {
                    "agent_type": agent_type,
                    "name": name,
                    "owner_id": owner_id,
                    "source_type": source_type,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        name: str | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["last_run_start_time", "name", "created_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[Agent]:
        """Returns Agents visible to the caller.

        Each item is the same Agent shape as GET
        /api/v1/agents/{agent_id}, including the environments the caller may read. The
        list never embeds runtime bindings. An unknown query parameter, including limit,
        returns 400; use page_size to set the page size.

        Args:
          id: Exact Agent ids (repeat the parameter; maximum 100)

          cursor: Opaque pagination cursor

          name: Case-insensitive partial Agent name

          page_size: Maximum number of Agents to return

          sort_by: Field to sort by. When name is set, exact name matches still come first.

          sort_order: Sort direction

          source_type: Agent source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/agents",
            page=SyncItemsCursorGetPagination[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "name": name,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "source_type": source_type,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes an Agent, along with its environments, runtime bindings,
        runtimes, and tracing projects. This cannot be undone. Deleting an Agent that
        does not exist returns 204.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] = "EXTERNAL",
        agent_type: Literal["CUSTOM", "CODING"] | Omit = omit,
        name: str | Omit = omit,
        production_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Creates an Agent with a caller-assigned ID.

        Returns 409 if the ID already
        exists. Creates all four environments unless production_only is set for a FLEET
        agent. agent_type defaults to CUSTOM. The authenticated user becomes the owner
        when available. Requires permission to create projects. The response does not
        include runtime bindings.

        Args:
          id: Unique agent identifier: 1-63 lowercase letters, digits, or hyphens, starting
              with a letter and ending with a letter or digit.

          source_type: Agent runtime kind. Defaults to EXTERNAL for an application hosted outside LangSmith.

          agent_type: AgentType defaults to CUSTOM when omitted.

          name: Display name. Defaults to the agent ID.

          production_only: ProductionOnly creates only the PRODUCTION environment. It is accepted only when
              SourceType is FLEET; other sources always get all four environments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/agents",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "source_type": source_type,
                    "agent_type": agent_type,
                    "name": name,
                    "production_only": production_only,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        include: Literal["runtime_bindings"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Returns an Agent with the environments visible to the caller.

        The path value is
        the user-assigned Agent ID. Pass include=runtime_bindings to embed each
        environment's runtime bindings.

        Args:
          include: Relation to embed. runtime_bindings adds each environment's runtime bindings; an
              empty array means no runtime is linked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, agent_retrieve_params.AgentRetrieveParams),
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        agent_id: str,
        *,
        agent_type: Literal["CUSTOM", "CODING"] | Omit = omit,
        name: str | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Updates an Agent's name, source_type, agent_type, or owner_id.

        Omitted fields
        keep their values. Changing or clearing owner_id additionally requires
        workspaces:manage; assigning an owner also requires workspaces:read and active
        workspace membership. Fleet ownership cannot be changed through this endpoint.
        Changing agent_type requires workspaces:manage in addition to project update
        access; repeating the current type is a no-op. Source type can change only for
        an EXTERNAL Agent without runtime bindings. The id is immutable and is rejected
        when present. Requires update permission on every environment project.

        Args:
          agent_type: New classification. Omit to keep the current classification.

          name: New display name. Omit to keep the current name.

          owner_id: Omit to leave the owner unchanged; null clears it.

          source_type: New runtime kind. Only EXTERNAL agents without runtime bindings can change kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "agent_type": agent_type,
                    "name": name,
                    "owner_id": owner_id,
                    "source_type": source_type,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        name: str | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["last_run_start_time", "name", "created_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Agent, AsyncItemsCursorGetPagination[Agent]]:
        """Returns Agents visible to the caller.

        Each item is the same Agent shape as GET
        /api/v1/agents/{agent_id}, including the environments the caller may read. The
        list never embeds runtime bindings. An unknown query parameter, including limit,
        returns 400; use page_size to set the page size.

        Args:
          id: Exact Agent ids (repeat the parameter; maximum 100)

          cursor: Opaque pagination cursor

          name: Case-insensitive partial Agent name

          page_size: Maximum number of Agents to return

          sort_by: Field to sort by. When name is set, exact name matches still come first.

          sort_order: Sort direction

          source_type: Agent source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/agents",
            page=AsyncItemsCursorGetPagination[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "name": name,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "source_type": source_type,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes an Agent, along with its environments, runtime bindings,
        runtimes, and tracing projects. This cannot be undone. Deleting an Agent that
        does not exist returns 204.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
