# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SessionCreateV2Params"]


class SessionCreateV2Params(TypedDict, total=False):
    type: Required[Literal["PROJECT", "AGENT", "EXPERIMENT"]]
    """Type identifies a tracing project, Agent tracing project, or experiment."""

    upsert: bool
    """Update an existing session with the same name"""

    id: str

    default_dataset_id: str

    description: str

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    evaluator_keys: SequenceNotStr[str]

    extra: Dict[str, object]

    kicked_off_by: str

    longlived_ttl_days: Optional[int]
    """LonglivedTTLDays overrides long-lived trace retention.

    Null restores the workspace default.
    """

    name: str

    num_examples: int

    num_repetitions: int

    reference_dataset_id: str

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    tag_value_ids: SequenceNotStr[str]

    trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"]
