# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...types import workspace_tag_list_params
from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .keys.keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workspace_tag_list_response import WorkspaceTagListResponse

__all__ = ["WorkspaceTagsResource", "AsyncWorkspaceTagsResource"]


class WorkspaceTagsResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspaceTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return WorkspaceTagsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        resource_type: Optional[
            Literal[
                "agent",
                "custom_app",
                "dashboard",
                "dataset",
                "deployment",
                "evaluator",
                "experiment",
                "fleet_integration",
                "mcp_server",
                "project",
                "prompt",
                "queue",
                "sandbox",
                "skill",
                "snapshot_name",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceTagListResponse:
        """
        List the workspace's tag keys, each with its values.

        With resource_type, only values applied to at least one resource of that type
        are returned, and keys with no such values are left out.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/workspaces/current/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"resource_type": resource_type}, workspace_tag_list_params.WorkspaceTagListParams
                ),
            ),
            cast_to=WorkspaceTagListResponse,
        )


class AsyncWorkspaceTagsResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncWorkspaceTagsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        resource_type: Optional[
            Literal[
                "agent",
                "custom_app",
                "dashboard",
                "dataset",
                "deployment",
                "evaluator",
                "experiment",
                "fleet_integration",
                "mcp_server",
                "project",
                "prompt",
                "queue",
                "sandbox",
                "skill",
                "snapshot_name",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceTagListResponse:
        """
        List the workspace's tag keys, each with its values.

        With resource_type, only values applied to at least one resource of that type
        are returned, and keys with no such values are left out.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/workspaces/current/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"resource_type": resource_type}, workspace_tag_list_params.WorkspaceTagListParams
                ),
            ),
            cast_to=WorkspaceTagListResponse,
        )


class WorkspaceTagsResourceWithRawResponse:
    def __init__(self, workspace_tags: WorkspaceTagsResource) -> None:
        self._workspace_tags = workspace_tags

        self.list = to_raw_response_wrapper(
            workspace_tags.list,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._workspace_tags.keys)


class AsyncWorkspaceTagsResourceWithRawResponse:
    def __init__(self, workspace_tags: AsyncWorkspaceTagsResource) -> None:
        self._workspace_tags = workspace_tags

        self.list = async_to_raw_response_wrapper(
            workspace_tags.list,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._workspace_tags.keys)


class WorkspaceTagsResourceWithStreamingResponse:
    def __init__(self, workspace_tags: WorkspaceTagsResource) -> None:
        self._workspace_tags = workspace_tags

        self.list = to_streamed_response_wrapper(
            workspace_tags.list,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._workspace_tags.keys)


class AsyncWorkspaceTagsResourceWithStreamingResponse:
    def __init__(self, workspace_tags: AsyncWorkspaceTagsResource) -> None:
        self._workspace_tags = workspace_tags

        self.list = async_to_streamed_response_wrapper(
            workspace_tags.list,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._workspace_tags.keys)
