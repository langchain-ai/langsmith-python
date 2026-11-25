"""Configuration management for Claude Agent SDK tracing."""

from typing import Any, Optional

from langsmith.address import AgentAddress

# Global configuration for tracing
_tracing_config: dict[str, Any] = {
    "name": None,
    "project_name": None,
    "address": None,
    "metadata": None,
    "tags": None,
}


def set_tracing_config(
    name: Optional[str] = None,
    project_name: Optional[str] = None,
    metadata: Optional[dict] = None,
    tags: Optional[list[str]] = None,
    address: Optional[AgentAddress] = None,
) -> None:
    """Set the global tracing configuration for Claude Agent SDK.

    Args:
        name: Name of the root trace.
        project_name: LangSmith project to trace to.
        address: An `AgentAddress` to trace to instead of a project;
            cannot be combined with `project_name`.
        metadata: Metadata to associate with all traces.
        tags: Tags to associate with all traces.
    """
    global _tracing_config
    _tracing_config = {
        "name": name,
        "project_name": project_name,
        "address": address,
        "metadata": metadata,
        "tags": tags,
    }


def get_tracing_config() -> dict[str, Any]:
    """Get the current tracing configuration."""
    return _tracing_config.copy()
