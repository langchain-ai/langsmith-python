# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types.workspace_tags.keys import TagValue, ValueListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            description="description",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.workspace_tags.keys.values.with_raw_response.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.workspace_tags.keys.values.with_streaming_response.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.create(
                tag_key_id="",
                value="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.workspace_tags.keys.values.with_raw_response.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.workspace_tags.keys.values.with_streaming_response.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.retrieve(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.retrieve(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            value="x",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.workspace_tags.keys.values.with_raw_response.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.workspace_tags.keys.values.with_streaming_response.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.update(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.update(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ValueListResponse, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.workspace_tags.keys.values.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueListResponse, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.workspace_tags.keys.values.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueListResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        value = client.workspace_tags.keys.values.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert value is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.workspace_tags.keys.values.with_raw_response.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert value is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.workspace_tags.keys.values.with_streaming_response.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert value is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.delete(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            client.workspace_tags.keys.values.with_raw_response.delete(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncValues:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            description="description",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_tags.keys.values.with_raw_response.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_tags.keys.values.with_streaming_response.create(
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.create(
                tag_key_id="",
                value="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_tags.keys.values.with_raw_response.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_tags.keys.values.with_streaming_response.retrieve(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.retrieve(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.retrieve(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            value="x",
        )
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_tags.keys.values.with_raw_response.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(TagValue, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_tags.keys.values.with_streaming_response.update(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(TagValue, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.update(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.update(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ValueListResponse, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_tags.keys.values.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueListResponse, value, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_tags.keys.values.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueListResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        value = await async_client.workspace_tags.keys.values.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert value is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.workspace_tags.keys.values.with_raw_response.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert value is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.workspace_tags.keys.values.with_streaming_response.delete(
            tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert value is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_key_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.delete(
                tag_value_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tag_key_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_value_id` but received ''"):
            await async_client.workspace_tags.keys.values.with_raw_response.delete(
                tag_value_id="",
                tag_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
