# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    id: Required[str]
    """
    Unique agent identifier: 1-63 lowercase letters, digits, or hyphens, starting
    with a letter and ending with a letter or digit.
    """

    source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"]
    """Agent runtime kind. Defaults to EXTERNAL for an application hosted outside LangSmith."""

    agent_type: Literal["CUSTOM", "CODING"]
    """AgentType defaults to CUSTOM when omitted."""

    name: str
    """Display name. Defaults to the agent ID."""

    production_only: bool
    """ProductionOnly creates only the PRODUCTION environment.

    It is accepted only when SourceType is FLEET; other sources always get all four
    environments.
    """
