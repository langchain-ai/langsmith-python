# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import AISearchParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAISearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse(self, client: Langsmith) -> None:
        ai_search = client.ai_search.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        )
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse_with_all_params(self, client: Langsmith) -> None:
        ai_search = client.ai_search.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
            allow_clarification=True,
            scope="runs",
        )
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_parse(self, client: Langsmith) -> None:

        response = client.ai_search.with_raw_response.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_search = response.parse()
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_parse(self, client: Langsmith) -> None:
        with client.ai_search.with_streaming_response.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_search = response.parse()
            assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAISearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse(self, async_client: AsyncLangsmith) -> None:
        ai_search = await async_client.ai_search.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        )
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse_with_all_params(self, async_client: AsyncLangsmith) -> None:
        ai_search = await async_client.ai_search.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
            allow_clarification=True,
            scope="runs",
        )
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.ai_search.with_raw_response.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_search = await response.parse()
        assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncLangsmith) -> None:
        async with async_client.ai_search.with_streaming_response.parse(
            ai_search="threads where the agent did not complete the task and spent more than $1",
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_search = await response.parse()
            assert_matches_type(AISearchParseResponse, ai_search, path=["response"])

        assert cast(Any, response.is_closed) is True
