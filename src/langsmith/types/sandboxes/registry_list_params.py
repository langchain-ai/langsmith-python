# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RegistryListParams"]


class RegistryListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor from a prior response's next_cursor"""

    limit: int
    """Deprecated: use page_size. Maximum number of registries to return"""

    name_contains: str
    """Filter to registries whose name contains this substring"""

    offset: int
    """Deprecated: use cursor. Number of registries to skip"""

    page_size: int
    """Number of results per cursor page"""
