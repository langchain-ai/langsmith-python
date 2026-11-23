# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReviewerListParams"]


class ReviewerListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor"""

    page_size: int
    """Page size (max 100)"""
