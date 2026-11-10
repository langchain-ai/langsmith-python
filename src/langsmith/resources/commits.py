# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..types import commit_list_params, commit_create_params, commit_retrieve_params
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPaginationCommits, AsyncOffsetPaginationCommits
from .._base_client import AsyncPaginator, make_request_options
from ..types.commit_with_lookups import CommitWithLookups
from ..types.commit_create_response import CommitCreateResponse
from ..types.commit_retrieve_response import CommitRetrieveResponse

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return CommitsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        manifest: object,
        description: str | Omit = omit,
        parent_commit: str | Omit = omit,
        skip_webhooks: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitCreateResponse:
        """Creates a new commit in a repository.

        Requires authentication and write access
        to the repository.

        Args:
          skip_webhooks: SkipWebhooks allows skipping webhook notifications. Can be true (boolean) to
              skip all, or an array of webhook UUIDs to skip specific ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            path_template("/api/v1/commits/{owner}/{repo}", owner=owner, repo=repo),
            body=maybe_transform(
                {
                    "manifest": manifest,
                    "description": description,
                    "parent_commit": parent_commit,
                    "skip_webhooks": skip_webhooks,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitCreateResponse,
        )

    def retrieve(
        self,
        commit: str,
        *,
        owner: str,
        repo: str,
        get_examples: bool | Omit = omit,
        include: str | Omit = omit,
        include_model: bool | Omit = omit,
        is_view: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitRetrieveResponse:
        """Retrieves a specific commit by hash, tag, or "latest" for a repository.

        This
        endpoint supports both authenticated and unauthenticated access. Authenticated
        users can access private repos, while unauthenticated users can only access
        public repos. Commit resolution logic:

        - "latest" or empty: Get the most recent commit
        - Less than 8 characters: Only check for tags
        - 8 or more characters: Prioritize commit hash over tag, check both

        Args:
          include: Comma-separated list of optional fields: "model", "is_draft"

          include_model: Deprecated: use Include instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not commit:
            raise ValueError(f"Expected a non-empty value for `commit` but received {commit!r}")
        return self._get(
            path_template("/api/v1/commits/{owner}/{repo}/{commit}", owner=owner, repo=repo, commit=commit),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "get_examples": get_examples,
                        "include": include,
                        "include_model": include_model,
                        "is_view": is_view,
                    },
                    commit_retrieve_params.CommitRetrieveParams,
                ),
            ),
            cast_to=CommitRetrieveResponse,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        include_stats: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPaginationCommits[CommitWithLookups]:
        """List commits for a repository, newest first, with pagination support.

        This
        endpoint supports both authenticated and unauthenticated access. Authenticated
        users can access private repositories; unauthenticated users can only access
        public repositories. The include_stats parameter controls whether download and
        view statistics are computed (defaults to true).

        Args:
          include_stats: IncludeStats determines whether to compute num_downloads and num_views

          limit: Limit is the pagination limit.

          offset: Offset is the pagination offset.

          tag: Tag filters commits to only those with a specific tag (e.g. "production",
              "staging")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get_api_list(
            path_template("/api/v1/commits/{owner}/{repo}", owner=owner, repo=repo),
            page=SyncOffsetPaginationCommits[CommitWithLookups],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_stats": include_stats,
                        "limit": limit,
                        "offset": offset,
                        "tag": tag,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            model=CommitWithLookups,
        )


class AsyncCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        manifest: object,
        description: str | Omit = omit,
        parent_commit: str | Omit = omit,
        skip_webhooks: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitCreateResponse:
        """Creates a new commit in a repository.

        Requires authentication and write access
        to the repository.

        Args:
          skip_webhooks: SkipWebhooks allows skipping webhook notifications. Can be true (boolean) to
              skip all, or an array of webhook UUIDs to skip specific ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            path_template("/api/v1/commits/{owner}/{repo}", owner=owner, repo=repo),
            body=await async_maybe_transform(
                {
                    "manifest": manifest,
                    "description": description,
                    "parent_commit": parent_commit,
                    "skip_webhooks": skip_webhooks,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitCreateResponse,
        )

    async def retrieve(
        self,
        commit: str,
        *,
        owner: str,
        repo: str,
        get_examples: bool | Omit = omit,
        include: str | Omit = omit,
        include_model: bool | Omit = omit,
        is_view: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitRetrieveResponse:
        """Retrieves a specific commit by hash, tag, or "latest" for a repository.

        This
        endpoint supports both authenticated and unauthenticated access. Authenticated
        users can access private repos, while unauthenticated users can only access
        public repos. Commit resolution logic:

        - "latest" or empty: Get the most recent commit
        - Less than 8 characters: Only check for tags
        - 8 or more characters: Prioritize commit hash over tag, check both

        Args:
          include: Comma-separated list of optional fields: "model", "is_draft"

          include_model: Deprecated: use Include instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not commit:
            raise ValueError(f"Expected a non-empty value for `commit` but received {commit!r}")
        return await self._get(
            path_template("/api/v1/commits/{owner}/{repo}/{commit}", owner=owner, repo=repo, commit=commit),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "get_examples": get_examples,
                        "include": include,
                        "include_model": include_model,
                        "is_view": is_view,
                    },
                    commit_retrieve_params.CommitRetrieveParams,
                ),
            ),
            cast_to=CommitRetrieveResponse,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        include_stats: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CommitWithLookups, AsyncOffsetPaginationCommits[CommitWithLookups]]:
        """List commits for a repository, newest first, with pagination support.

        This
        endpoint supports both authenticated and unauthenticated access. Authenticated
        users can access private repositories; unauthenticated users can only access
        public repositories. The include_stats parameter controls whether download and
        view statistics are computed (defaults to true).

        Args:
          include_stats: IncludeStats determines whether to compute num_downloads and num_views

          limit: Limit is the pagination limit.

          offset: Offset is the pagination offset.

          tag: Tag filters commits to only those with a specific tag (e.g. "production",
              "staging")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get_api_list(
            path_template("/api/v1/commits/{owner}/{repo}", owner=owner, repo=repo),
            page=AsyncOffsetPaginationCommits[CommitWithLookups],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_stats": include_stats,
                        "limit": limit,
                        "offset": offset,
                        "tag": tag,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            model=CommitWithLookups,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_raw_response_wrapper(
            commits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            commits.list,
        )


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_raw_response_wrapper(
            commits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            commits.list,
        )


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_streamed_response_wrapper(
            commits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            commits.list,
        )


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_streamed_response_wrapper(
            commits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            commits.list,
        )
