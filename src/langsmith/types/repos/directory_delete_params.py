# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DirectoryDeleteParams"]


class DirectoryDeleteParams(TypedDict, total=False):
    owner: Required[str]

    repo_type: Literal["agent", "skill"]
    """Repository type to delete; a different type is treated as not found"""
