# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    GetRepoResponse,
    RepoWithLookups,
    CreateRepoResponse,
)
from langsmith.pagination import SyncOffsetPaginationRepos, AsyncOffsetPaginationRepos

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        repo = client.repos.create(
            is_public=True,
            repo_handle="repo_handle",
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        repo = client.repos.create(
            is_public=True,
            repo_handle="repo_handle",
            description="description",
            readme="readme",
            repo_type="prompt",
            restricted_mode=True,
            source="internal",
            tag_value_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags=["string"],
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.repos.with_raw_response.create(
            is_public=True,
            repo_handle="repo_handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.repos.with_streaming_response.create(
            is_public=True,
            repo_handle="repo_handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(CreateRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        repo = client.repos.retrieve(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(GetRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.repos.with_raw_response.retrieve(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(GetRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.repos.with_streaming_response.retrieve(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(GetRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.with_raw_response.retrieve(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.with_raw_response.retrieve(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        repo = client.repos.update(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        repo = client.repos.update(
            repo="repo",
            owner="owner",
            description="description",
            is_archived=True,
            is_public=True,
            readme="readme",
            restricted_mode=True,
            tags=["string"],
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.repos.with_raw_response.update(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.repos.with_streaming_response.update(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(CreateRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.with_raw_response.update(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.with_raw_response.update(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        repo = client.repos.list()
        assert_matches_type(SyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        repo = client.repos.list(
            has_commits=True,
            include_owners=True,
            is_archived="true",
            is_public="true",
            limit=1,
            offset=0,
            query="query",
            single_repo_type="prompt",
            repo_types=["prompt", "file"],
            sort_direction="asc",
            sort_field="num_likes",
            source="internal",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags=["string", "string"],
            tenant_handle="tenant_handle",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            upstream_repo_handle="upstream_repo_handle",
            upstream_repo_owner="upstream_repo_owner",
            with_latest_manifest=True,
        )
        assert_matches_type(SyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.repos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(SyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.repos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(SyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        repo = client.repos.delete(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(object, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.repos.with_raw_response.delete(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(object, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.repos.with_streaming_response.delete(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(object, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.with_raw_response.delete(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.with_raw_response.delete(
                repo="",
                owner="owner",
            )


class TestAsyncRepos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.create(
            is_public=True,
            repo_handle="repo_handle",
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.create(
            is_public=True,
            repo_handle="repo_handle",
            description="description",
            readme="readme",
            repo_type="prompt",
            restricted_mode=True,
            source="internal",
            tag_value_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags=["string"],
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.with_raw_response.create(
            is_public=True,
            repo_handle="repo_handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.with_streaming_response.create(
            is_public=True,
            repo_handle="repo_handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(CreateRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.retrieve(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(GetRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.with_raw_response.retrieve(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(GetRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.with_streaming_response.retrieve(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(GetRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.with_raw_response.retrieve(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.with_raw_response.retrieve(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.update(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.update(
            repo="repo",
            owner="owner",
            description="description",
            is_archived=True,
            is_public=True,
            readme="readme",
            restricted_mode=True,
            tags=["string"],
        )
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.with_raw_response.update(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(CreateRepoResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.with_streaming_response.update(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(CreateRepoResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.with_raw_response.update(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.with_raw_response.update(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.list()
        assert_matches_type(AsyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.list(
            has_commits=True,
            include_owners=True,
            is_archived="true",
            is_public="true",
            limit=1,
            offset=0,
            query="query",
            single_repo_type="prompt",
            repo_types=["prompt", "file"],
            sort_direction="asc",
            sort_field="num_likes",
            source="internal",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tags=["string", "string"],
            tenant_handle="tenant_handle",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            upstream_repo_handle="upstream_repo_handle",
            upstream_repo_owner="upstream_repo_owner",
            with_latest_manifest=True,
        )
        assert_matches_type(AsyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(AsyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(AsyncOffsetPaginationRepos[RepoWithLookups], repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        repo = await async_client.repos.delete(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(object, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.with_raw_response.delete(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(object, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.with_streaming_response.delete(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(object, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.with_raw_response.delete(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.with_raw_response.delete(
                repo="",
                owner="owner",
            )
