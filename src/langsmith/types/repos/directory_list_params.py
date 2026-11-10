# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DirectoryListParams"]


class DirectoryListParams(TypedDict, total=False):
    owner: Required[str]

    commit: str
    """Commit hash/tag to resolve (defaults to latest)"""
