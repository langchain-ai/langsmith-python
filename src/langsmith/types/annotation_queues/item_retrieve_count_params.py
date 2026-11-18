# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemRetrieveCountParams"]


class ItemRetrieveCountParams(TypedDict, total=False):
    status: Required[str]
    """Count bucket: all, needs_my_review, needs_others_review, or archived."""

    agreement: Literal["disagreed"]
    """Count only completed items whose reviewers disagreed on at least one rubric key.

    Returns 501 unless multi-reviewer queues are on for the workspace. Requires
    status=archived
    """

    end_time: str
    """Archived strictly before this time. Only used when status=archived"""

    has_unresolved_keys: bool
    """
    Count only completed items that do (true) or do not (false) still have a
    disagreed rubric key with no final answer. Items with no agreement result match
    neither value. Returns 501 unless multi-reviewer queues are on for the
    workspace. Requires status=archived
    """

    max_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Trace started at or before this time"""

    min_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Trace started at or after this time"""

    start_time: str
    """Archived strictly after this time. Only used when status=archived"""
