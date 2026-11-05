# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SessionListV2Params"]


class SessionListV2Params(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Only return projects with these IDs"""

    cursor: str
    """next_cursor from the previous page; omit for the first page"""

    dataset_version: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return experiments run against this dataset version (RFC 3339 timestamp)"""

    filter: str
    """Filter expression, for example eq(name, \\"""

    include_facets: bool
    """Include run facets"""

    include_stats: bool
    """Include run statistics"""

    metadata: str
    """JSON object the project metadata must contain"""

    name: str
    """Only return the project with this exact name"""

    name_contains: str
    """Only return projects whose name contains this substring"""

    page_size: int
    """Number of projects per page"""

    reference_dataset_id: SequenceNotStr[str]
    """Only return experiments run against these dataset IDs"""

    reference_free: bool
    """true for tracing projects only, false for experiments only"""

    sort_by: Literal[
        "NAME", "START_TIME", "LAST_RUN_START_TIME", "ERROR_RATE", "LATENCY_P50", "LATENCY_P99", "FEEDBACK"
    ]
    """Sort column. FEEDBACK requires reference_dataset_id"""

    sort_by_feedback_key: str
    """Feedback key to sort by; required when sort_by is FEEDBACK"""

    sort_by_feedback_source: Literal["RUN", "SESSION"]
    """Where the sort feedback is recorded; defaults to RUN when sort_by is FEEDBACK"""

    sort_order: Literal["asc", "desc"]
    """Sort direction"""

    stats_filter: str
    """Run filter expression that scopes the statistics"""

    stats_select: SequenceNotStr[str]
    """Statistics to include when include_stats is true; defaults to all"""

    stats_start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only aggregate statistics at or after this time, within the last 31 days"""

    tag_value_id: SequenceNotStr[str]
    """Only return projects tagged with all of these tag value IDs"""

    use_approx_stats: bool
    """
    Compute statistics from pre-aggregated data, which is faster but up to an hour
    stale
    """
