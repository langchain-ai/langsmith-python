# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    upsert: bool

    id: Optional[str]

    default_dataset_id: Optional[str]

    description: Optional[str]

    end_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    evaluator_keys: Optional[SequenceNotStr[str]]

    extra: Optional[Dict[str, object]]

    kicked_off_by: Optional[str]

    longlived_ttl_days: Optional[int]
    """Retention in days for traces while trace_tier is longlived.

    One of the deployment's allowed values (allowed_longlived_ttl_days in /info), up
    to the maximum of the deployment. The value is kept while trace_tier is
    shortlived. Null means the project uses the workspace retention.
    """

    name: str

    num_examples: Optional[int]

    num_repetitions: Optional[int]

    reference_dataset_id: Optional[str]

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    tag_value_ids: Optional[SequenceNotStr[str]]

    trace_tier: Optional[Literal["longlived", "shortlived"]]
