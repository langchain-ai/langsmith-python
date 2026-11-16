from __future__ import annotations

import json
import asyncio
from typing import Any, Dict, List, Callable, Iterator, AsyncIterator
from typing_extensions import override

import httpx
import pytest

from langsmith import Langsmith, AsyncLangsmith

base_url = "http://127.0.0.1:4010"


@pytest.fixture(autouse=True)
def vcr_fixture() -> Iterator[None]:
    """Overrides the global VCR fixture: it buffers whole response bodies, which hides when items are yielded."""
    yield


def data(patches: str) -> str:
    return f"event: data\ndata: {patches}\n\n"


END = "event: end\ndata: \n\n"


class Probe(httpx.SyncByteStream, httpx.AsyncByteStream):
    """Streams one chunk per event and runs `checks[i]` right before chunk i is produced."""

    def __init__(self, events: List[str], checks: Dict[int, Callable[[], None]]) -> None:
        self.events = events
        self.checks = checks

    @override
    def __iter__(self) -> Iterator[bytes]:
        for i, event in enumerate(self.events):
            if i in self.checks:
                self.checks[i]()
            yield event.encode()

    @override
    async def __aiter__(self) -> AsyncIterator[bytes]:
        for i, event in enumerate(self.events):
            if i in self.checks:
                self.checks[i]()
            yield event.encode()


_handler: Callable[[httpx.Request], httpx.Response] | None = None


def serve(
    pages: Dict[str, List[str]],
    checks: Dict[str, Dict[int, Callable[[], None]]] | None = None,
    on_request: Callable[[str], None] | None = None,
) -> None:
    global _handler

    def handler(request: httpx.Request) -> httpx.Response:
        cursor = json.loads(request.content).get("cursor", "")
        if on_request:
            on_request(cursor)
        return httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            stream=Probe(pages[cursor], (checks or {}).get(cursor, {})),
        )

    _handler = handler


@pytest.fixture(params=["sync", "async"])
def collect(request: pytest.FixtureRequest) -> Callable[[List[Any]], None]:
    def run(out: List[Any]) -> None:
        if request.param == "sync":
            client = Langsmith(
                base_url=base_url,
                api_key="key",
                tenant_id="tenant",
                max_retries=0,
                http_client=httpx.Client(transport=httpx.MockTransport(lambda r: _handler(r))),  # type: ignore
            )
            for item in client.runs.streaming.query_v2_items():
                out.append(item)
        else:
            aclient = AsyncLangsmith(
                base_url=base_url,
                api_key="key",
                tenant_id="tenant",
                max_retries=0,
                http_client=httpx.AsyncClient(transport=httpx.MockTransport(lambda r: _handler(r))),  # type: ignore
            )

            async def go() -> None:
                async for item in aclient.runs.streaming.query_v2_items():
                    out.append(item)

            asyncio.run(go())

    return run


def ids(out: List[Any]) -> List[str]:
    return [r.id for r in out]


def test_appends_are_yielded_before_the_stream_ends(collect: Callable[[List[Any]], None]) -> None:
    out: List[Any] = []
    seen: List[List[str]] = []

    def check() -> None:
        seen.append(ids(out))

    serve(
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"r1"}],"next_cursor":null}}]'),
                data(
                    '[{"op":"add","path":"/items/-","value":{"id":"r2"}},{"op":"add","path":"/items/0/extra","value":1}]'
                ),
                data('[{"op":"add","path":"/items/-","value":{"id":"r3"}}]'),
                END,
            ]
        },
        checks={"": {1: check, 2: check, 3: check}},
    )
    collect(out)
    # r1 is out before chunk 1 is read, r1 and r2 before chunk 2, all before the end event
    assert seen == [["r1"], ["r1", "r2"], ["r1", "r2", "r3"]]
    assert ids(out) == ["r1", "r2", "r3"]


def test_indexed_inserts_are_yielded_in_final_order_at_the_end(collect: Callable[[List[Any]], None]) -> None:
    out: List[Any] = []
    seen: List[List[str]] = []

    def check() -> None:
        seen.append(ids(out))

    serve(
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[],"next_cursor":null}}]'),
                data('[{"op":"add","path":"/items/0","value":{"id":"B"}}]'),
                data('[{"op":"add","path":"/items/0","value":{"id":"A"}}]'),
                data('[{"op":"add","path":"/items/2","value":{"id":"C"}},{"op":"add","path":"/items/1/x","value":1}]'),
                END,
            ]
        },
        checks={"": {2: check, 3: check, 4: check}},
    )
    collect(out)
    assert seen == [[], [], []]  # nothing is yielded before the end of the page's stream
    assert ids(out) == ["A", "B", "C"]


def test_next_page_is_requested_after_the_page_is_yielded(collect: Callable[[List[Any]], None]) -> None:
    out: List[Any] = []
    at_request: Dict[str, List[str]] = {}

    def on_request(cursor: str) -> None:
        at_request[cursor] = ids(out)

    serve(
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[],"next_cursor":null}}]'),
                data('[{"op":"add","path":"/items/0","value":{"id":"B"}}]'),
                data(
                    '[{"op":"add","path":"/items/0","value":{"id":"A"}},{"op":"replace","path":"/next_cursor","value":"c2"}]'
                ),
                END,
            ],
            "c2": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"D"}],"next_cursor":null}}]'),
                data('[{"op":"add","path":"/items/-","value":{"id":"E"}}]'),
                END,
            ],
        },
        on_request=on_request,
    )
    collect(out)
    assert ids(out) == ["A", "B", "D", "E"]
    assert at_request == {"": [], "c2": ["A", "B"]}


def test_replace_applies_to_items_not_yielded_yet(collect: Callable[[List[Any]], None]) -> None:
    out: List[Any] = []
    serve(
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[],"next_cursor":null}}]'),
                data(
                    '[{"op":"add","path":"/items/0","value":{"id":"X"}},{"op":"add","path":"/items/1","value":{"id":"Y"}}]'
                ),
                data('[{"op":"replace","path":"/items/0","value":{"id":"X2"}}]'),
                END,
            ]
        },
    )
    collect(out)
    assert ids(out) == ["X2", "Y"]


def test_yielded_items_are_not_changed_and_the_rest_is_held_back(collect: Callable[[List[Any]], None]) -> None:
    out: List[Any] = []
    seen: List[List[str]] = []

    def check() -> None:
        seen.append(ids(out))

    serve(
        {
            "": [
                data('[{"op":"add","path":"","value":{"items":[{"id":"r1"}],"next_cursor":null}}]'),
                data('[{"op":"replace","path":"/items/0","value":{"id":"changed"}}]'),
                data('[{"op":"add","path":"/items/-","value":{"id":"r2"}}]'),
                END,
            ]
        },
        checks={"": {2: check, 3: check}},
    )
    collect(out)
    # r1 was yielded and stays as it was; the replace switches the page to held back items
    assert seen == [["r1"], ["r1"]]
    assert ids(out) == ["r1", "r2"]
