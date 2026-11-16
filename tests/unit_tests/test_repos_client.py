"""Exercise Prompt Hub repo and directory requests without a running API server."""

import json

import pytest

from langsmith import AsyncLangsmith, Langsmith
from langsmith._httpx import httpx
from langsmith.types.repos import DirectoryCommitResponse, DirectoryListResponse

DIRECTORIES_PATH = "/api/v1/platform/hub/repos/-/my-agent/directories"


async def _call(asynchronous, handle, call):
    if asynchronous:
        async with AsyncLangsmith(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
        ) as client:
            return await call(client)
    with Langsmith(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handle)),
    ) as client:
        return call(client)


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_directories_list(asynchronous):
    listing = {
        "commit_hash": "abc123",
        "commit_id": "0190f5e0-0000-7000-8000-000000000001",
        "files": {
            "AGENTS.md": {"type": "file", "content": "# Agent"},
            "skills/search": {
                "type": "skill",
                "owner": "-",
                "repo_handle": "search",
                "commit_hash": "def456",
            },
        },
    }

    def handle(request):
        assert request.method == "GET"
        assert request.url.path == DIRECTORIES_PATH
        assert request.url.params["commit"] == "abc123"
        return httpx.Response(200, json=listing)

    result = await _call(
        asynchronous,
        handle,
        lambda client: client.repos.directories.list("my-agent", owner="-", commit="abc123"),
    )

    assert isinstance(result, DirectoryListResponse)
    assert result.commit_hash == "abc123"
    assert result.files["AGENTS.md"].type == "file"
    assert result.files["AGENTS.md"].content == "# Agent"
    assert result.files["skills/search"].type == "skill"
    assert result.files["skills/search"].repo_handle == "search"


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_directories_commit(asynchronous):
    files = {
        "AGENTS.md": {"type": "file", "content": "# Agent v2"},
        "old.md": None,
    }
    commit = {"id": "0190f5e0-0000-7000-8000-000000000002", "commit_hash": "fed321"}

    def handle(request):
        assert request.method == "POST"
        assert request.url.path == f"{DIRECTORIES_PATH}/commits"
        assert json.loads(request.content) == {"files": files, "parent_commit": "abc123"}
        return httpx.Response(201, json={"commit": commit})

    result = await _call(
        asynchronous,
        handle,
        lambda client: client.repos.directories.commit("my-agent", owner="-", files=files, parent_commit="abc123"),
    )

    assert isinstance(result, DirectoryCommitResponse)
    assert result.commit is not None
    assert result.commit.commit_hash == "fed321"


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_repos_list_pages_by_offset(asynchronous):
    pages = {
        "0": [{"repo_handle": "first"}, {"repo_handle": "second"}],
        "2": [{"repo_handle": "third"}],
        "3": [],
    }
    offsets = []

    def handle(request):
        assert request.method == "GET"
        assert request.url.path == "/api/v1/repos"
        offset = request.url.params.get("offset", "0")
        offsets.append(offset)
        return httpx.Response(200, json={"repos": pages[offset], "total": 3})

    if asynchronous:

        async def collect(client):
            return [repo.repo_handle async for repo in client.repos.list()]

    else:

        def collect(client):
            return [repo.repo_handle for repo in client.repos.list()]

    handles = await _call(asynchronous, handle, collect)

    assert handles == ["first", "second", "third"]
    assert offsets == ["0", "2", "3"]
