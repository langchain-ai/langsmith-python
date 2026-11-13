# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkspaceSecretListParams"]


class WorkspaceSecretListParams(TypedDict, total=False):
    include_configs: bool
    """If true, include the hosts each secret may be sent to."""
