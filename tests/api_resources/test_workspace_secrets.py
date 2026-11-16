# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    WorkspaceSecret,
    WorkspaceSecretListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaceSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        workspace_secret = client.workspace_secrets.list()
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        workspace_secret = client.workspace_secrets.list(
            include_configs=True,
        )
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.workspace_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = response.parse()
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.workspace_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = response.parse()
            assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        workspace_secret = client.workspace_secrets.delete(
            "key",
        )
        assert workspace_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.workspace_secrets.with_raw_response.delete(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = response.parse()
        assert workspace_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.workspace_secrets.with_streaming_response.delete(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = response.parse()
            assert workspace_secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.workspace_secrets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Langsmith) -> None:
        workspace_secret = client.workspace_secrets.upsert(
            key="key",
        )
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Langsmith) -> None:
        workspace_secret = client.workspace_secrets.upsert(
            key="key",
            configs=[
                {
                    "host_pattern": "host_pattern",
                    "header_name": "header_name",
                    "header_value_template": "header_value_template",
                }
            ],
            value="x",
        )
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Langsmith) -> None:

        response = client.workspace_secrets.with_raw_response.upsert(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = response.parse()
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Langsmith) -> None:
        with client.workspace_secrets.with_streaming_response.upsert(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = response.parse()
            assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.workspace_secrets.with_raw_response.upsert(
                key="",
            )


class TestAsyncWorkspaceSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        workspace_secret = await async_client.workspace_secrets.list()
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        workspace_secret = await async_client.workspace_secrets.list(
            include_configs=True,
        )
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = await response.parse()
        assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = await response.parse()
            assert_matches_type(WorkspaceSecretListResponse, workspace_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        workspace_secret = await async_client.workspace_secrets.delete(
            "key",
        )
        assert workspace_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_secrets.with_raw_response.delete(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = await response.parse()
        assert workspace_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_secrets.with_streaming_response.delete(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = await response.parse()
            assert workspace_secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.workspace_secrets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLangsmith) -> None:
        workspace_secret = await async_client.workspace_secrets.upsert(
            key="key",
        )
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLangsmith) -> None:
        workspace_secret = await async_client.workspace_secrets.upsert(
            key="key",
            configs=[
                {
                    "host_pattern": "host_pattern",
                    "header_name": "header_name",
                    "header_value_template": "header_value_template",
                }
            ],
            value="x",
        )
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_secrets.with_raw_response.upsert(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_secret = await response.parse()
        assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_secrets.with_streaming_response.upsert(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_secret = await response.parse()
            assert_matches_type(WorkspaceSecret, workspace_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.workspace_secrets.with_raw_response.upsert(
                key="",
            )
