# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Exact Agent ids (repeat the parameter; maximum 100)"""

    cursor: str
    """Opaque pagination cursor"""

    name: str
    """Case-insensitive partial Agent name"""

    page_size: int
    """Maximum number of Agents to return"""

    sort_by: Literal["last_run_start_time", "name", "created_at"]
    """Field to sort by. When name is set, exact name matches still come first."""

    sort_order: Literal["asc", "desc"]
    """Sort direction"""

    source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"]
    """Agent source type"""
