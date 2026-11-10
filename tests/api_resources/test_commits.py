# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    CommitWithLookups,
    CommitCreateResponse,
    CommitRetrieveResponse,
)
from langsmith.pagination import SyncOffsetPaginationCommits, AsyncOffsetPaginationCommits

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        commit = client.commits.create(
            repo="repo",
            owner="owner",
            manifest={},
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        commit = client.commits.create(
            repo="repo",
            owner="owner",
            manifest={},
            description="description",
            parent_commit="parent_commit",
            skip_webhooks={},
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.commits.with_raw_response.create(
            repo="repo",
            owner="owner",
            manifest={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.commits.with_streaming_response.create(
            repo="repo",
            owner="owner",
            manifest={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitCreateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.commits.with_raw_response.create(
                repo="repo",
                owner="",
                manifest={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.commits.with_raw_response.create(
                repo="",
                owner="owner",
                manifest={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        commit = client.commits.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        )
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        commit = client.commits.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
            get_examples=True,
            include="include",
            include_model=True,
            is_view=True,
        )
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.commits.with_raw_response.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.commits.with_streaming_response.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.commits.with_raw_response.retrieve(
                commit="commit",
                owner="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.commits.with_raw_response.retrieve(
                commit="commit",
                owner="owner",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commit` but received ''"):
            client.commits.with_raw_response.retrieve(
                commit="",
                owner="owner",
                repo="repo",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        commit = client.commits.list(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(SyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        commit = client.commits.list(
            repo="repo",
            owner="owner",
            include_stats=True,
            limit=1,
            offset=0,
            tag="tag",
        )
        assert_matches_type(SyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.commits.with_raw_response.list(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(SyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.commits.with_streaming_response.list(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(SyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.commits.with_raw_response.list(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.commits.with_raw_response.list(
                repo="",
                owner="owner",
            )


class TestAsyncCommits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.create(
            repo="repo",
            owner="owner",
            manifest={},
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.create(
            repo="repo",
            owner="owner",
            manifest={},
            description="description",
            parent_commit="parent_commit",
            skip_webhooks={},
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.commits.with_raw_response.create(
            repo="repo",
            owner="owner",
            manifest={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.commits.with_streaming_response.create(
            repo="repo",
            owner="owner",
            manifest={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitCreateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.commits.with_raw_response.create(
                repo="repo",
                owner="",
                manifest={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.commits.with_raw_response.create(
                repo="",
                owner="owner",
                manifest={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        )
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
            get_examples=True,
            include="include",
            include_model=True,
            is_view=True,
        )
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.commits.with_raw_response.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.commits.with_streaming_response.retrieve(
            commit="commit",
            owner="owner",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitRetrieveResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.commits.with_raw_response.retrieve(
                commit="commit",
                owner="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.commits.with_raw_response.retrieve(
                commit="commit",
                owner="owner",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commit` but received ''"):
            await async_client.commits.with_raw_response.retrieve(
                commit="",
                owner="owner",
                repo="repo",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.list(
            repo="repo",
            owner="owner",
        )
        assert_matches_type(AsyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        commit = await async_client.commits.list(
            repo="repo",
            owner="owner",
            include_stats=True,
            limit=1,
            offset=0,
            tag="tag",
        )
        assert_matches_type(AsyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.commits.with_raw_response.list(
            repo="repo",
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(AsyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.commits.with_streaming_response.list(
            repo="repo",
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(AsyncOffsetPaginationCommits[CommitWithLookups], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.commits.with_raw_response.list(
                repo="repo",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.commits.with_raw_response.list(
                repo="",
                owner="owner",
            )
