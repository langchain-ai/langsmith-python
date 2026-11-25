# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["VolumeUpdateParams"]


class VolumeUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Description replaces the description; null or an empty string clears it."""

    labels: Optional[Dict[str, str]]
    """Labels replaces every label; null or an empty object clears them."""
