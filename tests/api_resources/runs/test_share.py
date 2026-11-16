# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types.runs import ShareCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShare:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        share = client.runs.share.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )
        assert_matches_type(ShareCreateResponse, share, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.runs.share.with_raw_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert_matches_type(ShareCreateResponse, share, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.runs.share.with_streaming_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert_matches_type(ShareCreateResponse, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.share.with_raw_response.create(
                run_id="",
                session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
                trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        share = client.runs.share.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )
        assert share is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.runs.share.with_raw_response.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert share is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.runs.share.with_streaming_response.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.runs.share.with_raw_response.delete(
                trace_id="",
                session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            )


class TestAsyncShare:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        share = await async_client.runs.share.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )
        assert_matches_type(ShareCreateResponse, share, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.share.with_raw_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert_matches_type(ShareCreateResponse, share, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.share.with_streaming_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert_matches_type(ShareCreateResponse, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.share.with_raw_response.create(
                run_id="",
                session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
                trace_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        share = await async_client.runs.share.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )
        assert share is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.runs.share.with_raw_response.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert share is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.share.with_streaming_response.delete(
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.runs.share.with_raw_response.delete(
                trace_id="",
                session_id="018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
            )
