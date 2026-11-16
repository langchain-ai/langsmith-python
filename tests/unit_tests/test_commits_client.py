"""Exercise Prompt Hub commit requests without a running API server."""

import json

import pytest

from langsmith import AsyncLangsmith, Langsmith
from langsmith._httpx import httpx
from langsmith.types import CommitCreateResponse, CommitRetrieveResponse

COMMITS_PATH = "/api/v1/commits/-/my-prompt"


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
async def test_commits_create(asynchronous):
    manifest = {"lc": 1, "type": "constructor", "id": ["langchain", "prompts", "PromptTemplate"]}

    def handle(request):
        assert request.method == "POST"
        assert request.url.path == COMMITS_PATH
        assert json.loads(request.content) == {"manifest": manifest, "parent_commit": "abc12345"}
        return httpx.Response(201, json={"commit": {"commit_hash": "fed32100", "repo_id": "repo"}})

    result = await _call(
        asynchronous,
        handle,
        lambda client: client.commits.create("my-prompt", owner="-", manifest=manifest, parent_commit="abc12345"),
    )

    assert isinstance(result, CommitCreateResponse)
    assert result.commit.commit_hash == "fed32100"


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_commits_retrieve(asynchronous):
    def handle(request):
        assert request.method == "GET"
        assert request.url.path == f"{COMMITS_PATH}/latest"
        assert request.url.params["include_model"] == "true"
        return httpx.Response(200, json={"commit_hash": "fed32100", "manifest": {"lc": 1}})

    result = await _call(
        asynchronous,
        handle,
        lambda client: client.commits.retrieve("latest", owner="-", repo="my-prompt", include_model=True),
    )

    assert isinstance(result, CommitRetrieveResponse)
    assert result.commit_hash == "fed32100"
    assert result.manifest == {"lc": 1}


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_commits_list_pages_by_offset(asynchronous):
    pages = {
        "0": [{"commit_hash": "c3"}, {"commit_hash": "c2"}],
        "2": [{"commit_hash": "c1"}],
        "3": [],
    }
    offsets = []

    def handle(request):
        assert request.method == "GET"
        assert request.url.path == COMMITS_PATH
        offset = request.url.params.get("offset", "0")
        offsets.append(offset)
        return httpx.Response(200, json={"commits": pages[offset], "total": 3})

    if asynchronous:

        async def collect(client):
            return [commit.commit_hash async for commit in client.commits.list("my-prompt", owner="-")]

    else:

        def collect(client):
            return [commit.commit_hash for commit in client.commits.list("my-prompt", owner="-")]

    hashes = await _call(asynchronous, handle, collect)

    assert hashes == ["c3", "c2", "c1"]
    assert offsets == ["0", "2", "3"]
