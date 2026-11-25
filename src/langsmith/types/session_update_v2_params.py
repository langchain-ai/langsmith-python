# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionUpdateV2Params"]


class SessionUpdateV2Params(TypedDict, total=False):
    default_dataset_id: Optional[str]

    description: Optional[str]

    end_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    extra: Optional[object]

    longlived_ttl_days: Optional[int]

    name: str

    trace_tier: Literal["LONG_LIVED", "SHORT_LIVED"]
