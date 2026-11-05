# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SessionFeedbackStat"]


class SessionFeedbackStat(BaseModel):
    """Aggregate feedback for one feedback key."""

    avg: Optional[float] = None
    """Mean numeric score."""

    contains_thread_feedback: bool
    """Whether any feedback was left on a thread."""

    errors: int
    """Number of feedback entries recorded as errors."""

    max: Optional[float] = None
    """Highest numeric score."""

    median: Optional[float] = None
    """Median numeric score."""

    min: Optional[float] = None
    """Lowest numeric score."""

    n: int
    """Number of feedback scores for this key."""

    stdev: Optional[float] = None
    """Standard deviation of numeric scores."""

    type: Literal["PRIMARY", "COMPOSITE"]
    """
    `PRIMARY` for recorded feedback, `COMPOSITE` for a score computed from other
    feedback keys.
    """

    values: Dict[str, int]
    """Count of each categorical value."""
