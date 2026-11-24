"""Unit tests for the MCP client and server tracing wrappers."""

from __future__ import annotations

from typing import Any, Optional
from unittest import mock

import pytest

pytest.importorskip("mcp.server.mcpserver")

from mcp import Client as MCPClient  # noqa: E402
from mcp.server.lowlevel import Server  # noqa: E402
from mcp.server.mcpserver import MCPServer  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402
from mcp_types import CallToolResult, ListToolsResult, Tool  # noqa: E402

from langsmith import Client  # noqa: E402
from langsmith.integrations.mcp import wrap_mcp_client, wrap_mcp_server  # noqa: E402
from langsmith.run_helpers import trace, tracing_context  # noqa: E402
from langsmith.run_trees import RunTree  # noqa: E402


@pytest.fixture
def runs(monkeypatch: pytest.MonkeyPatch) -> dict[str, list[RunTree]]:
    """Record every run instead of sending it, keyed by run name."""
    client = Client(session=mock.MagicMock(), api_key="test", api_url="http://x")
    monkeypatch.setattr("langsmith.run_trees.get_cached_client", lambda **_: client)
    recorded: dict[str, list[RunTree]] = {}

    def record(self: RunTree, *args: Any, **kwargs: Any) -> None:
        if self not in recorded.setdefault(self.name, []):
            recorded[self.name].append(self)

    monkeypatch.setattr(RunTree, "post", record)
    monkeypatch.setattr(RunTree, "patch", record)
    return recorded


def _server() -> MCPServer:
    server = MCPServer("test")

    @server.tool()
    def add(a: int, b: int) -> int:
        return a + b

    @server.tool()
    def fail() -> str:
        raise ToolError("boom")

    return server


async def test_client_and_server_runs_share_one_trace(runs) -> None:
    server = wrap_mcp_server(_server(), distributed_tracing=True)
    with tracing_context(enabled=True):
        # The server takes its parent only from the request's _meta field, even
        # though this in-process client shares the agent's context with it.
        async with MCPClient(server) as client:
            client = wrap_mcp_client(client, distributed_tracing=True)
            with trace("agent") as agent:
                result = await client.call_tool("add", {"a": 1, "b": 2})

    assert not result.is_error
    client_run, server_run = runs["add"]
    assert client_run.parent_run_id == agent.id
    assert server_run.parent_run_id == client_run.id
    assert server_run.trace_id == agent.trace_id
    assert server_run.inputs == {"name": "add", "arguments": {"a": 1, "b": 2}}
    assert server_run.outputs["content"][0]["text"] == "3"
    assert server_run.extra["metadata"]["ls_integration"] == "mcp"


@pytest.mark.parametrize(
    "meta",
    [
        None,
        # Malformed trace context is client input: it is ignored, not an error.
        {"langsmith-trace": "not-a-dotted-order", "baggage": "%%%"},
    ],
)
@pytest.mark.parametrize("enabled", [True, False])
async def test_server_without_valid_trace_context_starts_its_own_trace(
    runs, meta: Optional[dict[str, str]], enabled: bool
) -> None:
    server = wrap_mcp_server(_server(), distributed_tracing=True)
    with tracing_context(enabled=enabled):
        async with MCPClient(server) as client:
            result = await client.call_tool("add", {"a": 1, "b": 2}, meta=meta)

    assert not result.is_error
    if enabled:
        (server_run,) = runs["add"]
        assert server_run.parent_run_id is None


async def test_server_ignores_client_trace_context_by_default(runs) -> None:
    server = wrap_mcp_server(_server())
    with tracing_context(enabled=True):
        async with MCPClient(server) as client:
            client = wrap_mcp_client(client, distributed_tracing=True)
            await client.call_tool("add", {"a": 1, "b": 2})

    client_run, server_run = runs["add"]
    assert server_run.parent_run_id is None
    assert server_run.trace_id != client_run.trace_id


async def test_tool_error_is_recorded_on_both_runs(runs) -> None:
    server = wrap_mcp_server(_server())
    with tracing_context(enabled=True):
        async with MCPClient(server) as client:
            client = wrap_mcp_client(client)
            result = await client.call_tool("fail", {})

    assert result.is_error
    assert len(runs["fail"]) == 2
    assert all(run.error for run in runs["fail"])


async def test_lowlevel_server_is_traced(runs) -> None:
    async def on_list_tools(ctx: Any, params: Any) -> ListToolsResult:
        return ListToolsResult(tools=[Tool(name="echo", input_schema={"type": "object"})])

    async def on_call_tool(ctx: Any, params: Any) -> CallToolResult:
        return CallToolResult(content=[])

    server = wrap_mcp_server(Server("lowlevel", on_list_tools=on_list_tools, on_call_tool=on_call_tool))
    with tracing_context(enabled=True):
        async with MCPClient(server) as client:
            await client.call_tool("echo", {"x": 1})

    (server_run,) = runs["echo"]
    assert server_run.inputs == {"name": "echo", "arguments": {"x": 1}}


class _Connection:
    def __init__(self, session_id: Optional[str]) -> None:
        self.session_id = session_id


class _Session:
    def __init__(self, session_id: Optional[str]) -> None:
        self._connection = _Connection(session_id)


class _Ctx:
    method = "tools/call"
    params = {"name": "add", "arguments": {"a": 1}}

    def __init__(self, session_id: Optional[str], meta: Optional[dict] = None) -> None:
        self.session = _Session(session_id)
        self.meta = meta


async def _call_middleware(server: Any, ctx: _Ctx) -> None:
    async def call_next(ctx: Any) -> CallToolResult:
        return CallToolResult(content=[])

    with tracing_context(enabled=True):
        await server.middleware[-1](ctx, call_next)


async def test_server_groups_a_session_into_a_hashed_thread(runs) -> None:
    server = wrap_mcp_server(_server())
    await _call_middleware(server, _Ctx("sess-123"))
    await _call_middleware(server, _Ctx("sess-123"))
    await _call_middleware(server, _Ctx(None))

    first, second, no_session = runs["add"]
    thread_id = first.extra["metadata"]["thread_id"]
    assert thread_id == second.extra["metadata"]["thread_id"]
    assert "sess-123" not in thread_id, "the live session id is never uploaded"
    assert "thread_id" not in no_session.extra["metadata"]


async def test_server_run_in_a_client_trace_leaves_the_thread_to_the_client(runs) -> None:
    with tracing_context(enabled=True), trace("agent") as agent:
        headers = agent.to_headers()
    server = wrap_mcp_server(_server(), distributed_tracing=True)
    await _call_middleware(server, _Ctx("sess-123", meta=headers))

    (server_run,) = runs["add"]
    assert server_run.parent_run_id == agent.id
    assert "thread_id" not in server_run.extra["metadata"]


class _FakeClient:
    def __init__(self) -> None:
        self.meta: Optional[dict[str, Any]] = None

    async def call_tool(
        self, name: str, arguments: Optional[dict] = None, *, meta: Optional[dict] = None
    ) -> CallToolResult:
        self.meta = meta
        return CallToolResult(content=[])


async def test_client_does_not_send_trace_context_by_default(runs) -> None:
    client = wrap_mcp_client(_FakeClient())
    with tracing_context(enabled=True):
        await client.call_tool("add", {}, meta={"progressToken": 1})
    assert client.meta == {"progressToken": 1}


async def test_client_sends_trace_context_only_when_tracing(runs) -> None:
    client = wrap_mcp_client(_FakeClient(), distributed_tracing=True)
    with tracing_context(enabled=False):
        await client.call_tool("add", {}, meta={"progressToken": 1})
    assert client.meta == {"progressToken": 1}

    with tracing_context(enabled=True):
        await client.call_tool("add", {}, meta={"progressToken": 1})
    assert client.meta is not None
    assert client.meta["progressToken"] == 1
    assert "langsmith-trace" in client.meta


def test_wrapping_twice_is_a_no_op() -> None:
    client = wrap_mcp_client(_FakeClient())
    call_tool = client.call_tool
    assert wrap_mcp_client(client).call_tool is call_tool

    server = wrap_mcp_server(wrap_mcp_server(_server()))
    assert len(server.middleware) == len(MCPServer("fresh").middleware) + 1


def test_rejects_objects_that_are_not_mcp_servers() -> None:
    with pytest.raises(TypeError, match="MCPServer or lowlevel Server"):
        wrap_mcp_server(object())


def test_reading_client_trace_context_keeps_the_callers_distributed_parent() -> None:
    from langsmith import run_trees
    from langsmith.integrations.mcp._wrappers import _trace_parent

    headers = RunTree(name="client", project_name="p").to_headers()
    token = run_trees._DISTRIBUTED_PARENT_ID.set("outer")
    try:
        assert _trace_parent(headers) == headers
        assert run_trees._DISTRIBUTED_PARENT_ID.get() == "outer"
    finally:
        run_trees._DISTRIBUTED_PARENT_ID.reset(token)
