# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.sandboxes import volume_list_params, volume_clone_params, volume_create_params, volume_update_params
from ...types.sandboxes.volume_response import VolumeResponse

__all__ = ["VolumesResource", "AsyncVolumesResource"]


class VolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return VolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return VolumesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        size_bytes: int,
        description: str | Omit = omit,
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Create an empty
        volume that can be attached to sandboxes at a mount path. The size is rounded up
        to a whole GiB.

        Args:
          name: Name is unique within the workspace.

          size_bytes: SizeBytes is the volume's capacity, rounded up to a whole GiB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/sandboxes/volumes",
            body=maybe_transform(
                {
                    "name": name,
                    "size_bytes": size_bytes,
                    "description": description,
                    "labels": labels,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    def retrieve(
        self,
        volume: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Get a sandbox volume
        by ID or name, with its current attachments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return self._get(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    def update(
        self,
        volume: str,
        *,
        description: Optional[str] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Update a volume's
        description or labels. Each field sent replaces the stored value; omitted fields
        are unchanged. Null, an empty description, or an empty labels object clears it.
        Only the volume's creator, or a role with sandboxes:exec, may update it.

        Args:
          description: Description replaces the description; null or an empty string clears it.

          labels: Labels replaces every label; null or an empty object clears them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return self._patch(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[VolumeResponse]:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. List the workspace's
        sandbox volumes with their current attachments.

        Args:
          cursor: Opaque pagination cursor from a prior response's next_cursor

          name_contains: Filter by name substring

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/sandboxes/volumes",
            page=SyncItemsCursorGetPagination[VolumeResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "name_contains": name_contains,
                        "page_size": page_size,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            model=VolumeResponse,
        )

    def delete(
        self,
        volume: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Delete a volume and
        its data. A volume attached to any sandbox cannot be deleted. Storage is
        reclaimed asynchronously. Only the volume's creator, or a role with
        sandboxes:exec, may delete it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clone(
        self,
        volume: str,
        *,
        name: str,
        description: str | Omit = omit,
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Create a new volume
        holding a copy-on-write copy of an existing one. A volume attached read-write to
        a sandbox that is not stopped cannot be cloned. Only the volume's creator, or a
        role with sandboxes:exec, may clone it.

        Args:
          name: Name of the new volume, unique within the workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return self._post(
            path_template("/api/v2/sandboxes/volumes/{volume}/clone", volume=volume),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
                volume_clone_params.VolumeCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )


class AsyncVolumesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncVolumesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        size_bytes: int,
        description: str | Omit = omit,
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Create an empty
        volume that can be attached to sandboxes at a mount path. The size is rounded up
        to a whole GiB.

        Args:
          name: Name is unique within the workspace.

          size_bytes: SizeBytes is the volume's capacity, rounded up to a whole GiB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/sandboxes/volumes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "size_bytes": size_bytes,
                    "description": description,
                    "labels": labels,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    async def retrieve(
        self,
        volume: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Get a sandbox volume
        by ID or name, with its current attachments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return await self._get(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    async def update(
        self,
        volume: str,
        *,
        description: Optional[str] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Update a volume's
        description or labels. Each field sent replaces the stored value; omitted fields
        are unchanged. Null, an empty description, or an empty labels object clears it.
        Only the volume's creator, or a role with sandboxes:exec, may update it.

        Args:
          description: Description replaces the description; null or an empty string clears it.

          labels: Labels replaces every label; null or an empty object clears them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return await self._patch(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VolumeResponse, AsyncItemsCursorGetPagination[VolumeResponse]]:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. List the workspace's
        sandbox volumes with their current attachments.

        Args:
          cursor: Opaque pagination cursor from a prior response's next_cursor

          name_contains: Filter by name substring

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/sandboxes/volumes",
            page=AsyncItemsCursorGetPagination[VolumeResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "name_contains": name_contains,
                        "page_size": page_size,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            model=VolumeResponse,
        )

    async def delete(
        self,
        volume: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Delete a volume and
        its data. A volume attached to any sandbox cannot be deleted. Storage is
        reclaimed asynchronously. Only the volume's creator, or a role with
        sandboxes:exec, may delete it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v2/sandboxes/volumes/{volume}", volume=volume),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clone(
        self,
        volume: str,
        *,
        name: str,
        description: str | Omit = omit,
        labels: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeResponse:
        """
        **Beta:** This API is in active development and may change without notice.
        Requires sandbox volumes to be enabled for your workspace. Create a new volume
        holding a copy-on-write copy of an existing one. A volume attached read-write to
        a sandbox that is not stopped cannot be cloned. Only the volume's creator, or a
        role with sandboxes:exec, may clone it.

        Args:
          name: Name of the new volume, unique within the workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume:
            raise ValueError(f"Expected a non-empty value for `volume` but received {volume!r}")
        return await self._post(
            path_template("/api/v2/sandboxes/volumes/{volume}/clone", volume=volume),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
                volume_clone_params.VolumeCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeResponse,
        )


class VolumesResourceWithRawResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_raw_response_wrapper(
            volumes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            volumes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            volumes.update,
        )
        self.list = to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = to_raw_response_wrapper(
            volumes.delete,
        )
        self.clone = to_raw_response_wrapper(
            volumes.clone,
        )


class AsyncVolumesResourceWithRawResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_raw_response_wrapper(
            volumes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            volumes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            volumes.update,
        )
        self.list = async_to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            volumes.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            volumes.clone,
        )


class VolumesResourceWithStreamingResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_streamed_response_wrapper(
            volumes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            volumes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            volumes.update,
        )
        self.list = to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = to_streamed_response_wrapper(
            volumes.delete,
        )
        self.clone = to_streamed_response_wrapper(
            volumes.clone,
        )


class AsyncVolumesResourceWithStreamingResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_streamed_response_wrapper(
            volumes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            volumes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            volumes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            volumes.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            volumes.clone,
        )
