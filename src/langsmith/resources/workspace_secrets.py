# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

from ..types import workspace_secret_list_params, workspace_secret_upsert_params
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.workspace_secret import WorkspaceSecret
from ..types.workspace_secret_list_response import WorkspaceSecretListResponse

__all__ = ["WorkspaceSecretsResource", "AsyncWorkspaceSecretsResource"]


class WorkspaceSecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspaceSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return WorkspaceSecretsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        include_configs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecretListResponse:
        """List the current workspace's secret keys.

        Values are never returned.

        Args:
          include_configs: If true, include the hosts each secret may be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/workspaces/current/secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_configs": include_configs}, workspace_secret_list_params.WorkspaceSecretListParams
                ),
            ),
            cast_to=WorkspaceSecretListResponse,
        )

    def delete(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a workspace secret and its allowed hosts.

        Requires workspace admin.

        Missing keys succeed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/workspaces/current/secrets/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        key: str,
        *,
        configs: Optional[Iterable[workspace_secret_upsert_params.Config]] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Create or update a workspace secret and the hosts it may be sent to.

        Requires workspace admin. Omit value to keep the current one; it is required to
        create a secret. configs replaces the secret's hosts; omitted or empty restores
        the built-in defaults for known provider keys. The value is never returned.

        Args:
          configs: Full replacement of the allowed hosts. Omitted or empty removes custom hosts so
              the built-in defaults, if any, apply.

          value: Secret value. Required to create a secret; omit to keep the current value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._put(
            path_template("/api/v1/workspaces/current/secrets/{key}", key=key),
            body=maybe_transform(
                {
                    "configs": configs,
                    "value": value,
                },
                workspace_secret_upsert_params.WorkspaceSecretUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
        )


class AsyncWorkspaceSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncWorkspaceSecretsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        include_configs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecretListResponse:
        """List the current workspace's secret keys.

        Values are never returned.

        Args:
          include_configs: If true, include the hosts each secret may be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/workspaces/current/secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_configs": include_configs}, workspace_secret_list_params.WorkspaceSecretListParams
                ),
            ),
            cast_to=WorkspaceSecretListResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a workspace secret and its allowed hosts.

        Requires workspace admin.

        Missing keys succeed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/workspaces/current/secrets/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        key: str,
        *,
        configs: Optional[Iterable[workspace_secret_upsert_params.Config]] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Create or update a workspace secret and the hosts it may be sent to.

        Requires workspace admin. Omit value to keep the current one; it is required to
        create a secret. configs replaces the secret's hosts; omitted or empty restores
        the built-in defaults for known provider keys. The value is never returned.

        Args:
          configs: Full replacement of the allowed hosts. Omitted or empty removes custom hosts so
              the built-in defaults, if any, apply.

          value: Secret value. Required to create a secret; omit to keep the current value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._put(
            path_template("/api/v1/workspaces/current/secrets/{key}", key=key),
            body=await async_maybe_transform(
                {
                    "configs": configs,
                    "value": value,
                },
                workspace_secret_upsert_params.WorkspaceSecretUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
        )


class WorkspaceSecretsResourceWithRawResponse:
    def __init__(self, workspace_secrets: WorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.list = to_raw_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            workspace_secrets.delete,
        )
        self.upsert = to_raw_response_wrapper(
            workspace_secrets.upsert,
        )


class AsyncWorkspaceSecretsResourceWithRawResponse:
    def __init__(self, workspace_secrets: AsyncWorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.list = async_to_raw_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workspace_secrets.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            workspace_secrets.upsert,
        )


class WorkspaceSecretsResourceWithStreamingResponse:
    def __init__(self, workspace_secrets: WorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.list = to_streamed_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            workspace_secrets.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            workspace_secrets.upsert,
        )


class AsyncWorkspaceSecretsResourceWithStreamingResponse:
    def __init__(self, workspace_secrets: AsyncWorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.list = async_to_streamed_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workspace_secrets.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            workspace_secrets.upsert,
        )
