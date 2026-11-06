# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    default_dataset_id: Optional[str]

    description: Optional[str]

    end_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    extra: Optional[Dict[str, object]]

    longlived_ttl_days: Optional[int]
    """Retention in days for traces while trace_tier is longlived.

    One of 30, 60, 90, 120, 150, 180, 240, 300, 365 or 400, up to the maximum of the
    deployment. Self-hosted also accepts its configured retention. The value is kept
    while trace_tier is shortlived. Null means the project uses the workspace
    retention. Omit the field to keep the current value.
    """

    name: Optional[str]

    trace_tier: Optional[Literal["longlived", "shortlived"]]
