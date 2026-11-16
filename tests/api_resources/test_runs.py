# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    Run,
    RunGetURLResponse,
)
from langsmith._utils import parse_datetime
from langsmith.pagination import SyncItemsCursorPostPagination, AsyncItemsCursorPostPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_url(self, client: Langsmith) -> None:
        run = client.runs.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        )
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_url_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
            start_time="start_time",
        )
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_url(self, client: Langsmith) -> None:

        response = client.runs.with_raw_response.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_url(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetURLResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_url(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.get_url(
                run_id="",
                project_id="project_id",
                trace_id="trace_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_v2(self, client: Langsmith) -> None:
        run = client.runs.query_v2()
        assert_matches_type(SyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_v2_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.query_v2(
            ai_search="The customer was charged twice",
            cursor="eyJ2IjoxLCJhIjoicnVucy5xdWVyeSIsImsiOiJwYXNzIiwiYiI6InNkYiIsInQiOiJsdChjdXJzb3IsICcyMDI1LTEyLTEyIDE5OjAzOjI4LjQ4MTI1NTAxOWIxM2YyJykifQ",
            filter='and(eq(run_type, "llm"), gt(latency, 5))',
            has_error=False,
            ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327", "f47ac10b-58cc-4372-a567-0e02b2c3d479"],
            include_subtree_usage=True,
            is_root=True,
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=100,
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327", "0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328"],
            reference_dataset_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            reference_examples=["b2c3d4e5-f6a7-4b5c-9d0e-1f2a3b4c5d6e", "c3d4e5f6-a7b8-4c5d-0e1f-2a3b4c5d6e7f"],
            run_type="LLM",
            selects=["ID", "NAME", "PROJECT_ID", "START_TIME", "RUN_TYPE", "STATUS"],
            sem_filter="x",
            trace_filter='eq(status, "success")',
            trace_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(SyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_v2(self, client: Langsmith) -> None:

        response = client.runs.with_raw_response.query_v2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_v2(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.query_v2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncItemsCursorPostPagination[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_v2(self, client: Langsmith) -> None:
        run = client.runs.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_v2_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selects=["ID"],
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            accept="Accept",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_v2(self, client: Langsmith) -> None:

        response = client.runs.with_raw_response.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_v2(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_v2(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve_v2(
                run_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_url(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        )
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_url_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
            start_time="start_time",
        )
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_url(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.with_raw_response.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetURLResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_url(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.get_url(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="project_id",
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetURLResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_url(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.get_url(
                run_id="",
                project_id="project_id",
                trace_id="trace_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_v2(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.query_v2()
        assert_matches_type(AsyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_v2_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.query_v2(
            ai_search="The customer was charged twice",
            cursor="eyJ2IjoxLCJhIjoicnVucy5xdWVyeSIsImsiOiJwYXNzIiwiYiI6InNkYiIsInQiOiJsdChjdXJzb3IsICcyMDI1LTEyLTEyIDE5OjAzOjI4LjQ4MTI1NTAxOWIxM2YyJykifQ",
            filter='and(eq(run_type, "llm"), gt(latency, 5))',
            has_error=False,
            ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327", "f47ac10b-58cc-4372-a567-0e02b2c3d479"],
            include_subtree_usage=True,
            is_root=True,
            max_feedback_modified_at=parse_datetime("2024-12-31T23:59:59Z"),
            max_start_time=parse_datetime("2024-12-31T23:59:59Z"),
            min_feedback_modified_at=parse_datetime("2024-01-01T00:00:00Z"),
            min_start_time=parse_datetime("2024-01-01T00:00:00Z"),
            page_size=100,
            project_ids=["018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327", "0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328"],
            reference_dataset_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            reference_examples=["b2c3d4e5-f6a7-4b5c-9d0e-1f2a3b4c5d6e", "c3d4e5f6-a7b8-4c5d-0e1f-2a3b4c5d6e7f"],
            run_type="LLM",
            selects=["ID", "NAME", "PROJECT_ID", "START_TIME", "RUN_TYPE", "STATUS"],
            sem_filter="x",
            trace_filter='eq(status, "success")',
            trace_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
            tree_filter='has(tags, "production")',
            accept="Accept",
        )
        assert_matches_type(AsyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_v2(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.with_raw_response.query_v2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncItemsCursorPostPagination[Run], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_v2(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.query_v2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncItemsCursorPostPagination[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_v2(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_v2_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selects=["ID"],
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            accept="Accept",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_v2(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.with_raw_response.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_v2(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.retrieve_v2(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_v2(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve_v2(
                run_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
