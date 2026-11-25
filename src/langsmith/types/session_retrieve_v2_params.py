# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionRetrieveV2Params"]


class SessionRetrieveV2Params(TypedDict, total=False):
    include_stats: bool
    """Include run statistics"""

    stats_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only aggregate statistics at or after this time, within the last 31 days"""
