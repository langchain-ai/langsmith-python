# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from langsmith import Langsmith, AsyncLangsmith
from tests.utils import assert_matches_type
from langsmith.types import (
    SandboxResponse,
    SnapshotResponse,
    ServiceURLResponse,
    DownloadURLResponse,
    SandboxStatusResponse,
)
from langsmith.pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from langsmith.types.sandboxes import (
    BoxListServiceURLsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBoxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create(
            access_delegation={
                "mode": "INHERIT",
                "permissions": ["string"],
            },
            cpu_millicores=0,
            delete_after_stop_seconds=0,
            env_vars={"foo": "string"},
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            labels={"foo": "string"},
            mem_bytes=0,
            mount_config={
                "auth": {
                    "aws": {
                        "role_arn": "x",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                    "azure": {
                        "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                        "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                    "gcp": {
                        "workload_identity_provider": "x",
                        "service_account_email": "service_account_email",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                },
                "mounts": [
                    {
                        "id": "id",
                        "mount_path": "mount_path",
                        "s3": {
                            "bucket": "bucket",
                            "region": "region",
                            "endpoint_url": "endpoint_url",
                            "path_style": True,
                            "prefix": "prefix",
                        },
                        "type": "s3",
                        "azure_blob": {
                            "container": "container",
                            "storage_account": "26f1klzn5713",
                            "prefix": "prefix",
                        },
                        "cache": {
                            "max_size_bytes": 0,
                            "writeback_seconds": 0,
                        },
                        "contexthub": {
                            "repo": "repo",
                            "initial_pull_only": True,
                        },
                        "encryption": {"kms_key": "kms_key"},
                        "gcs": {
                            "bucket": "bucket",
                            "prefix": "prefix",
                        },
                        "git": {
                            "remote_url": "remote_url",
                            "ref": {
                                "name": "name",
                                "type": "branch",
                            },
                            "refresh_interval_seconds": 1,
                        },
                        "read_only": True,
                    }
                ],
            },
            name="name",
            persistent=True,
            preserve_memory_on_stop=True,
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "description": "description",
                "no_proxy": ["string"],
                "rules": [
                    {
                        "name": "name",
                        "aws": {
                            "role_arn": "x",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "azure": {
                            "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "resources": ["https://storage.azure.com"],
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "description": "description",
                        "enabled": True,
                        "env_vars": {"foo": "string"},
                        "gcp": {
                            "workload_identity_provider": "x",
                            "scopes": ["string"],
                            "service_account_email": "service_account_email",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_headers": ["string"],
                        "match_hosts": ["string"],
                        "match_paths": ["string"],
                        "relay_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "type": "type",
                    }
                ],
            },
            restore_memory=True,
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            snapshot="snapshot",
            snapshot_id="snapshot_id",
            snapshot_name="snapshot_name",
            tag_value_ids=["string"],
            vcpus=0,
            volumes=[
                {
                    "mount_path": "mount_path",
                    "volume": "volume",
                    "read_only": True,
                }
            ],
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.retrieve(
            "name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.update(
            path_name="name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.update(
            path_name="name",
            cpu_millicores=0,
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            body_name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "description": "description",
                "no_proxy": ["string"],
                "rules": [
                    {
                        "name": "name",
                        "aws": {
                            "role_arn": "x",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "azure": {
                            "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "resources": ["https://storage.azure.com"],
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "description": "description",
                        "enabled": True,
                        "env_vars": {"foo": "string"},
                        "gcp": {
                            "workload_identity_provider": "x",
                            "scopes": ["string"],
                            "service_account_email": "service_account_email",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_headers": ["string"],
                        "match_hosts": ["string"],
                        "match_paths": ["string"],
                        "relay_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "type": "type",
                    }
                ],
            },
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.update(
            path_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.update(
            path_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.sandboxes.boxes.with_raw_response.update(
                path_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list()
        assert_matches_type(SyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list(
            created_by="created_by",
            cursor="cursor",
            label=["string"],
            limit=0,
            name_contains="name_contains",
            offset=0,
            page_size=0,
            sort_by="sort_by",
            sort_direction="sort_direction",
            sort_order="sort_order",
            status="status",
            tag_value_id=["string"],
        )
        assert_matches_type(SyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.delete(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_snapshot(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
        )
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_snapshot_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
            checkpoint="checkpoint",
            confirm_allow_snapshot_secret_values=True,
            description="description",
            docker_image="docker_image",
            fs_capacity_bytes=0,
            image_config={
                "cmd": ["string"],
                "entrypoint": ["string"],
                "exposed_ports": [0],
            },
            include=["all"],
            include_memory=True,
            labels={"foo": "string"},
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            tag="tag",
        )
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_snapshot(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.create_snapshot(
            path_name="name",
            body_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_snapshot(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.create_snapshot(
            path_name="name",
            body_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SnapshotResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_snapshot(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.sandboxes.boxes.with_raw_response.create_snapshot(
                path_name="",
                body_name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_service_url(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.delete_service_url(
            name="name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_service_url_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.delete_service_url(
            name="name",
            port=0,
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_service_url(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.delete_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_service_url(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.delete_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_service_url(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.delete_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_download_url(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_download_url(
            name="name",
            path="path",
        )
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_download_url_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_download_url(
            name="name",
            path="path",
            content_disposition="content_disposition",
            content_type="content_type",
            csp_sandbox=True,
            csp_sandbox_flags=["allow-downloads"],
            csp_source_bundles=["cdnjs"],
            expires_in_seconds=0,
        )
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_download_url(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.generate_download_url(
            name="name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_download_url(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.generate_download_url(
            name="name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(DownloadURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_download_url(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.generate_download_url(
                name="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_service_url(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_service_url(
            name="name",
        )
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_service_url_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_service_url(
            name="name",
            access="restricted",
            embed_origins=["string"],
            expires_in_seconds=0,
            port=0,
        )
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_service_url(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.generate_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_service_url(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.generate_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(ServiceURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_service_url(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.generate_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.get_status(
            "name",
        )
        assert_matches_type(SandboxStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.get_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SandboxStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.get_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SandboxStatusResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_service_urls(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list_service_urls(
            name="name",
        )
        assert_matches_type(SyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_service_urls_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list_service_urls(
            name="name",
            cursor="cursor",
            page_size=0,
        )
        assert_matches_type(SyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_service_urls(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.list_service_urls(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_service_urls(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.list_service_urls(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_service_urls(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.list_service_urls(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.start(
            "name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.start(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.start(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.stop(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Langsmith) -> None:

        response = client.sandboxes.boxes.with_raw_response.stop(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.stop(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.stop(
                "",
            )


class TestAsyncBoxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create(
            access_delegation={
                "mode": "INHERIT",
                "permissions": ["string"],
            },
            cpu_millicores=0,
            delete_after_stop_seconds=0,
            env_vars={"foo": "string"},
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            labels={"foo": "string"},
            mem_bytes=0,
            mount_config={
                "auth": {
                    "aws": {
                        "role_arn": "x",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                    "azure": {
                        "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                        "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                    "gcp": {
                        "workload_identity_provider": "x",
                        "service_account_email": "service_account_email",
                        "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                    },
                },
                "mounts": [
                    {
                        "id": "id",
                        "mount_path": "mount_path",
                        "s3": {
                            "bucket": "bucket",
                            "region": "region",
                            "endpoint_url": "endpoint_url",
                            "path_style": True,
                            "prefix": "prefix",
                        },
                        "type": "s3",
                        "azure_blob": {
                            "container": "container",
                            "storage_account": "26f1klzn5713",
                            "prefix": "prefix",
                        },
                        "cache": {
                            "max_size_bytes": 0,
                            "writeback_seconds": 0,
                        },
                        "contexthub": {
                            "repo": "repo",
                            "initial_pull_only": True,
                        },
                        "encryption": {"kms_key": "kms_key"},
                        "gcs": {
                            "bucket": "bucket",
                            "prefix": "prefix",
                        },
                        "git": {
                            "remote_url": "remote_url",
                            "ref": {
                                "name": "name",
                                "type": "branch",
                            },
                            "refresh_interval_seconds": 1,
                        },
                        "read_only": True,
                    }
                ],
            },
            name="name",
            persistent=True,
            preserve_memory_on_stop=True,
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "description": "description",
                "no_proxy": ["string"],
                "rules": [
                    {
                        "name": "name",
                        "aws": {
                            "role_arn": "x",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "azure": {
                            "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "resources": ["https://storage.azure.com"],
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "description": "description",
                        "enabled": True,
                        "env_vars": {"foo": "string"},
                        "gcp": {
                            "workload_identity_provider": "x",
                            "scopes": ["string"],
                            "service_account_email": "service_account_email",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_headers": ["string"],
                        "match_hosts": ["string"],
                        "match_paths": ["string"],
                        "relay_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "type": "type",
                    }
                ],
            },
            restore_memory=True,
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            snapshot="snapshot",
            snapshot_id="snapshot_id",
            snapshot_name="snapshot_name",
            tag_value_ids=["string"],
            vcpus=0,
            volumes=[
                {
                    "mount_path": "mount_path",
                    "volume": "volume",
                    "read_only": True,
                }
            ],
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.retrieve(
            "name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.update(
            path_name="name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.update(
            path_name="name",
            cpu_millicores=0,
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            body_name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "description": "description",
                "no_proxy": ["string"],
                "rules": [
                    {
                        "name": "name",
                        "aws": {
                            "role_arn": "x",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "azure": {
                            "client_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "tenant_id": "E1CB97d8-Ddf3-aAae-0Afa-1A3C33cFaADc",
                            "resources": ["https://storage.azure.com"],
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "description": "description",
                        "enabled": True,
                        "env_vars": {"foo": "string"},
                        "gcp": {
                            "workload_identity_provider": "x",
                            "scopes": ["string"],
                            "service_account_email": "service_account_email",
                            "subject_scope": "tag:2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_headers": ["string"],
                        "match_hosts": ["string"],
                        "match_paths": ["string"],
                        "relay_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "type": "type",
                    }
                ],
            },
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.update(
            path_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.update(
            path_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.update(
                path_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list()
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list(
            created_by="created_by",
            cursor="cursor",
            label=["string"],
            limit=0,
            name_contains="name_contains",
            offset=0,
            page_size=0,
            sort_by="sort_by",
            sort_direction="sort_direction",
            sort_order="sort_order",
            status="status",
            tag_value_id=["string"],
        )
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[SandboxResponse], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.delete(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
        )
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_snapshot_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
            checkpoint="checkpoint",
            confirm_allow_snapshot_secret_values=True,
            description="description",
            docker_image="docker_image",
            fs_capacity_bytes=0,
            image_config={
                "cmd": ["string"],
                "entrypoint": ["string"],
                "exposed_ports": [0],
            },
            include=["all"],
            include_memory=True,
            labels={"foo": "string"},
            run_config={
                "env_vars": {"foo": "string"},
                "user": "user",
                "work_dir": "work_dir",
            },
            tag="tag",
        )
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_snapshot(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.create_snapshot(
            path_name="name",
            body_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.create_snapshot(
            path_name="name",
            body_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SnapshotResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.create_snapshot(
                path_name="",
                body_name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_service_url(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.delete_service_url(
            name="name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_service_url_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.delete_service_url(
            name="name",
            port=0,
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_service_url(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.delete_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_service_url(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.delete_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_service_url(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.delete_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_download_url(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_download_url(
            name="name",
            path="path",
        )
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_download_url_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_download_url(
            name="name",
            path="path",
            content_disposition="content_disposition",
            content_type="content_type",
            csp_sandbox=True,
            csp_sandbox_flags=["allow-downloads"],
            csp_source_bundles=["cdnjs"],
            expires_in_seconds=0,
        )
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_download_url(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.generate_download_url(
            name="name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(DownloadURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_download_url(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.generate_download_url(
            name="name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(DownloadURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_download_url(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.generate_download_url(
                name="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_service_url(
            name="name",
        )
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_service_url_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_service_url(
            name="name",
            access="restricted",
            embed_origins=["string"],
            expires_in_seconds=0,
            port=0,
        )
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_service_url(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.generate_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(ServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.generate_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(ServiceURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.generate_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.get_status(
            "name",
        )
        assert_matches_type(SandboxStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.get_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SandboxStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.get_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SandboxStatusResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_service_urls(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list_service_urls(
            name="name",
        )
        assert_matches_type(AsyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_service_urls_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list_service_urls(
            name="name",
            cursor="cursor",
            page_size=0,
        )
        assert_matches_type(AsyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_service_urls(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.list_service_urls(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(AsyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_service_urls(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.list_service_urls(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(AsyncItemsCursorGetPagination[BoxListServiceURLsResponse], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_service_urls(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.list_service_urls(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.start(
            "name",
        )
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.start(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(SandboxResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.start(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(SandboxResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.stop(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncLangsmith) -> None:

        response = await async_client.sandboxes.boxes.with_raw_response.stop(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.stop(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.stop(
                "",
            )
