# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    OnlineEvaluator,
    BulkDeleteEvaluatorsResponse,
    CreateOnlineEvaluatorResponse,
    UpdateOnlineEvaluatorResponse,
    GetOnlineEvaluatorSpendResponse,
)
from langsmith.pagination import SyncOffsetPaginationOnlineEvaluators, AsyncOffsetPaginationOnlineEvaluators

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnlineEvaluators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.create()
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.create(
            code_evaluator={
                "advanced_features_enabled": True,
                "code": "code",
                "code_evaluator_input": "thread",
                "dependencies": "dependencies",
                "language": "language",
                "managed_code_evaluator_key": "voice_metrics",
                "managed_code_evaluator_settings": {
                    "foo": {
                        "is_enabled": True,
                        "key_name": "key_name",
                    }
                },
                "require_attachments": True,
                "workspace_secrets_keys": ["string"],
            },
            llm_evaluator={
                "commit_hash_or_tag": "commit_hash_or_tag",
                "playground_settings_id": "playground_settings_id",
                "prompt_repo_handle": "prompt_repo_handle",
                "variable_mapping": {},
            },
            metadata={"foo": "bar"},
            name="name",
            type="llm",
        )
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.retrieve(
            "evaluator_id",
        )
        assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.retrieve(
            "evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.retrieve(
            "evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            client.online_evaluators.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.update(
            evaluator_id="evaluator_id",
        )
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.update(
            evaluator_id="evaluator_id",
            code_evaluator={
                "advanced_features_enabled": True,
                "code": "code",
                "code_evaluator_input": "thread",
                "dependencies": "dependencies",
                "language": "language",
                "managed_code_evaluator_settings": {
                    "foo": {
                        "is_enabled": True,
                        "key_name": "key_name",
                    }
                },
                "require_attachments": True,
                "workspace_secrets_keys": ["string"],
            },
            llm_evaluator={
                "commit_hash_or_tag": "commit_hash_or_tag",
                "num_few_shot_examples": 0,
                "playground_settings_id": "playground_settings_id",
                "prompt_repo_handle": "prompt_repo_handle",
                "use_corrections_dataset": True,
                "variable_mapping": {},
            },
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.update(
            evaluator_id="evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.update(
            evaluator_id="evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            client.online_evaluators.with_raw_response.update(
                evaluator_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.list()
        assert_matches_type(SyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.list(
            agent_id="agent_id",
            feedback_key="feedback_key",
            limit=0,
            metadata="metadata",
            name_contains="name_contains",
            offset=0,
            resource_id=["string"],
            sort_by="sort_by",
            sort_by_desc=True,
            tag_value_id=["string"],
            type="type",
        )
        assert_matches_type(SyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(SyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(
                SyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.delete(
            evaluator_id="evaluator_id",
        )
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.delete(
            evaluator_id="evaluator_id",
            delete_run_rules=True,
        )
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.delete(
            evaluator_id="evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.delete(
            evaluator_id="evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert online_evaluator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            client.online_evaluators.with_raw_response.delete(
                evaluator_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.bulk_delete(
            evaluator_ids=["string"],
        )
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_delete_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.bulk_delete(
            evaluator_ids=["string"],
            delete_run_rules=True,
        )
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.bulk_delete(
            evaluator_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.bulk_delete(
            evaluator_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_spend(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.spend(
            period_start="period_start",
        )
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_spend_with_all_params(self, client: Langsmith) -> None:
        online_evaluator = client.online_evaluators.spend(
            period_start="period_start",
            agent_id="agent_id",
            dataset_id="dataset_id",
            evaluator_id="evaluator_id",
            feedback_key="feedback_key",
            group_by="group_by",
            resource_id=["string"],
            session_id="session_id",
            tag_value_id=["string"],
            type="type",
        )
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_spend(self, client: Langsmith) -> None:

        response = client.online_evaluators.with_raw_response.spend(
            period_start="period_start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = response.parse()
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_spend(self, client: Langsmith) -> None:
        with client.online_evaluators.with_streaming_response.spend(
            period_start="period_start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = response.parse()
            assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnlineEvaluators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.create()
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.create(
            code_evaluator={
                "advanced_features_enabled": True,
                "code": "code",
                "code_evaluator_input": "thread",
                "dependencies": "dependencies",
                "language": "language",
                "managed_code_evaluator_key": "voice_metrics",
                "managed_code_evaluator_settings": {
                    "foo": {
                        "is_enabled": True,
                        "key_name": "key_name",
                    }
                },
                "require_attachments": True,
                "workspace_secrets_keys": ["string"],
            },
            llm_evaluator={
                "commit_hash_or_tag": "commit_hash_or_tag",
                "playground_settings_id": "playground_settings_id",
                "prompt_repo_handle": "prompt_repo_handle",
                "variable_mapping": {},
            },
            metadata={"foo": "bar"},
            name="name",
            type="llm",
        )
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(CreateOnlineEvaluatorResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.retrieve(
            "evaluator_id",
        )
        assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.retrieve(
            "evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.retrieve(
            "evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(OnlineEvaluator, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            await async_client.online_evaluators.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.update(
            evaluator_id="evaluator_id",
        )
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.update(
            evaluator_id="evaluator_id",
            code_evaluator={
                "advanced_features_enabled": True,
                "code": "code",
                "code_evaluator_input": "thread",
                "dependencies": "dependencies",
                "language": "language",
                "managed_code_evaluator_settings": {
                    "foo": {
                        "is_enabled": True,
                        "key_name": "key_name",
                    }
                },
                "require_attachments": True,
                "workspace_secrets_keys": ["string"],
            },
            llm_evaluator={
                "commit_hash_or_tag": "commit_hash_or_tag",
                "num_few_shot_examples": 0,
                "playground_settings_id": "playground_settings_id",
                "prompt_repo_handle": "prompt_repo_handle",
                "use_corrections_dataset": True,
                "variable_mapping": {},
            },
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.update(
            evaluator_id="evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.update(
            evaluator_id="evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(UpdateOnlineEvaluatorResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            await async_client.online_evaluators.with_raw_response.update(
                evaluator_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.list()
        assert_matches_type(AsyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.list(
            agent_id="agent_id",
            feedback_key="feedback_key",
            limit=0,
            metadata="metadata",
            name_contains="name_contains",
            offset=0,
            resource_id=["string"],
            sort_by="sort_by",
            sort_by_desc=True,
            tag_value_id=["string"],
            type="type",
        )
        assert_matches_type(AsyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(AsyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(
                AsyncOffsetPaginationOnlineEvaluators[OnlineEvaluator], online_evaluator, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.delete(
            evaluator_id="evaluator_id",
        )
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.delete(
            evaluator_id="evaluator_id",
            delete_run_rules=True,
        )
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.delete(
            evaluator_id="evaluator_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert online_evaluator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.delete(
            evaluator_id="evaluator_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert online_evaluator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluator_id` but received ''"):
            await async_client.online_evaluators.with_raw_response.delete(
                evaluator_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.bulk_delete(
            evaluator_ids=["string"],
        )
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_delete_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.bulk_delete(
            evaluator_ids=["string"],
            delete_run_rules=True,
        )
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.bulk_delete(
            evaluator_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.bulk_delete(
            evaluator_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(BulkDeleteEvaluatorsResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_spend(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.spend(
            period_start="period_start",
        )
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_spend_with_all_params(self, async_client: AsyncLangsmith) -> None:
        online_evaluator = await async_client.online_evaluators.spend(
            period_start="period_start",
            agent_id="agent_id",
            dataset_id="dataset_id",
            evaluator_id="evaluator_id",
            feedback_key="feedback_key",
            group_by="group_by",
            resource_id=["string"],
            session_id="session_id",
            tag_value_id=["string"],
            type="type",
        )
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_spend(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.online_evaluators.with_raw_response.spend(
            period_start="period_start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        online_evaluator = await response.parse()
        assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_spend(self, async_client: AsyncLangsmith) -> None:
        async with async_client.online_evaluators.with_streaming_response.spend(
            period_start="period_start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            online_evaluator = await response.parse()
            assert_matches_type(GetOnlineEvaluatorSpendResponse, online_evaluator, path=["response"])

        assert cast(Any, response.is_closed) is True
