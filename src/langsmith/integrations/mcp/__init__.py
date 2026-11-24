"""LangSmith tracing for MCP (Model Context Protocol) clients and servers.

Wrap an MCP client to trace each tool call, and wrap an MCP server to trace each
tool it runs. When you own both sides, turn on ``distributed_tracing`` on each:
the client passes its trace context in the request's ``_meta`` field, so the
server's run appears inside the client's trace.

Requires ``mcp>=2``.

Example:
    >>> from mcp import Client  # doctest: +SKIP
    >>> from mcp.server.mcpserver import MCPServer  # doctest: +SKIP
    >>> from langsmith.integrations.mcp import wrap_mcp_client, wrap_mcp_server
    >>> server = wrap_mcp_server(MCPServer("weather"), distributed_tracing=True)  # doctest: +SKIP
    >>> async with Client(server) as client:  # doctest: +SKIP
    ...     client = wrap_mcp_client(client, distributed_tracing=True)
    ...     await client.call_tool("get_weather", {"city": "Paris"})
"""

from ._wrappers import wrap_mcp_client, wrap_mcp_server

__all__ = ["wrap_mcp_client", "wrap_mcp_server"]
