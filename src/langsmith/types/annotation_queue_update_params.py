# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .annotation_queue_rubric_item_schema_param import AnnotationQueueRubricItemSchemaParam

__all__ = ["AnnotationQueueUpdateParams"]


class AnnotationQueueUpdateParams(TypedDict, total=False):
    default_dataset: Optional[str]
    """Dataset that reviewed runs are added to by default."""

    description: Optional[str]
    """New description."""

    enable_reservations: bool
    """Whether a reviewer reserves a run while reviewing it, so others skip it."""

    metadata: Optional[Dict[str, object]]
    """Metadata to store on the queue. Replaces the existing metadata."""

    name: Optional[str]
    """New name for the queue."""

    num_reviewers_per_item: Optional[int]
    """How many reviewers must review each run."""

    reservation_minutes: Optional[int]
    """How long a reservation lasts, in minutes."""

    reviewer_access_mode: Optional[Literal["any", "assigned"]]
    """
    Who completes a run: any (one reviewer is enough) or assigned (every assigned
    reviewer must submit).
    """

    rubric_instructions: Optional[str]
    """Instructions shown to reviewers."""

    rubric_items: Optional[Iterable[AnnotationQueueRubricItemSchemaParam]]
    """Feedback keys reviewers fill in for each run."""
