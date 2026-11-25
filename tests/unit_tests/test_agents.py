"""The handwritten clients expose workspace-scoped registry agents."""

import json
from inspect import isawaitable
from typing import Literal
from unittest import mock

import pytest

from langsmith import AsyncClient, Client, ConflictError
from langsmith._httpx import httpx
from langsmith._internal import _profiles
from langsmith.schemas import LangSmithInfo


@pytest.mark.asyncio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("source_type", [None, "EXTERNAL", "LSD", "MDA", "FLEET"])
async def test_agents_create_uses_client_configuration(
    async_client: bool, source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"] | None
) -> None:
    requests = []
    expected_source_type = "EXTERNAL" if source_type is None else source_type

    def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(201, json={"id": "example-agent", "source_type": expected_source_type}, request=request)

    async def arespond(request, **kwargs):
        return respond(request, **kwargs)

    with (
        mock.patch.object(httpx.Client, "send", side_effect=respond),
        mock.patch.object(httpx.AsyncClient, "send", side_effect=arespond),
    ):
        client = (
            AsyncClient(
                api_url="http://localhost:8080/api/v1",
                api_key="test-api-key",
                workspace_id="test-workspace",
            )
            if async_client
            else Client(
                api_url="http://localhost:8080/api/v1",
                api_key="test-api-key",
                workspace_id="test-workspace",
                info=LangSmithInfo(),
            )
        )
        if source_type is None:
            result = client.agents.create(id="example-agent")
        else:
            result = client.agents.create(id="example-agent", source_type=source_type)
        agent = await result if isawaitable(result) else result

    assert agent.id == "example-agent"
    assert agent.source_type == expected_source_type
    assert len(requests) == 1
    request = requests[0]
    assert str(request.url) == "http://localhost:8080/api/v1/agents"
    assert request.headers["x-api-key"] == "test-api-key"
    assert request.headers["x-tenant-id"] == "test-workspace"
    assert json.loads(request.content) == {"id": "example-agent", "source_type": expected_source_type}


@pytest.mark.asyncio
async def test_async_agents_preserves_conflict() -> None:
    requests = []

    async def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(409, json={"detail": "Agent already exists"}, request=request)

    with mock.patch.object(httpx.AsyncClient, "send", side_effect=respond):
        client = AsyncClient(
            api_url="http://localhost:8080/api/v1",
            api_key="test-api-key",
            workspace_id="test-workspace",
        )
        client._langsmith_api.max_retries = 0
        with pytest.raises(ConflictError):
            await client.agents.create(id="example-agent")

    assert len(requests) == 1
    assert json.loads(requests[0].content) == {"id": "example-agent", "source_type": "EXTERNAL"}
    assert str(requests[0].url) == "http://localhost:8080/api/v1/agents"
    assert requests[0].headers["x-tenant-id"] == "test-workspace"
    assert requests[0].headers["x-api-key"] == "test-api-key"


@pytest.mark.asyncio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("copy_method", [None, "copy", "with_options"])
async def test_saved_agents_use_current_credentials_and_workspace(async_client: bool, copy_method: str | None) -> None:
    requests = []

    def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(200, json={"id": "example-agent", "source_type": "EXTERNAL"}, request=request)

    async def arespond(request, **kwargs):
        return respond(request, **kwargs)

    transport = httpx.AsyncClient if async_client else httpx.Client
    with mock.patch.object(transport, "send", side_effect=arespond if async_client else respond):
        client = (AsyncClient if async_client else Client)(
            api_url="http://localhost:8080",
            api_key="old-key",
            workspace_id="old-workspace",
            headers={"X-Custom": "old-value", "X-Removed": "old-value"},
            **({} if async_client else {"auto_batch_tracing": False}),
        )
        agents = client.agents
        if copy_method:
            generated = client._langsmith_api if async_client else client._get_langsmith_api_sync()
            agents = getattr(generated, copy_method)(timeout=2, max_retries=0).agents

        async def retrieve():
            result = agents.retrieve("example-agent", extra_headers={"X-Request": "per-request"})
            if isawaitable(result):
                await result

        await retrieve()
        client.api_key = "new-key"
        client.workspace_id = "new-workspace"
        client.headers["X-Custom"] = "new-value"
        del client.headers["X-Removed"]
        await retrieve()
        client.api_key = None
        client.workspace_id = None
        client.headers = {"Authorization": "Bearer replacement-token"}
        await retrieve()

    assert requests[0].headers["x-api-key"] == "old-key"
    assert requests[0].headers["x-tenant-id"] == "old-workspace"
    assert requests[1].headers["x-api-key"] == "new-key"
    assert requests[1].headers["x-tenant-id"] == "new-workspace"
    assert requests[1].headers["x-custom"] == "new-value"
    assert "x-removed" not in requests[1].headers
    assert requests[2].headers["authorization"] == "Bearer replacement-token"
    for name in ("x-api-key", "x-tenant-id", "x-custom", "x-removed"):
        assert name not in requests[2].headers
    assert all(request.headers["x-request"] == "per-request" for request in requests)
    for request in requests:
        assert request.headers["user-agent"].startswith("langsmith-py/")
        assert all(len(request.headers.get_list(name)) == 1 for name in request.headers)


@pytest.mark.asyncio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("copy_headers", [None, {}, {"authorization": "Bearer scoped-token"}])
async def test_saved_agents_refresh_profile_credentials(
    async_client: bool, copy_headers: dict[str, str] | None, monkeypatch: pytest.MonkeyPatch
) -> None:
    for prefix in ("LANGCHAIN", "LANGSMITH"):
        for suffix in ("API_KEY", "WORKSPACE_ID"):
            monkeypatch.delenv(f"{prefix}_{suffix}", raising=False)
    requests = []

    def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(200, json={"id": "example-agent", "source_type": "EXTERNAL"}, request=request)

    async def arespond(request, **kwargs):
        return respond(request, **kwargs)

    profile = mock.Mock(spec=_profiles.ProfileAuth)
    profile.oauth_access_token = "old-token"
    profile.current_auth_headers.return_value = {"Authorization": "Bearer old-token"}
    profile.needs_refresh.return_value = True
    profile.get_auth_headers.side_effect = [
        {"Authorization": "Bearer old-token"},
        {"Authorization": "Bearer refreshed-token"},
    ]
    transport = httpx.AsyncClient if async_client else httpx.Client
    with (
        mock.patch.object(transport, "send", side_effect=arespond if async_client else respond),
        mock.patch.object(
            _profiles,
            "load_profile_client_config",
            return_value=_profiles.ProfileClientConfig(oauth_access_token="old-token"),
        ),
        mock.patch.object(_profiles, "ProfileAuth", return_value=profile),
    ):
        client = (AsyncClient if async_client else Client)(
            api_url="http://localhost:8080",
            **({} if async_client else {"auto_batch_tracing": False}),
        )
        agents = client.agents
        if copy_headers is not None:
            generated = client._langsmith_api if async_client else client._get_langsmith_api_sync()
            agents = generated.with_options(set_default_headers=copy_headers).copy(timeout=2).agents
        for _ in range(2):
            result = agents.retrieve("example-agent")
            if isawaitable(result):
                await result

    expected_tokens = ["Bearer scoped-token"] * 2 if copy_headers else ["Bearer old-token", "Bearer refreshed-token"]
    assert [request.headers.get_list("authorization") for request in requests] == [[token] for token in expected_tokens]
    assert all("x-api-key" not in request.headers for request in requests)


@pytest.mark.asyncio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("replace_headers", [False, True])
async def test_agents_option_copies_preserve_overrides(async_client: bool, replace_headers: bool) -> None:
    requests = []

    def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(200, json={"id": "example-agent"}, request=request)

    async def arespond(request, **kwargs):
        return respond(request, **kwargs)

    transport = httpx.AsyncClient if async_client else httpx.Client
    with mock.patch.object(transport, "send", side_effect=arespond if async_client else respond):
        client = (AsyncClient if async_client else Client)(
            api_url="http://localhost:8080",
            api_key="original-key",
            workspace_id="original-workspace",
            headers={"X-Original": "original", "X-Region": "east"},
            **({} if async_client else {"auto_batch_tracing": False}),
        )
        generated = client._langsmith_api if async_client else client._get_langsmith_api_sync()
        scoped = generated.with_options(
            api_key="scoped-key",
            tenant_id="scoped-workspace",
            timeout=2,
            **{
                "set_default_headers" if replace_headers else "default_headers": {
                    "X-Scoped": "scoped",
                    "x-region": "west",
                    "x-api-key": "header-key",
                    "user-agent": "scoped-client",
                    "ACCEPT": "application/json; charset=utf-8",
                    "content-type": "application/json; charset=utf-8",
                    "x-stainless-os": "scoped-os",
                }
            },
        ).copy(max_retries=0)
        client.api_key = "refreshed-key"
        client.workspace_id = "refreshed-workspace"
        for agents in (scoped.agents, client.agents):
            result = agents.update("example-agent", name="Updated agent")
            if isawaitable(result):
                await result

    assert requests[0].headers.get_list("x-api-key") == ["header-key"]
    assert requests[0].headers.get_list("x-region") == ["west"]
    assert requests[0].headers.get_list("user-agent") == ["scoped-client"]
    assert requests[0].headers.get_list("accept") == ["application/json; charset=utf-8"]
    assert requests[0].headers.get_list("content-type") == ["application/json; charset=utf-8"]
    assert requests[0].headers.get_list("x-stainless-os") == ["scoped-os"]
    assert all(len(requests[0].headers.get_list(name)) == 1 for name in requests[0].headers)
    assert requests[0].headers["x-tenant-id"] == "scoped-workspace"
    assert requests[0].headers["x-scoped"] == "scoped"
    assert ("x-original" in requests[0].headers) is not replace_headers
    assert requests[0].extensions["timeout"]["read"] == 2
    assert requests[1].headers["x-api-key"] == "refreshed-key"
    assert requests[1].headers["x-tenant-id"] == "refreshed-workspace"
    assert "x-scoped" not in requests[1].headers


@pytest.mark.asyncio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("header_name", ["authorization", "AUTHORIZATION", "Authorization"])
async def test_agents_accept_case_insensitive_bearer_headers(async_client: bool, header_name: str) -> None:
    requests = []

    def respond(request, **kwargs):
        requests.append(request)
        return httpx.Response(200, json={"id": "example-agent"}, request=request)

    async def arespond(request, **kwargs):
        return respond(request, **kwargs)

    transport = httpx.AsyncClient if async_client else httpx.Client
    with mock.patch.object(transport, "send", side_effect=arespond if async_client else respond):
        client = (AsyncClient if async_client else Client)(
            api_url="http://localhost:8080",
            api_key="initial-key",
            **({} if async_client else {"auto_batch_tracing": False}),
        )
        client.api_key = None
        client.workspace_id = None
        client.headers = {}
        result = client.agents.retrieve("example-agent", extra_headers={header_name: "Bearer per-request-token"})
        if isawaitable(result):
            await result
        with pytest.raises(TypeError, match="Could not resolve authentication method"):
            result = client.agents.retrieve("example-agent", extra_headers={header_name: ""})
            if isawaitable(result):
                await result

    assert len(requests) == 1
    assert requests[0].headers["authorization"] == "Bearer per-request-token"
    assert "x-api-key" not in requests[0].headers
