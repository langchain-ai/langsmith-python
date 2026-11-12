# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from langsmith._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStreaming:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Langsmith) -> None:
        streaming_stream = client.traces.streaming.query()
        streaming_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Langsmith) -> None:
        streaming_stream = client.traces.streaming.query(
            ai_search="A run that contains a billing dispute",
            cursor="cursor",
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=20,
            project_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            selects=["ID", "NAME", "START_TIME", "STATUS", "TOTAL_TOKENS", "TOTAL_COST", "FIRST_TOKEN_TIME"],
            sem_filter="x",
            trace_filter='eq(status, "error")',
            trace_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        streaming_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Langsmith) -> None:

        response = client.traces.streaming.with_raw_response.query()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Langsmith) -> None:
        with client.traces.streaming.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncStreaming:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLangsmith) -> None:
        streaming_stream = await async_client.traces.streaming.query()
        await streaming_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLangsmith) -> None:
        streaming_stream = await async_client.traces.streaming.query(
            ai_search="A run that contains a billing dispute",
            cursor="cursor",
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=20,
            project_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            selects=["ID", "NAME", "START_TIME", "STATUS", "TOTAL_TOKENS", "TOTAL_COST", "FIRST_TOKEN_TIME"],
            sem_filter="x",
            trace_filter='eq(status, "error")',
            trace_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        await streaming_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.traces.streaming.with_raw_response.query()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLangsmith) -> None:
        async with async_client.traces.streaming.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
