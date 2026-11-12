# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    Thread,
    ThreadStats,
    ThreadTrace,
    ThreadAggregateStatsResponse,
)
from langsmith._utils import parse_datetime
from langsmith.pagination import (
    SyncItemsCursorGetPagination,
    AsyncItemsCursorGetPagination,
    SyncItemsCursorPostPagination,
    AsyncItemsCursorPostPagination,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_aggregate_stats(self, client: Langsmith) -> None:
        thread = client.threads.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        )
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_aggregate_stats_with_all_params(self, client: Langsmith) -> None:
        thread = client.threads.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
            filter='eq(status, "error")',
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            thread_filter="gte(turn_count, 3)",
            trace_filter='eq(status, "error")',
            tree_filter='has(tags, "production")',
        )
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_aggregate_stats(self, client: Langsmith) -> None:

        response = client.threads.with_raw_response.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_aggregate_stats(self, client: Langsmith) -> None:
        with client.threads.with_streaming_response.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_traces(self, client: Langsmith) -> None:
        thread = client.threads.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_traces_with_all_params(self, client: Langsmith) -> None:
        thread = client.threads.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            filter="filter",
            page_size=1,
            selects=["THREAD_ID"],
            trace_filter="trace_filter",
            tree_filter="tree_filter",
        )
        assert_matches_type(SyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_traces(self, client: Langsmith) -> None:

        response = client.threads.with_raw_response.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_traces(self, client: Langsmith) -> None:
        with client.threads.with_streaming_response.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_traces(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.with_raw_response.list_traces(
                thread_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Langsmith) -> None:
        thread = client.threads.query()
        assert_matches_type(SyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Langsmith) -> None:
        thread = client.threads.query(
            ai_search="A conversation about a refund request",
            cursor="cursor",
            filter="filter",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=20,
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            sem_filter="x",
            thread_filter="gte(turn_count, 3)",
            trace_filter='eq(status, "error")',
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(SyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Langsmith) -> None:

        response = client.threads.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(SyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Langsmith) -> None:
        with client.threads.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(SyncItemsCursorPostPagination[Thread], thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats(self, client: Langsmith) -> None:
        thread = client.threads.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats_with_all_params(self, client: Langsmith) -> None:
        thread = client.threads.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
        )
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stats(self, client: Langsmith) -> None:

        response = client.threads.with_raw_response.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stats(self, client: Langsmith) -> None:
        with client.threads.with_streaming_response.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadStats, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stats(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.with_raw_response.stats(
                thread_id="",
                selects=["TURNS"],
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_aggregate_stats(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        )
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_aggregate_stats_with_all_params(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
            filter='eq(status, "error")',
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            thread_filter="gte(turn_count, 3)",
            trace_filter='eq(status, "error")',
            tree_filter='has(tags, "production")',
        )
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_aggregate_stats(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.threads.with_raw_response.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_aggregate_stats(self, async_client: AsyncLangsmith) -> None:
        async with async_client.threads.with_streaming_response.aggregate_stats(
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            select=["THREAD_COUNT", "TRACE_COUNT", "TOTAL_TOKENS", "TOTAL_COST"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadAggregateStatsResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_traces(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_traces_with_all_params(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            filter="filter",
            page_size=1,
            selects=["THREAD_ID"],
            trace_filter="trace_filter",
            tree_filter="tree_filter",
        )
        assert_matches_type(AsyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_traces(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.threads.with_raw_response.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_traces(self, async_client: AsyncLangsmith) -> None:
        async with async_client.threads.with_streaming_response.list_traces(
            thread_id="thread_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[ThreadTrace], thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_traces(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.with_raw_response.list_traces(
                thread_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.query()
        assert_matches_type(AsyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.query(
            ai_search="A conversation about a refund request",
            cursor="cursor",
            filter="filter",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=20,
            project_id="0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328",
            sem_filter="x",
            thread_filter="gte(turn_count, 3)",
            trace_filter='eq(status, "error")',
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(AsyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.threads.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(AsyncItemsCursorPostPagination[Thread], thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLangsmith) -> None:
        async with async_client.threads.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(AsyncItemsCursorPostPagination[Thread], thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncLangsmith) -> None:
        thread = await async_client.threads.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
        )
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.threads.with_raw_response.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadStats, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncLangsmith) -> None:
        async with async_client.threads.with_streaming_response.stats(
            thread_id="thread_id",
            selects=["TURNS"],
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadStats, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stats(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.with_raw_response.stats(
                thread_id="",
                selects=["TURNS"],
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
