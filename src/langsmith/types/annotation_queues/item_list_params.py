# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    status: Required[Literal["needs_my_review", "needs_others_review", "archived"]]
    """Review section: needs_my_review, needs_others_review, or archived"""

    agreement: Literal["disagreed"]
    """Only completed items whose reviewers disagreed on at least one rubric key.

    Returns 501 unless multi-reviewer queues are on for the workspace. Requires
    status=archived
    """

    cursor: str
    """Opaque pagination cursor"""

    direction: Literal["forward", "backward"]
    """Pagination direction. backward requires cursor"""

    has_unresolved_keys: bool
    """
    Only completed items that do (true) or do not (false) still have a disagreed
    rubric key with no final answer. Items with no agreement result match neither
    value. Returns 501 unless multi-reviewer queues are on for the workspace.
    Requires status=archived
    """

    item_type: Literal["RUN", "THREAD"]
    """Filter to RUN or THREAD"""

    max_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only items whose trace start time is at or before this timestamp.

    Omit or send the zero time for no bound
    """

    min_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only items whose trace start time is at or after this timestamp.

    Omit or send the zero time for no bound
    """

    page_size: int
    """Page size (max 100)"""
