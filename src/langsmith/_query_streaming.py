"""Item iterators over streamed JSON Patch queries."""

from __future__ import annotations

from typing import Any, Dict, List, TypeVar, Callable, Iterator, Optional, Awaitable, AsyncIterator, cast

from ._models import validate_type
from ._streaming import Stream, AsyncStream

__all__ = ["iter_query_stream", "aiter_query_stream"]

_T = TypeVar("_T")
_E = TypeVar("_E")


def _pointer_get(doc: Any, path: str) -> Any:
    for key in path.split("/")[1:]:
        if not isinstance(doc, dict):
            return None
        doc = cast("Dict[str, Any]", doc).get(key)
    return doc


class _Page:
    """The items and next cursor of one page, rebuilt from the patches of its stream.

    Items are yielded as they arrive while the server only appends (`add <items_path>/-`, or the items of the
    root document): their order is final. As soon as the page sees an indexed patch (`add <items_path>/<n>`,
    `replace` or `remove`), the order of the items is only known once the stream ends, so the rest of the page
    is held back until then. Items already yielded cannot be reordered or changed afterwards.

    Patches deeper than one item (`<items_path>/<n>/<field>`) are ignored: the item was already yielded.
    """

    def __init__(self, items_path: str, next_cursor_path: str) -> None:
        self._items_path = items_path
        self._next_cursor_path = next_cursor_path
        self._items: List[object] = []
        self._yielded = 0
        self._buffered = False
        self.next: Optional[str] = None

    def apply(self, event: Any) -> None:
        for op in event:
            path: str = op.path
            kind: str = op.op
            if path == "":
                doc: Any = op.value or {}
                self.next = _pointer_get(doc, self._next_cursor_path)
                # A root document replaces the items that were not yielded yet.
                self._items[self._yielded :] = (_pointer_get(doc, self._items_path) or [])[self._yielded :]
            elif path == self._next_cursor_path:
                self.next = None if kind == "remove" else op.value  # type: ignore[assignment]
            elif path.startswith(self._items_path + "/"):
                self._apply_item(kind, path[len(self._items_path) + 1 :], op.value)

    def _apply_item(self, kind: str, key: str, value: object) -> None:
        if key == "-":
            if kind == "add":
                self._items.append(value)
            return
        if not key.isascii() or not key.isdigit():
            return  # deeper patch
        self._buffered = True
        index = int(key)
        if kind == "add":
            # An item cannot be inserted before one that was already yielded: it comes first among the rest.
            self._items.insert(min(max(index, self._yielded), len(self._items)), value)
        elif index >= self._yielded and index < len(self._items):
            if kind == "replace":
                self._items[index] = value
            elif kind == "remove":
                del self._items[index]

    def ready(self) -> List[object]:
        """The items that can be yielded now."""
        return [] if self._buffered else self.rest()

    def rest(self) -> List[object]:
        """The items not yielded yet, in final order."""
        items = self._items[self._yielded :]
        self._yielded = len(self._items)
        return items


def iter_query_stream(
    item_type: type[_T],
    query: Callable[..., Stream[_E]],
    params: Dict[str, Any],
    *,
    items_path: str = "/items",
    next_cursor_path: str = "/next_cursor",
    cursor_param: str = "cursor",
) -> Iterator[_T]:
    """Calls `query(**params)`, yields the items and follows the next cursor across pages.

    See `_Page` for when items are yielded.
    """
    cursor: Optional[str] = None
    while True:
        page = _Page(items_path, next_cursor_path)
        stream = query(**(params if cursor is None else {**params, cursor_param: cursor}))
        try:
            for event in stream:
                page.apply(event)
                for raw in page.ready():
                    yield validate_type(type_=item_type, value=raw)
            for raw in page.rest():
                yield validate_type(type_=item_type, value=raw)
        finally:
            stream.close()
        cursor = page.next
        if not cursor:
            return


async def aiter_query_stream(
    item_type: type[_T],
    query: Callable[..., Awaitable[AsyncStream[_E]]],
    params: Dict[str, Any],
    *,
    items_path: str = "/items",
    next_cursor_path: str = "/next_cursor",
    cursor_param: str = "cursor",
) -> AsyncIterator[_T]:
    """Async variant of `iter_query_stream`."""
    cursor: Optional[str] = None
    while True:
        page = _Page(items_path, next_cursor_path)
        stream = await query(**(params if cursor is None else {**params, cursor_param: cursor}))
        try:
            async for event in stream:
                page.apply(event)
                for raw in page.ready():
                    yield validate_type(type_=item_type, value=raw)
            for raw in page.rest():
                yield validate_type(type_=item_type, value=raw)
        finally:
            await stream.close()
        cursor = page.next
        if not cursor:
            return
