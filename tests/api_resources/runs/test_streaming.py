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
    def test_method_query_v2(self, client: Langsmith) -> None:
        streaming_stream = client.runs.streaming.query_v2()
        streaming_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_v2_with_all_params(self, client: Langsmith) -> None:
        streaming_stream = client.runs.streaming.query_v2(
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
        streaming_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_v2(self, client: Langsmith) -> None:

        response = client.runs.streaming.with_raw_response.query_v2()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_v2(self, client: Langsmith) -> None:
        with client.runs.streaming.with_streaming_response.query_v2() as response:
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
    async def test_method_query_v2(self, async_client: AsyncLangsmith) -> None:
        streaming_stream = await async_client.runs.streaming.query_v2()
        await streaming_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_v2_with_all_params(self, async_client: AsyncLangsmith) -> None:
        streaming_stream = await async_client.runs.streaming.query_v2(
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
        await streaming_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_v2(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.streaming.with_raw_response.query_v2()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_v2(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.streaming.with_streaming_response.query_v2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
