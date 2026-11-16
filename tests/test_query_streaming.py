from __future__ import annotations

import json
from typing import Any, Dict, List, Callable

import httpx
import pytest
import pydantic
from respx import MockRouter

from langsmith import Langsmith, APIStatusError, AsyncLangsmith

base_url = "http://127.0.0.1:4010"


def data(patches: str) -> str:
    return f"event: data\ndata: {patches}\n\n"


END = "event: end\ndata: \n\n"


def serve(respx_mock: MockRouter, resource: str, pages: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    """Serves /api/v2/<resource>/query from `pages`, keyed by the request's cursor."""
    bodies: List[Dict[str, Any]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["accept"] == "text/event-stream"
        body = json.loads(request.content)
        bodies.append(body)
        events = pages.get(body.get("cursor", ""))
        if events is None:
            return httpx.Response(406, json={"detail": "no such page"})
        return httpx.Response(200, headers={"content-type": "text/event-stream"}, content="".join(events))

    respx_mock.post(f"{base_url}/api/v2/{resource}/query").mock(side_effect=handler)
    return bodies


def methods(client: Langsmith) -> Dict[str, Callable[..., Any]]:
    return {
        "runs": client.runs.streaming.query_v2_items,
        "threads": client.threads.streaming.query_items,
        "traces": client.traces.streaming.query_items,
    }


async def collect_async(client: AsyncLangsmith, resource: str, out: List[Any], **params: Any) -> None:
    method = {
        "runs": client.runs.streaming.query_v2_items,
        "threads": client.threads.streaming.query_items,
        "traces": client.traces.streaming.query_items,
    }[resource]
    async for item in method(**params):
        out.append(item)


@pytest.fixture(params=["sync", "async"])
def collect(request: pytest.FixtureRequest) -> Callable[..., List[Any]]:
    """Drains a query_items helper into `out` (filled even when it raises)."""

    def run(resource: str, out: List[Any], **params: Any) -> List[Any]:
        if request.param == "sync":
            client = Langsmith(base_url=base_url, api_key="key", tenant_id="tenant", max_retries=0)
            for item in methods(client)[resource](**params):
                out.append(item)
        else:
            import asyncio

            aclient = AsyncLangsmith(base_url=base_url, api_key="key", tenant_id="tenant", max_retries=0)
            asyncio.run(collect_async(aclient, resource, out, **params))
        return out

    return run


@pytest.mark.respx(base_url=base_url)
def test_follows_cursor(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    bodies = serve(
        respx_mock,
        "runs",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"run-1","name":"a"}],"next_cursor":null}}]'),
                data(
                    '[{"op":"add","path":"/items/-","value":{"id":"run-2","name":"b"}},{"op":"add","path":"/items/0/extra","value":1}]'
                ),
                data(
                    '[{"op":"add","path":"/items/-","value":{"id":"run-3","name":"c"}},{"op":"replace","path":"/next_cursor","value":"abc"}]'
                ),
                END,
            ],
            "abc": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"run-4","name":"d"}],"next_cursor":null}}]'),
                data('[{"op":"replace","path":"/next_cursor","value":null}]'),
                END,
            ],
        },
    )
    got = collect("runs", [], ai_search="question about langchain")
    assert [f"{r.id}:{r.name}" for r in got] == ["run-1:a", "run-2:b", "run-3:c", "run-4:d"]
    assert len(bodies) == 2
    assert "cursor" not in bodies[0]
    assert bodies[1] == {"cursor": "abc", "ai_search": "question about langchain"}


@pytest.mark.respx(base_url=base_url)
def test_indexed_inserts_and_empty_cursor(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    bodies = serve(
        respx_mock,
        "runs",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[],"next_cursor":null}}]'),
                data(
                    '[{"op":"add","path":"/items/0","value":{"id":"run-1"}},{"op":"add","path":"/items/0","value":{"id":"run-2"}}]'
                ),
                data(
                    '[{"op":"add","path":"/items/1/extra","value":{}},{"op":"replace","path":"/next_cursor","value":""}]'
                ),
                END,
            ]
        },
    )
    assert [r.id for r in collect("runs", [])] == ["run-2", "run-1"]
    assert len(bodies) == 1


@pytest.mark.respx(base_url=base_url)
def test_traces(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    serve(
        respx_mock,
        "traces",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"root_run":{"id":"run-1"}}],"next_cursor":null}}]'),
                data(
                    '[{"op":"add","path":"/items/-","value":{"root_run":{"id":"run-2"}}},{"op":"add","path":"/items/0/trace_aggregates","value":{"total_tokens":3}}]'
                ),
                END,
            ]
        },
    )
    assert [t.root_run.id for t in collect("traces", [])] == ["run-1", "run-2"]


@pytest.mark.respx(base_url=base_url)
def test_empty_page(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    bodies = serve(
        respx_mock, "threads", {"": [data('[{"op":"add","path":"","value":{"items":[],"next_cursor":null}}]'), END]}
    )
    assert collect("threads", []) == []
    assert len(bodies) == 1


@pytest.mark.respx(base_url=base_url)
def test_error_event_after_item(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    serve(
        respx_mock,
        "runs",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"run-1"}],"next_cursor":null}}]'),
                'event: error\ndata: {"detail":"boom"}\n\n',
            ]
        },
    )
    got: List[Any] = []
    with pytest.raises(APIStatusError):
        collect("runs", got)
    assert [r.id for r in got] == ["run-1"]


@pytest.mark.respx(base_url=base_url)
def test_http_error(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    serve(respx_mock, "runs", {})
    with pytest.raises(APIStatusError) as exc:
        collect("runs", [], cursor="missing")
    assert exc.value.status_code == 406


@pytest.mark.respx(base_url=base_url)
def test_decode_error_yields_earlier_items(respx_mock: MockRouter, collect: Callable[..., List[Any]]) -> None:
    serve(
        respx_mock,
        "runs",
        {"": [data('[{"op":"add","path":"","value":{"items":[{"id":"run-1"},"not-a-run"],"next_cursor":null}}]'), END]},
    )
    got: List[Any] = []
    with pytest.raises(pydantic.ValidationError):
        collect("runs", got)
    assert [r.id for r in got] == ["run-1"]


@pytest.mark.respx(base_url=base_url)
def test_early_break_stops_paging(respx_mock: MockRouter) -> None:
    bodies = serve(
        respx_mock,
        "runs",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"run-1"},{"id":"run-2"}],"next_cursor":"abc"}}]'),
                END,
            ],
            "abc": [data('[{"op":"add","path":"","value":{"items":[{"id":"run-3"}],"next_cursor":null}}]'), END],
        },
    )
    client = Langsmith(base_url=base_url, api_key="key", tenant_id="tenant", max_retries=0)
    for run in client.runs.streaming.query_v2_items():
        assert run.id == "run-1"
        break
    assert len(bodies) == 1


@pytest.mark.respx(base_url=base_url)
async def test_early_break_stops_paging_async(respx_mock: MockRouter) -> None:
    bodies = serve(
        respx_mock,
        "runs",
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"run-1"},{"id":"run-2"}],"next_cursor":"abc"}}]'),
                END,
            ],
            "abc": [data('[{"op":"add","path":"","value":{"items":[{"id":"run-3"}],"next_cursor":null}}]'), END],
        },
    )
    client = AsyncLangsmith(base_url=base_url, api_key="key", tenant_id="tenant", max_retries=0)
    async for run in client.runs.streaming.query_v2_items():
        assert run.id == "run-1"
        break
    assert len(bodies) == 1
