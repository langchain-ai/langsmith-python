# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "CustomChartsSection",
    "Chart",
    "ChartSingleCustomChartResponseSerialized",
    "ChartSingleCustomChartResponseSerializedData",
    "ChartSingleCustomChartResponseSerializedSeries",
    "ChartSingleCustomChartResponseSerializedSeriesFilterDefinition",
    "ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByTracingProject",
    "ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByDataset",
    "ChartSingleCustomChartResponseSerializedSeriesFilters",
    "ChartSingleCustomChartResponseSerializedSeriesGroupBy",
    "ChartSingleCustomChartResponseSerializedSeriesGroupByDefinition",
    "ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByPlain",
    "ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByComplex",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinition",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetric",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetricParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricCount",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutput",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile",
    "ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams",
    "ChartSingleCustomChartResponseSerializedCommonFilters",
    "ChartCustomTextBlock",
    "Layout",
    "LayoutBreakpoints",
    "LayoutBreakpointsMd",
    "LayoutBreakpointsMdRow",
    "LayoutBreakpointsMdRowItem",
    "LayoutBreakpointsSm",
    "LayoutBreakpointsSmRow",
    "LayoutBreakpointsSmRowItem",
    "SubSection",
    "SubSectionChart",
    "SubSectionChartData",
    "SubSectionChartSeries",
    "SubSectionChartSeriesFilterDefinition",
    "SubSectionChartSeriesFilterDefinitionCustomChartFilterByTracingProject",
    "SubSectionChartSeriesFilterDefinitionCustomChartFilterByDataset",
    "SubSectionChartSeriesFilters",
    "SubSectionChartSeriesGroupBy",
    "SubSectionChartSeriesGroupByDefinition",
    "SubSectionChartSeriesGroupByDefinitionCustomChartGroupByPlain",
    "SubSectionChartSeriesGroupByDefinitionCustomChartGroupByComplex",
    "SubSectionChartSeriesMetricDefinition",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetric",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetricParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricCount",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentileParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutput",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile",
    "SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams",
    "SubSectionChartCommonFilters",
]


class ChartSingleCustomChartResponseSerializedData(BaseModel):
    series_id: str

    timestamp: datetime

    value: Union[float, Dict[str, object], None] = None

    group: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByTracingProject(BaseModel):
    project_ids: List[str]

    source_type: Literal["tracing_project"]

    run_filter: Optional[str] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByDataset(BaseModel):
    dataset_ids: List[str]

    source_type: Literal["dataset"]


ChartSingleCustomChartResponseSerializedSeriesFilterDefinition: TypeAlias = Union[
    ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByTracingProject,
    ChartSingleCustomChartResponseSerializedSeriesFilterDefinitionCustomChartFilterByDataset,
    None,
]


class ChartSingleCustomChartResponseSerializedSeriesFilters(BaseModel):
    filter: Optional[str] = None

    session: Optional[List[str]] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesGroupBy(BaseModel):
    """Include additional information about where the group_by param was set."""

    attribute: Literal["name", "run_type", "tag", "metadata"]

    max_groups: Optional[int] = None

    path: Optional[str] = None

    set_by: Optional[Literal["section", "series"]] = None


class ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByPlain(BaseModel):
    attribute: Literal["name", "run_type", "tag", "project", "status"]


class ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByComplex(BaseModel):
    attribute: Literal["metadata", "feedback_label"]

    path: str


ChartSingleCustomChartResponseSerializedSeriesGroupByDefinition: TypeAlias = Union[
    ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByPlain,
    ChartSingleCustomChartResponseSerializedSeriesGroupByDefinitionCustomChartGroupByComplex,
]


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetricParams(BaseModel):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetric(BaseModel):
    entity: Literal["feedback"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetricParams

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricCount(BaseModel):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams(
    BaseModel
):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar(BaseModel):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricScalar(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams(
    BaseModel
):
    feedback_key: str

    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile(BaseModel):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentileParams(BaseModel):
    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentile(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams(
    BaseModel
):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric(
    BaseModel
):
    entity: Literal["feedback"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount(
    BaseModel
):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams(
    BaseModel
):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar(
    BaseModel
):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar(
    BaseModel
):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams(
    BaseModel
):
    feedback_key: str

    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile(
    BaseModel
):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams(
    BaseModel
):
    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile(
    BaseModel
):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator: TypeAlias = Union[
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile,
]


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams(
    BaseModel
):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric(
    BaseModel
):
    entity: Literal["feedback"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount(
    BaseModel
):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams(
    BaseModel
):
    feedback_key: str


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar(
    BaseModel
):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar(
    BaseModel
):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams(
    BaseModel
):
    feedback_key: str

    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile(
    BaseModel
):
    field: Literal["feedback_score"]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams(
    BaseModel
):
    p: float


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile(
    BaseModel
):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator: TypeAlias = Union[
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile,
]


class ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutput(BaseModel):
    denominator: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator

    numerator: ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator

    type: Literal["ratio"]


ChartSingleCustomChartResponseSerializedSeriesMetricDefinition: TypeAlias = Union[
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackCountMetric,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricCount,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricScalar,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricPercentile,
    ChartSingleCustomChartResponseSerializedSeriesMetricDefinitionCustomChartMetricRatioOutput,
    None,
]


class ChartSingleCustomChartResponseSerializedSeries(BaseModel):
    id: str

    name: str

    feedback_key: Optional[str] = None

    filter_definition: Optional[ChartSingleCustomChartResponseSerializedSeriesFilterDefinition] = None

    filters: Optional[ChartSingleCustomChartResponseSerializedSeriesFilters] = None

    group_by: Optional[ChartSingleCustomChartResponseSerializedSeriesGroupBy] = None
    """Include additional information about where the group_by param was set."""

    group_by_definitions: Optional[List[ChartSingleCustomChartResponseSerializedSeriesGroupByDefinition]] = None

    metadata: Optional[Dict[str, object]] = None

    metric: Optional[
        Literal[
            "run_count",
            "latency_p50",
            "latency_p99",
            "latency_avg",
            "first_token_p50",
            "first_token_p99",
            "total_tokens",
            "prompt_tokens",
            "completion_tokens",
            "median_tokens",
            "completion_tokens_p50",
            "prompt_tokens_p50",
            "tokens_p99",
            "completion_tokens_p99",
            "prompt_tokens_p99",
            "feedback",
            "feedback_score_avg",
            "feedback_values",
            "total_cost",
            "prompt_cost",
            "completion_cost",
            "error_rate",
            "streaming_rate",
            "cost_p50",
            "cost_p99",
        ]
    ] = None
    """Metrics you can chart.

    Feedback metrics are not available for organization-scoped charts.
    """

    metric_definition: Optional[ChartSingleCustomChartResponseSerializedSeriesMetricDefinition] = None

    project_metric: Optional[
        Literal[
            "memory_usage",
            "cpu_usage",
            "disk_usage",
            "restart_count",
            "replica_count",
            "worker_count",
            "lg_run_count",
            "responses_per_second",
            "error_responses_per_second",
            "p95_latency",
            "run_queue_wait_time",
        ]
    ] = None
    """LGP Metrics you can chart."""

    workspace_id: Optional[str] = None


class ChartSingleCustomChartResponseSerializedCommonFilters(BaseModel):
    filter: Optional[str] = None

    session: Optional[List[str]] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class ChartSingleCustomChartResponseSerialized(BaseModel):
    id: str

    chart_type: Literal["line", "bar", "table", "kpi", "top-k", "pie"]

    data: List[ChartSingleCustomChartResponseSerializedData]

    index: int

    series: List[ChartSingleCustomChartResponseSerializedSeries]

    title: str

    common_filters: Optional[ChartSingleCustomChartResponseSerializedCommonFilters] = None

    description: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


class ChartCustomTextBlock(BaseModel):
    id: str

    chart_type: Literal["text"]

    index: int

    markdown: str

    metadata: Optional[Dict[str, object]] = None


Chart: TypeAlias = Union[ChartSingleCustomChartResponseSerialized, ChartCustomTextBlock]


class LayoutBreakpointsMdRowItem(BaseModel):
    chart_id: str

    width_units: int


class LayoutBreakpointsMdRow(BaseModel):
    height_units: int

    items: List[LayoutBreakpointsMdRowItem]


class LayoutBreakpointsMd(BaseModel):
    rows: List[LayoutBreakpointsMdRow]


class LayoutBreakpointsSmRowItem(BaseModel):
    chart_id: str

    width_units: int


class LayoutBreakpointsSmRow(BaseModel):
    height_units: int

    items: List[LayoutBreakpointsSmRowItem]


class LayoutBreakpointsSm(BaseModel):
    rows: List[LayoutBreakpointsSmRow]


class LayoutBreakpoints(BaseModel):
    md: LayoutBreakpointsMd

    sm: LayoutBreakpointsSm


class Layout(BaseModel):
    breakpoints: LayoutBreakpoints

    version: Literal[1]


class SubSectionChartData(BaseModel):
    series_id: str

    timestamp: datetime

    value: Union[float, Dict[str, object], None] = None

    group: Optional[str] = None


class SubSectionChartSeriesFilterDefinitionCustomChartFilterByTracingProject(BaseModel):
    project_ids: List[str]

    source_type: Literal["tracing_project"]

    run_filter: Optional[str] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class SubSectionChartSeriesFilterDefinitionCustomChartFilterByDataset(BaseModel):
    dataset_ids: List[str]

    source_type: Literal["dataset"]


SubSectionChartSeriesFilterDefinition: TypeAlias = Union[
    SubSectionChartSeriesFilterDefinitionCustomChartFilterByTracingProject,
    SubSectionChartSeriesFilterDefinitionCustomChartFilterByDataset,
    None,
]


class SubSectionChartSeriesFilters(BaseModel):
    filter: Optional[str] = None

    session: Optional[List[str]] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class SubSectionChartSeriesGroupBy(BaseModel):
    """Include additional information about where the group_by param was set."""

    attribute: Literal["name", "run_type", "tag", "metadata"]

    max_groups: Optional[int] = None

    path: Optional[str] = None

    set_by: Optional[Literal["section", "series"]] = None


class SubSectionChartSeriesGroupByDefinitionCustomChartGroupByPlain(BaseModel):
    attribute: Literal["name", "run_type", "tag", "project", "status"]


class SubSectionChartSeriesGroupByDefinitionCustomChartGroupByComplex(BaseModel):
    attribute: Literal["metadata", "feedback_label"]

    path: str


SubSectionChartSeriesGroupByDefinition: TypeAlias = Union[
    SubSectionChartSeriesGroupByDefinitionCustomChartGroupByPlain,
    SubSectionChartSeriesGroupByDefinitionCustomChartGroupByComplex,
]


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetricParams(BaseModel):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetric(BaseModel):
    entity: Literal["feedback"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetricParams

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricCount(BaseModel):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams(BaseModel):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar(BaseModel):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricScalar(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams(BaseModel):
    feedback_key: str

    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile(BaseModel):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentileParams(BaseModel):
    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentile(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams(
    BaseModel
):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric(
    BaseModel
):
    entity: Literal["feedback"]

    params: (
        SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetricParams
    )

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount(BaseModel):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams(
    BaseModel
):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar(
    BaseModel
):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams(
    BaseModel
):
    feedback_key: str

    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile(
    BaseModel
):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams(
    BaseModel
):
    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile(
    BaseModel
):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: (
        SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentileParams
    )

    type: Literal["percentile"]

    filter: Optional[str] = None


SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator: TypeAlias = Union[
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackCountMetric,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricCount,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartFeedbackScoreMetricPercentile,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominatorCustomChartMetricPercentile,
]


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams(
    BaseModel
):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric(
    BaseModel
):
    entity: Literal["feedback"]

    params: (
        SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetricParams
    )

    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount(BaseModel):
    filter: Optional[str] = None

    type: Optional[Literal["count"]] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams(
    BaseModel
):
    feedback_key: str


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar(
    BaseModel
):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalarParams

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    type: Literal["sum", "max", "min", "avg"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams(
    BaseModel
):
    feedback_key: str

    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile(
    BaseModel
):
    field: Literal["feedback_score"]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams(
    BaseModel
):
    p: float


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile(BaseModel):
    field: Literal[
        "latency_seconds",
        "first_token_seconds",
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "prompt_token_details.cache_creation",
        "prompt_token_details.cache_read",
        "prompt_token_details.ephemeral_1h_input_tokens",
        "prompt_token_details.ephemeral_5m_input_tokens",
        "prompt_token_details.audio",
        "prompt_token_details.image",
        "prompt_token_details.video",
        "completion_token_details.reasoning",
        "completion_token_details.audio",
        "completion_token_details.image",
        "completion_token_details.video",
        "total_cost",
        "prompt_cost",
        "completion_cost",
        "feedback_score",
    ]

    params: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentileParams

    type: Literal["percentile"]

    filter: Optional[str] = None


SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator: TypeAlias = Union[
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackCountMetric,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricCount,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartFeedbackScoreMetricPercentile,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumeratorCustomChartMetricPercentile,
]


class SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutput(BaseModel):
    denominator: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputDenominator

    numerator: SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutputNumerator

    type: Literal["ratio"]


SubSectionChartSeriesMetricDefinition: TypeAlias = Union[
    SubSectionChartSeriesMetricDefinitionCustomChartFeedbackCountMetric,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricCount,
    SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricScalar,
    SubSectionChartSeriesMetricDefinitionCustomChartFeedbackScoreMetricPercentile,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricPercentile,
    SubSectionChartSeriesMetricDefinitionCustomChartMetricRatioOutput,
    None,
]


class SubSectionChartSeries(BaseModel):
    id: str

    name: str

    feedback_key: Optional[str] = None

    filter_definition: Optional[SubSectionChartSeriesFilterDefinition] = None

    filters: Optional[SubSectionChartSeriesFilters] = None

    group_by: Optional[SubSectionChartSeriesGroupBy] = None
    """Include additional information about where the group_by param was set."""

    group_by_definitions: Optional[List[SubSectionChartSeriesGroupByDefinition]] = None

    metadata: Optional[Dict[str, object]] = None

    metric: Optional[
        Literal[
            "run_count",
            "latency_p50",
            "latency_p99",
            "latency_avg",
            "first_token_p50",
            "first_token_p99",
            "total_tokens",
            "prompt_tokens",
            "completion_tokens",
            "median_tokens",
            "completion_tokens_p50",
            "prompt_tokens_p50",
            "tokens_p99",
            "completion_tokens_p99",
            "prompt_tokens_p99",
            "feedback",
            "feedback_score_avg",
            "feedback_values",
            "total_cost",
            "prompt_cost",
            "completion_cost",
            "error_rate",
            "streaming_rate",
            "cost_p50",
            "cost_p99",
        ]
    ] = None
    """Metrics you can chart.

    Feedback metrics are not available for organization-scoped charts.
    """

    metric_definition: Optional[SubSectionChartSeriesMetricDefinition] = None

    project_metric: Optional[
        Literal[
            "memory_usage",
            "cpu_usage",
            "disk_usage",
            "restart_count",
            "replica_count",
            "worker_count",
            "lg_run_count",
            "responses_per_second",
            "error_responses_per_second",
            "p95_latency",
            "run_queue_wait_time",
        ]
    ] = None
    """LGP Metrics you can chart."""

    workspace_id: Optional[str] = None


class SubSectionChartCommonFilters(BaseModel):
    filter: Optional[str] = None

    session: Optional[List[str]] = None

    trace_filter: Optional[str] = None

    tree_filter: Optional[str] = None


class SubSectionChart(BaseModel):
    id: str

    chart_type: Literal["line", "bar", "table", "kpi", "top-k", "pie"]

    data: List[SubSectionChartData]

    index: int

    series: List[SubSectionChartSeries]

    title: str

    common_filters: Optional[SubSectionChartCommonFilters] = None

    description: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


class SubSection(BaseModel):
    id: str

    charts: List[SubSectionChart]

    index: int

    title: str

    description: Optional[str] = None


class CustomChartsSection(BaseModel):
    id: str

    charts: List[Chart]

    title: str

    description: Optional[str] = None

    index: Optional[int] = None

    layout: Optional[Layout] = None

    session_id: Optional[str] = None

    sub_sections: Optional[List[SubSection]] = None
