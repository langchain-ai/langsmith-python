# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitRetrieveParams"]


class CommitRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    get_examples: bool

    include: str
    """Comma-separated list of optional fields: "model", "is_draft" """

    include_model: bool
    """Deprecated: use Include instead"""

    is_view: bool
