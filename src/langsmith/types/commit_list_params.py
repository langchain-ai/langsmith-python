# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitListParams"]


class CommitListParams(TypedDict, total=False):
    owner: Required[str]

    include_stats: bool
    """IncludeStats determines whether to compute num_downloads and num_views"""

    limit: int
    """Limit is the pagination limit."""

    offset: int
    """Offset is the pagination offset."""

    tag: str
    """Tag filters commits to only those with a specific tag (e.g.

    "production", "staging")
    """
