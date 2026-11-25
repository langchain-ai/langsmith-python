"""Tracing wrappers for the official ``mcp`` Python package (``mcp>=2``)."""

from __future__ import annotations

import contextvars
import functools
import hashlib
import logging
from collections.abc import Awaitable, Callable, Mapping
from typing import Any, Optional, TypeVar, Union, cast

from langsmith import run_helpers
from langsmith import utils as ls_utils
from langsmith.run_trees import LANGSMITH_DOTTED_ORDER, RunTree

logger = logging.getLogger(__name__)

# The only _meta keys read from a client: the parent's dotted order and baggage,
# the pair RunTree.to_headers() writes and RunTree.from_headers() parses.
_TRACE_META_KEYS = (LANGSMITH_DOTTED_ORDER, "baggage")
_WRAPPED = "__langsmith_mcp_wrapped__"
_TOOL_ERROR = "MCP tool returned an error"
_METADATA = {"ls_integration": "mcp"}

ClientT = TypeVar("ClientT")
ServerT = TypeVar("ServerT")


def wrap_mcp_client(client: ClientT, *, distributed_tracing: bool = False) -> ClientT:
    """Trace each tool call an MCP client makes.

    Each ``call_tool`` becomes a ``tool`` run, nested under the current trace when
    there is one.

    Args:
        client: An ``mcp.Client`` or ``mcp.ClientSession``. It is changed in place
            and returned.
        distributed_tracing: Send the run's trace context to the server in the
            request's ``_meta`` field, so a server wrapped with `wrap_mcp_server`
            and ``distributed_tracing=True`` continues the same trace. The context
            includes the project, tags and metadata, so only turn it on for
            servers you own.

    Returns:
        The same client.

    Example:
        >>> from mcp import Client  # doctest: +SKIP
        >>> from langsmith.integrations.mcp import wrap_mcp_client
        >>> async with Client("http://localhost:8000/mcp") as client:  # doctest: +SKIP
        ...     client = wrap_mcp_client(client, distributed_tracing=True)
        ...     await client.call_tool("get_weather", {"city": "Paris"})
    """
    original = client.call_tool  # type: ignore[attr-defined]
    if getattr(original, _WRAPPED, False):
        return client

    @functools.wraps(original)
    async def call_tool(
        name: str,
        arguments: Optional[dict[str, Any]] = None,
        *args: Any,
        meta: Optional[Mapping[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        with run_helpers.trace(
            name=name,
            run_type="tool",
            inputs={"name": name, "arguments": arguments or {}},
            metadata=_METADATA,
        ) as run:
            if distributed_tracing and ls_utils.tracing_is_enabled() is True:
                meta = {**(meta or {}), **run.to_headers()}
            result = await original(name, arguments, *args, meta=meta, **kwargs)
            _end_run(run, result)
            return result

    setattr(call_tool, _WRAPPED, True)
    client.call_tool = call_tool  # type: ignore[attr-defined]
    return client


def wrap_mcp_server(server: ServerT, *, distributed_tracing: bool = False) -> ServerT:
    """Trace each tool an MCP server runs.

    Adds a middleware to an ``MCPServer`` or a low-level
    ``mcp.server.lowlevel.Server``. Each ``tools/call`` becomes a ``tool`` run
    with the tool's arguments as inputs and its result as outputs. On stateful
    streamable HTTP, a run that starts its own trace gets a ``thread_id``
    derived from the session, so a session's calls group into one thread. When
    the run continues a client's trace, the client's trace owns the thread.

    Args:
        server: An ``MCPServer`` or low-level ``Server``. It is changed in place
            and returned.
        distributed_tracing: Continue the caller's trace when the request carries
            LangSmith trace context in ``_meta``. Off by default, so a client
            can't place the server's runs in another trace or project. Turn it on
            when you own the clients too.

    Returns:
        The same server.

    Example:
        >>> from mcp.server.mcpserver import MCPServer  # doctest: +SKIP
        >>> from langsmith.integrations.mcp import wrap_mcp_server
        >>> mcp = wrap_mcp_server(MCPServer("weather"), distributed_tracing=True)  # doctest: +SKIP
    """
    middleware = getattr(server, "middleware", None)
    if not isinstance(middleware, list):
        raise TypeError("wrap_mcp_server expects an mcp>=2 MCPServer or lowlevel Server")
    if not any(isinstance(m, _ToolTracingMiddleware) for m in middleware):
        middleware.append(_ToolTracingMiddleware(distributed_tracing))
    return server


class _ToolTracingMiddleware:
    """Server middleware that records each ``tools/call`` as a LangSmith run."""

    def __init__(self, distributed_tracing: bool) -> None:
        self.distributed_tracing = distributed_tracing

    async def __call__(self, ctx: Any, call_next: Callable[[Any], Awaitable[Any]]) -> Any:
        if ctx.method != "tools/call":
            return await call_next(ctx)
        params = ctx.params if isinstance(ctx.params, Mapping) else {}
        name = params.get("name")
        arguments = params.get("arguments")
        name = name if isinstance(name, str) else "tools/call"
        parent = (self.distributed_tracing and _trace_parent(ctx.meta)) or None
        thread_id = None if parent else _session_thread_id(ctx)
        with run_helpers.trace(
            name=name,
            run_type="tool",
            inputs={
                "name": name,
                "arguments": arguments if isinstance(arguments, Mapping) else {},
            },
            metadata={**_METADATA, "thread_id": thread_id} if thread_id else _METADATA,
            # The parent comes only from the request: an in-process transport can
            # leak the client's context into the handler, which must not decide it.
            parent=parent or "ignore",
        ) as run:
            result = await call_next(ctx)
            _end_run(run, result)
            return result


def _session_thread_id(ctx: Any) -> Optional[str]:
    """Return a thread id for the server-issued session this request belongs to.

    Only a session the server issued counts, so stateless and stdio requests get
    none and a client can't pick its thread. The id is hashed because a live
    session id can be enough to act within that session.
    """
    connection = getattr(getattr(ctx, "session", None), "_connection", None)
    session_id = getattr(connection, "session_id", None)
    if not isinstance(session_id, str) or not session_id:
        return None
    return hashlib.sha256(session_id.encode()).hexdigest()[:32]


def _trace_parent(meta: Any) -> Optional[dict[str, str]]:
    """Return the LangSmith trace headers a client sent in ``_meta``, if any.

    The headers are client input, so ones that don't parse are ignored and the
    tool call runs in a new trace instead of failing. They are parsed in a copied
    context because parsing sets the distributed parent, which ``trace`` must
    only set after it saves the caller's context.
    """
    if not isinstance(meta, Mapping):
        return None
    headers = {key: value for key in _TRACE_META_KEYS if isinstance(value := meta.get(key), str)}
    if LANGSMITH_DOTTED_ORDER not in headers:
        return None
    try:
        contextvars.copy_context().run(
            RunTree.from_headers, cast(Mapping[Union[str, bytes], Union[str, bytes]], headers)
        )
    except Exception:
        logger.debug("Ignoring malformed LangSmith trace context in MCP _meta")
        return None
    return headers


def _end_run(run: RunTree, result: Any) -> None:
    dump = getattr(result, "model_dump", None)
    if callable(dump):
        outputs = dump(mode="json", by_alias=True, exclude_none=True)
    elif isinstance(result, Mapping):
        outputs = dict(result)
    else:
        outputs = {"output": result}
    is_error = getattr(result, "is_error", None) or outputs.get("isError") is True
    run.end(outputs=outputs, error=_TOOL_ERROR if is_error else None)
