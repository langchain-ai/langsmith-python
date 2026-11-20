# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from langsmith.types.sandboxes import (
    VolumeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.create(
            name="name",
            size_bytes=0,
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.create(
            name="name",
            size_bytes=0,
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.create(
            name="name",
            size_bytes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.create(
            name="name",
            size_bytes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.retrieve(
            "volume",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.retrieve(
            "volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.retrieve(
            "volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            client.sandboxes.volumes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.update(
            volume="volume",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.update(
            volume="volume",
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.update(
            volume="volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.update(
            volume="volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            client.sandboxes.volumes.with_raw_response.update(
                volume="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.list()
        assert_matches_type(SyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.list(
            cursor="cursor",
            name_contains="name_contains",
            page_size=0,
        )
        assert_matches_type(SyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.delete(
            "volume",
        )
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.delete(
            "volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.delete(
            "volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            client.sandboxes.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.clone(
            volume="volume",
            name="name",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Langsmith) -> None:
        volume = client.sandboxes.volumes.clone(
            volume="volume",
            name="name",
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Langsmith) -> None:

        response = client.sandboxes.volumes.with_raw_response.clone(
            volume="volume",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Langsmith) -> None:
        with client.sandboxes.volumes.with_streaming_response.clone(
            volume="volume",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            client.sandboxes.volumes.with_raw_response.clone(
                volume="",
                name="name",
            )


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.create(
            name="name",
            size_bytes=0,
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.create(
            name="name",
            size_bytes=0,
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.create(
            name="name",
            size_bytes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.create(
            name="name",
            size_bytes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.retrieve(
            "volume",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.retrieve(
            "volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.retrieve(
            "volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            await async_client.sandboxes.volumes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.update(
            volume="volume",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.update(
            volume="volume",
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.update(
            volume="volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.update(
            volume="volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            await async_client.sandboxes.volumes.with_raw_response.update(
                volume="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.list()
        assert_matches_type(AsyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.list(
            cursor="cursor",
            name_contains="name_contains",
            page_size=0,
        )
        assert_matches_type(AsyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[VolumeResponse], volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.delete(
            "volume",
        )
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.delete(
            "volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.delete(
            "volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            await async_client.sandboxes.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.clone(
            volume="volume",
            name="name",
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncLangsmith) -> None:
        volume = await async_client.sandboxes.volumes.clone(
            volume="volume",
            name="name",
            description="description",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.volumes.with_raw_response.clone(
            volume="volume",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.volumes.with_streaming_response.clone(
            volume="volume",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume` but received ''"):
            await async_client.sandboxes.volumes.with_raw_response.clone(
                volume="",
                name="name",
            )
