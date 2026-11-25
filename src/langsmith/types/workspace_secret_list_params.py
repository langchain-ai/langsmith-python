# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkspaceSecretListParams"]


class WorkspaceSecretListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor from a previous response"""

    include_configs: bool
    """Include the hosts each secret may be sent to"""

    page_size: int
    """Number of secrets per page"""
