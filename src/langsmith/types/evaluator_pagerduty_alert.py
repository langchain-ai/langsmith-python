# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EvaluatorPagerdutyAlert"]


class EvaluatorPagerdutyAlert(BaseModel):
    routing_key: str

    severity: Optional[Literal["critical", "warning", "error", "info"]] = None
    """Enum for severity."""

    summary: Optional[str] = None

    type: Optional[Literal["pagerduty"]] = None
    """Enum for alert types."""
