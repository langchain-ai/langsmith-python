# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    agent_type: Literal["CUSTOM", "CODING"]
    """New classification. Omit to keep the current classification."""

    name: str
    """New display name. Omit to keep the current name."""

    owner_id: Optional[str]
    """Omit to leave the owner unchanged; null clears it."""

    source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"]
    """New runtime kind.

    Only EXTERNAL agents without runtime bindings can change kind.
    """
