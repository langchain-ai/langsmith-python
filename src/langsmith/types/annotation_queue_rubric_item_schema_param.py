# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .missing_param import MissingParam

__all__ = [
    "AnnotationQueueRubricItemSchemaParam",
    "FeedbackConfig",
    "FeedbackConfigFeedbackConfig",
    "FeedbackConfigFeedbackConfigCategory",
    "RegexValidator",
    "RequiredIf",
    "RequiredIfRule",
    "VisibleIf",
    "VisibleIfRule",
]


class FeedbackConfigFeedbackConfigCategory(TypedDict, total=False):
    """Specific value and label pair for feedback"""

    value: Required[float]

    label: Optional[str]


class FeedbackConfigFeedbackConfig(TypedDict, total=False):
    type: Required[Literal["continuous", "categorical", "freeform"]]
    """Enum for feedback types."""

    allows_multiple_categories: bool
    """Whether a reviewer can pick several categories. Categorical feedback only."""

    categories: Optional[Iterable[FeedbackConfigFeedbackConfigCategory]]

    max: Optional[float]

    min: Optional[float]


class FeedbackConfig(TypedDict, total=False):
    id: Required[str]

    feedback_config: Required[FeedbackConfigFeedbackConfig]

    feedback_key: Required[str]

    modified_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    tenant_id: Required[str]

    is_deleted: bool

    is_enforced: bool

    is_first: bool

    is_lower_score_better: Optional[bool]


RegexValidator: TypeAlias = Union[str, MissingParam]


class RequiredIfRule(TypedDict, total=False):
    key: Required[str]

    op: Required[Literal["is", "is_one_of", "is_empty", "is_not_empty"]]

    values: Iterable[float]


class RequiredIf(TypedDict, total=False):
    join: Required[Literal["all", "any"]]

    rules: Required[Iterable[RequiredIfRule]]


class VisibleIfRule(TypedDict, total=False):
    key: Required[str]

    op: Required[Literal["is", "is_one_of", "is_empty", "is_not_empty"]]

    values: Iterable[float]


class VisibleIf(TypedDict, total=False):
    join: Required[Literal["all", "any"]]

    rules: Required[Iterable[VisibleIfRule]]


class AnnotationQueueRubricItemSchemaParam(TypedDict, total=False):
    feedback_key: Required[str]

    description: Optional[str]

    feedback_config: Optional[FeedbackConfig]

    feedback_config_id: Optional[str]

    is_assertion: Optional[bool]

    is_required: Optional[bool]

    regex_validator: Optional[RegexValidator]

    required_if: Optional[RequiredIf]

    score_descriptions: Optional[Dict[str, str]]

    value_descriptions: Optional[Dict[str, str]]

    visible_if: Optional[VisibleIf]
