# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .session_feedback_stat import SessionFeedbackStat

__all__ = ["Session", "ExperimentProgress"]


class ExperimentProgress(BaseModel):
    evaluator_progress: Dict[str, float]

    expected_run_count: int

    run_progress: float


class Session(BaseModel):
    """TracerSession schema."""

    id: str

    name: str

    start_time: datetime

    tenant_id: str

    type: Literal["PROJECT", "AGENT", "EXPERIMENT"]
    """
    `PROJECT` for a tracing project, `AGENT` for an Agent's tracing project, or
    `EXPERIMENT` for an evaluation run against a dataset.
    """

    completion_cost: Optional[float] = None

    completion_tokens: Optional[int] = None

    default_dataset_id: Optional[str] = None

    description: Optional[str] = None

    end_time: Optional[datetime] = None

    error_rate: Optional[float] = None

    experiment_progress: Optional[ExperimentProgress] = None

    extra: Optional[Dict[str, object]] = None

    feedback_stats: Optional[Dict[str, SessionFeedbackStat]] = None
    """Feedback on the session's runs, by feedback key."""

    first_token_p50: Optional[float] = None

    first_token_p99: Optional[float] = None

    last_run_start_time: Optional[datetime] = None

    last_run_start_time_live: Optional[datetime] = None

    latency_p50: Optional[float] = None

    latency_p99: Optional[float] = None

    longlived_ttl_days: Optional[int] = None
    """Retention in days for traces while trace_tier is longlived.

    One of the deployment's allowed values (allowed_longlived_ttl_days in /info), up
    to the maximum of the deployment. The value is kept while trace_tier is
    shortlived. Null means the project uses the workspace retention.
    """

    prompt_cost: Optional[float] = None

    prompt_tokens: Optional[int] = None

    reference_dataset_id: Optional[str] = None

    run_count: Optional[int] = None

    run_facets: Optional[List[Dict[str, object]]] = None

    session_feedback_stats: Optional[Dict[str, SessionFeedbackStat]] = None
    """Feedback on the session itself, by feedback key."""

    streaming_rate: Optional[float] = None

    test_run_number: Optional[int] = None

    total_cost: Optional[float] = None

    total_tokens: Optional[int] = None

    trace_tier: Optional[Literal["LONG_LIVED", "SHORT_LIVED"]] = None
