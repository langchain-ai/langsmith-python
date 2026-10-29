# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    Evaluator,
    EvaluatorListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        evaluator = client.evaluators.list()
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        evaluator = client.evaluators.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_backfill_progress=True,
            name_contains="name_contains",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            type="session",
        )
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.evaluators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator = response.parse()
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.evaluators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator = response.parse()
            assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_decision_model(self, client: Langsmith) -> None:
        evaluator = client.evaluators.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        )
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_decision_model_with_all_params(self, client: Langsmith) -> None:
        evaluator = client.evaluators.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                    "levels": ["string"],
                    "no": "no",
                    "options": ["string"],
                    "yes": "yes",
                }
            },
            base_url="base_url",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            max_retries=0,
            model="model",
            model_headers={"foo": "string"},
            playground_settings_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="typesafe",
            sampling_rate=0,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_format="mustache",
            timeout_seconds=0,
            variable_mapping={"foo": "string"},
        )
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_decision_model(self, client: Langsmith) -> None:

        response = client.evaluators.with_raw_response.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator = response.parse()
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_decision_model(self, client: Langsmith) -> None:
        with client.evaluators.with_streaming_response.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator = response.parse()
            assert_matches_type(Evaluator, evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        evaluator = await async_client.evaluators.list()
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        evaluator = await async_client.evaluators.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluator_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_backfill_progress=True,
            name_contains="name_contains",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            type="session",
        )
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.evaluators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator = await response.parse()
        assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.evaluators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator = await response.parse()
            assert_matches_type(EvaluatorListResponse, evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_decision_model(self, async_client: AsyncLangsmith) -> None:
        evaluator = await async_client.evaluators.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        )
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_decision_model_with_all_params(self, async_client: AsyncLangsmith) -> None:
        evaluator = await async_client.evaluators.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                    "levels": ["string"],
                    "no": "no",
                    "options": ["string"],
                    "yes": "yes",
                }
            },
            base_url="base_url",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            max_retries=0,
            model="model",
            model_headers={"foo": "string"},
            playground_settings_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider="typesafe",
            sampling_rate=0,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_format="mustache",
            timeout_seconds=0,
            variable_mapping={"foo": "string"},
        )
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_decision_model(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.evaluators.with_raw_response.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator = await response.parse()
        assert_matches_type(Evaluator, evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_decision_model(self, async_client: AsyncLangsmith) -> None:
        async with async_client.evaluators.with_streaming_response.create_decision_model(
            display_name="display_name",
            prompt=[[{}, {}]],
            questions={
                "foo": {
                    "instructions": "instructions",
                    "type": "noul",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator = await response.parse()
            assert_matches_type(Evaluator, evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True
