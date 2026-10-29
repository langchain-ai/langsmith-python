# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["EvaluatorListParams"]


class EvaluatorListParams(TypedDict, total=False):
    id: Optional[SequenceNotStr[str]]

    dataset_id: Optional[str]

    evaluator_id: Optional[str]

    include_backfill_progress: bool

    name_contains: Optional[str]

    session_id: Optional[str]

    tag_value_id: Optional[SequenceNotStr[str]]

    type: Optional[Literal["session", "dataset"]]
