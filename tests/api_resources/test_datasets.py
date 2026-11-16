# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import Dataset
from langsmith.pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_v2(self, client: Langsmith) -> None:
        dataset = client.datasets.list_v2()
        assert_matches_type(SyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_v2_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.list_v2(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            data_type=["kv"],
            exclude=["example_count"],
            exclude_corrections_datasets=True,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            page_size=1,
            sort_by="name",
            sort_order="asc",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_v2(self, client: Langsmith) -> None:

        response = client.datasets.with_raw_response.list_v2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_v2(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.list_v2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_v2(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.list_v2()
        assert_matches_type(AsyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_v2_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.list_v2(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            data_type=["kv"],
            exclude=["example_count"],
            exclude_corrections_datasets=True,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            page_size=1,
            sort_by="name",
            sort_order="asc",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_v2(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.datasets.with_raw_response.list_v2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_v2(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.list_v2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
