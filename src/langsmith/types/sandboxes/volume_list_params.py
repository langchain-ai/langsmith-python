# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VolumeListParams"]


class VolumeListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a prior response's next_cursor"""

    name_contains: str
    """Filter by name substring"""

    page_size: int
    """Number of results per page"""
