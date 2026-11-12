# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Rule",
    "Alert",
    "CodeEvaluator",
    "EffectiveSpendLimit",
    "Evaluator",
    "EvaluatorStructured",
    "SpendLimit",
    "Webhook",
]


class Alert(BaseModel):
    routing_key: str

    severity: Optional[Literal["CRITICAL", "WARNING", "ERROR", "INFO"]] = None

    summary: Optional[str] = None

    type: Optional[Literal["PAGERDUTY"]] = None


class CodeEvaluator(BaseModel):
    code: str

    require_attachments: bool

    advanced_features_enabled: Optional[bool] = None

    code_evaluator_input: Optional[
        Literal["THREAD", "ALL_MESSAGES", "HUMAN_AI_PAIRS", "FIRST_HUMAN_LAST_AI", "TRAJECTORY"]
    ] = None

    language: Optional[Literal["PYTHON", "JAVASCRIPT"]] = None


class EffectiveSpendLimit(BaseModel):
    limit_usd: str

    window: Literal["WEEKLY"]


class EvaluatorStructured(BaseModel):
    hub_ref: Optional[str] = None

    model: Optional[Dict[str, object]] = None

    playground_settings_id: Optional[str] = None

    prompt: Optional[List[List[str]]] = None

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)

    template_format: Optional[str] = None

    variable_mapping: Optional[Dict[str, str]] = None


class Evaluator(BaseModel):
    structured: EvaluatorStructured


class SpendLimit(BaseModel):
    limit_usd: str

    window: Literal["WEEKLY"]


class Webhook(BaseModel):
    url: str

    headers: Optional[Dict[str, str]] = None


class Rule(BaseModel):
    id: str

    add_to_dataset_prefer_correction: bool

    created_at: datetime

    display_name: str

    evaluator_version: int

    extend_only: bool

    include_extended_stats: bool

    is_enabled: bool

    is_managed_evaluator: bool

    is_tracing_disabled: bool

    sampling_rate: float

    tenant_id: str

    transient: bool

    updated_at: datetime

    use_corrections_dataset: bool

    add_to_annotation_queue_id: Optional[str] = None

    add_to_annotation_queue_name: Optional[str] = None

    add_to_dataset_id: Optional[str] = None

    add_to_dataset_name: Optional[str] = None

    alerts: Optional[List[Alert]] = None

    alignment_annotation_queue_id: Optional[str] = None

    backfill_completed_at: Optional[datetime] = None

    backfill_error: Optional[str] = None

    backfill_from: Optional[datetime] = None

    backfill_id: Optional[str] = None

    backfill_progress: Optional[float] = None

    backfill_status: Optional[str] = None

    code_evaluators: Optional[List[CodeEvaluator]] = None

    corrections_dataset_id: Optional[str] = None

    dataset_id: Optional[str] = None

    dataset_name: Optional[str] = None

    effective_spend_limit: Optional[EffectiveSpendLimit] = None

    evaluator_id: Optional[str] = None

    evaluator_name: Optional[str] = None

    evaluator_type: Optional[str] = None

    evaluators: Optional[List[Evaluator]] = None

    extend_annotation_queue_trace_retention: Optional[bool] = None

    extend_dataset_trace_retention: Optional[bool] = None

    extend_evaluator_trace_retention: Optional[bool] = None

    extend_webhook_trace_retention: Optional[bool] = None

    filter: Optional[str] = None

    group_by: Optional[Literal["THREAD_ID", "TRAJECTORY_ID"]] = None

    num_few_shot_examples: Optional[int] = None

    project_id: Optional[str] = None

    project_name: Optional[str] = None

    spend_limit: Optional[SpendLimit] = None

    spend_usd: Optional[float] = None

    thread_filter: Optional[str] = None

    trace_count: Optional[int] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None

    webhooks: Optional[List[Webhook]] = None
