# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SandboxListUsageCostsParams"]


class SandboxListUsageCostsParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exclusive RFC3339 end time; the range must not exceed 31 days"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive RFC3339 start time"""

    cursor: str
    """Opaque pagination cursor"""

    granularity: Literal["HOUR", "RESOURCE"]
    """HOUR returns hourly buckets.

    RESOURCE sums each resource over the requested interval and sets period_start to
    start_time.
    """

    include_daily: bool
    """
    Include bounded daily physical usage for the top 10 resources per metric and
    Other. Requires RESOURCE and include_totals. Omitted when unrestricted access or
    service support is unavailable. CLI: use --format raw to show this summary.
    """

    include_totals: bool
    """Include usage totals across the filtered interval (RESOURCE only).

    Omitted when unrestricted resource access cannot be verified or the service does
    not support totals. CLI: use --format raw to show this summary.
    """

    page_size: int
    """Maximum rows to return"""

    resource_ids: SequenceNotStr[str]
    """Resource UUID filter; repeat this parameter up to 100 times"""

    resource_type: Literal["SANDBOX", "SNAPSHOT"]
    """Resource type filter"""
