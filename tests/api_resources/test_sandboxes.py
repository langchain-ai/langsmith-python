# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import SandboxListUsageCostsResponse
from langsmith._utils import parse_datetime
from langsmith.pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_usage_costs(self, client: Langsmith) -> None:
        sandbox = client.sandboxes.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_usage_costs_with_all_params(self, client: Langsmith) -> None:
        sandbox = client.sandboxes.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            granularity="HOUR",
            include_daily=True,
            include_totals=True,
            page_size=1,
            resource_ids=["string"],
            resource_type="SANDBOX",
        )
        assert_matches_type(SyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_usage_costs(self, client: Langsmith) -> None:

        response = client.sandboxes.with_raw_response.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_usage_costs(self, client: Langsmith) -> None:
        with client.sandboxes.with_streaming_response.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSandboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_usage_costs(self, async_client: AsyncLangsmith) -> None:
        sandbox = await async_client.sandboxes.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_usage_costs_with_all_params(self, async_client: AsyncLangsmith) -> None:
        sandbox = await async_client.sandboxes.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            granularity="HOUR",
            include_daily=True,
            include_totals=True,
            page_size=1,
            resource_ids=["string"],
            resource_type="SANDBOX",
        )
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_usage_costs(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.with_raw_response.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_usage_costs(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.with_streaming_response.list_usage_costs(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(
                AsyncItemsCursorGetPagination[SandboxListUsageCostsResponse], sandbox, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
