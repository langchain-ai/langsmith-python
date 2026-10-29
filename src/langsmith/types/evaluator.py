# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .evaluator_webhook import EvaluatorWebhook
from .evaluator_top_level import EvaluatorTopLevel
from .code_evaluator_top_level import CodeEvaluatorTopLevel
from .evaluator_pagerduty_alert import EvaluatorPagerdutyAlert

__all__ = ["Evaluator", "SpendLimit"]


class SpendLimit(BaseModel):
    limit_usd: str

    window: Literal["weekly"]


class Evaluator(BaseModel):
    """Run rules schema."""

    id: str

    created_at: datetime

    display_name: str

    evaluator_version: int

    sampling_rate: float

    tenant_id: str

    updated_at: datetime

    webhooks: Optional[List[EvaluatorWebhook]] = None

    add_to_annotation_queue_id: Optional[str] = None

    add_to_annotation_queue_name: Optional[str] = None

    add_to_dataset_id: Optional[str] = None

    add_to_dataset_name: Optional[str] = None

    add_to_dataset_prefer_correction: Optional[bool] = None

    alerts: Optional[List[EvaluatorPagerdutyAlert]] = None

    alignment_annotation_queue_id: Optional[str] = None

    backfill_completed_at: Optional[datetime] = None

    backfill_error: Optional[str] = None

    backfill_from: Optional[datetime] = None

    backfill_id: Optional[str] = None

    backfill_progress: Optional[float] = None

    backfill_status: Optional[str] = None

    code_evaluators: Optional[List[CodeEvaluatorTopLevel]] = None

    corrections_dataset_id: Optional[str] = None

    dataset_id: Optional[str] = None

    dataset_name: Optional[str] = None

    evaluator_id: Optional[str] = None

    evaluator_name: Optional[str] = None

    evaluator_type: Optional[str] = None

    evaluators: Optional[List[EvaluatorTopLevel]] = None

    extend_annotation_queue_trace_retention: Optional[bool] = None

    extend_dataset_trace_retention: Optional[bool] = None

    extend_evaluator_trace_retention: Optional[bool] = None

    extend_only: Optional[bool] = None

    extend_webhook_trace_retention: Optional[bool] = None

    filter: Optional[str] = None

    group_by: Optional[Literal["thread_id", "trajectory_id"]] = None

    include_extended_stats: Optional[bool] = None

    is_enabled: Optional[bool] = None

    is_managed_evaluator: Optional[bool] = None

    is_tracing_disabled: Optional[bool] = None

    num_few_shot_examples: Optional[int] = None

    session_id: Optional[str] = None

    session_name: Optional[str] = None

    spend_limit: Optional[SpendLimit] = None

    spend_usd: Optional[float] = None

    trace_count: Optional[int] = None

    trace_filter: Optional[str] = None

    transient: Optional[bool] = None

    tree_filter: Optional[str] = None

    use_corrections_dataset: Optional[bool] = None
