# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import Trace, TraceListRunsResponse
from langsmith._utils import parse_datetime
from langsmith.pagination import SyncItemsCursorPostPagination, AsyncItemsCursorPostPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs(self, client: Langsmith) -> None:
        trace = client.traces.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs_with_all_params(self, client: Langsmith) -> None:
        trace = client.traces.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            selects=["ID"],
            accept="Accept",
        )
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_runs(self, client: Langsmith) -> None:

        response = client.traces.with_raw_response.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_runs(self, client: Langsmith) -> None:
        with client.traces.with_streaming_response.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceListRunsResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_runs(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.traces.with_raw_response.list_runs(
                trace_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Langsmith) -> None:
        trace = client.traces.query()
        assert_matches_type(SyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Langsmith) -> None:
        trace = client.traces.query(
            ai_search="A run that contains a billing dispute",
            cursor="cursor",
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=20,
            project_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            selects=["ID", "NAME", "START_TIME", "STATUS", "TOTAL_TOKENS", "TOTAL_COST", "FIRST_TOKEN_TIME"],
            trace_filter='eq(status, "error")',
            trace_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(SyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Langsmith) -> None:

        response = client.traces.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(SyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Langsmith) -> None:
        with client.traces.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(SyncItemsCursorPostPagination[Trace], trace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs(self, async_client: AsyncLangsmith) -> None:
        trace = await async_client.traces.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs_with_all_params(self, async_client: AsyncLangsmith) -> None:
        trace = await async_client.traces.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            max_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            selects=["ID"],
            accept="Accept",
        )
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_runs(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.traces.with_raw_response.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceListRunsResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_runs(self, async_client: AsyncLangsmith) -> None:
        async with async_client.traces.with_streaming_response.list_runs(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceListRunsResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_runs(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.traces.with_raw_response.list_runs(
                trace_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLangsmith) -> None:
        trace = await async_client.traces.query()
        assert_matches_type(AsyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLangsmith) -> None:
        trace = await async_client.traces.query(
            ai_search="A run that contains a billing dispute",
            cursor="cursor",
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=20,
            project_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            selects=["ID", "NAME", "START_TIME", "STATUS", "TOTAL_TOKENS", "TOTAL_COST", "FIRST_TOKEN_TIME"],
            trace_filter='eq(status, "error")',
            trace_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(AsyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.traces.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(AsyncItemsCursorPostPagination[Trace], trace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLangsmith) -> None:
        async with async_client.traces.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(AsyncItemsCursorPostPagination[Trace], trace, path=["response"])

        assert cast(Any, response.is_closed) is True
