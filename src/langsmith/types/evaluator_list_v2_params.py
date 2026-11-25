# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["EvaluatorListV2Params"]


class EvaluatorListV2Params(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Rule UUIDs"""

    cursor: str
    """Cursor from the previous page"""

    dataset_id: str
    """Source dataset UUID"""

    evaluator_id: str
    """Linked evaluator UUID"""

    include_backfill_progress: bool
    """Include backfill progress"""

    name_contains: str
    """Case-insensitive display-name pattern"""

    page_size: int
    """Page size"""

    project_id: str
    """Source project UUID"""

    tag_value_id: SequenceNotStr[str]
    """Source must have every tag UUID"""

    type: Literal["PROJECT", "DATASET"]
    """Rule source type"""
