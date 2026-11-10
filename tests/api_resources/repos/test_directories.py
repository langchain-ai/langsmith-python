# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types.repos import (
    DirectoryListResponse,
    DirectoryCommitResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        directory = client.repos.directories.list(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        directory = client.repos.directories.list(
            repo="repo",
            owner="owner",
            commit="commit",
        )
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.repos.directories.with_raw_response.list(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.repos.directories.with_streaming_response.list(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryListResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.directories.with_raw_response.list(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.directories.with_raw_response.list(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        directory = client.repos.directories.delete(
            repo="repo",
            owner="owner",
        )
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Langsmith) -> None:
        directory = client.repos.directories.delete(
            repo="repo",
            owner="owner",
            repo_type="agent",
        )
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.repos.directories.with_raw_response.delete(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.repos.directories.with_streaming_response.delete(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert directory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.directories.with_raw_response.delete(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.directories.with_raw_response.delete(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_commit(self, client: Langsmith) -> None:
        directory = client.repos.directories.commit(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_commit_with_all_params(self, client: Langsmith) -> None:
        directory = client.repos.directories.commit(
            repo="repo",
            owner="owner",
            files={
                "agents/pinned": {
                    "repo_handle": "review-agent",
                    "type": "agent",
                    "commit_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "selector": {
                        "commit_id": "0198f3ab-7c2d-7def-8a91-23456789abcd",
                        "type": "COMMIT",
                    },
                },
                "skills/current": {
                    "repo_handle": "shared-skill",
                    "type": "skill",
                    "commit_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "selector": {"type": "LATEST"},
                },
            },
            parent_commit="parent_commit",
            skip_webhooks=True,
        )
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_commit(self, client: Langsmith) -> None:

        response = client.repos.directories.with_raw_response.commit(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_commit(self, client: Langsmith) -> None:
        with client.repos.directories.with_streaming_response.commit(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_commit(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.repos.directories.with_raw_response.commit(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.directories.with_raw_response.commit(
                repo="",
                owner="owner",
            )


class TestAsyncDirectories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.list(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.list(
            repo="repo",
            owner="owner",
            commit="commit",
        )
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.directories.with_raw_response.list(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoryListResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.directories.with_streaming_response.list(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryListResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.directories.with_raw_response.list(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.directories.with_raw_response.list(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.delete(
            repo="repo",
            owner="owner",
        )
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.delete(
            repo="repo",
            owner="owner",
            repo_type="agent",
        )
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.directories.with_raw_response.delete(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert directory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.directories.with_streaming_response.delete(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert directory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.directories.with_raw_response.delete(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.directories.with_raw_response.delete(
                repo="",
                owner="owner",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_commit(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.commit(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_commit_with_all_params(self, async_client: AsyncLangsmith) -> None:
        directory = await async_client.repos.directories.commit(
            repo="repo",
            owner="owner",
            files={
                "agents/pinned": {
                    "repo_handle": "review-agent",
                    "type": "agent",
                    "commit_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "selector": {
                        "commit_id": "0198f3ab-7c2d-7def-8a91-23456789abcd",
                        "type": "COMMIT",
                    },
                },
                "skills/current": {
                    "repo_handle": "shared-skill",
                    "type": "skill",
                    "commit_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "selector": {"type": "LATEST"},
                },
            },
            parent_commit="parent_commit",
            skip_webhooks=True,
        )
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_commit(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.repos.directories.with_raw_response.commit(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = await response.parse()
        assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_commit(self, async_client: AsyncLangsmith) -> None:
        async with async_client.repos.directories.with_streaming_response.commit(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryCommitResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_commit(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.repos.directories.with_raw_response.commit(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.directories.with_raw_response.commit(
                repo="",
                owner="owner",
            )
