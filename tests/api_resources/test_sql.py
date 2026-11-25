# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import SqlQueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSql:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Langsmith) -> None:
        sql = client.sql.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        )
        assert_matches_type(SqlQueryResponse, sql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Langsmith) -> None:

        response = client.sql.with_raw_response.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql = response.parse()
        assert_matches_type(SqlQueryResponse, sql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Langsmith) -> None:
        with client.sql.with_streaming_response.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql = response.parse()
            assert_matches_type(SqlQueryResponse, sql, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSql:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLangsmith) -> None:
        sql = await async_client.sql.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        )
        assert_matches_type(SqlQueryResponse, sql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sql.with_raw_response.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql = await response.parse()
        assert_matches_type(SqlQueryResponse, sql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sql.with_streaming_response.query(
            project_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql = await response.parse()
            assert_matches_type(SqlQueryResponse, sql, path=["response"])

        assert cast(Any, response.is_closed) is True
