# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ItemSetReviewParams"]


class ItemSetReviewParams(TypedDict, total=False):
    queue_id: Required[str]

    item_id: Required[str]

    score: float

    value: str

    values: SequenceNotStr[str]
