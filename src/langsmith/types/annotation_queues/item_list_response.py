# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .annotation_queue_item_answer import AnnotationQueueItemAnswer
from .annotation_queue_item_agreement_state import AnnotationQueueItemAgreementState

__all__ = ["ItemListResponse", "KeyAgreements"]


class KeyAgreements(BaseModel):
    answer: Optional[AnnotationQueueItemAnswer] = None

    has_final: Optional[bool] = None

    state: Optional[AnnotationQueueItemAgreementState] = None


class ItemListResponse(BaseModel):
    id: Optional[str] = None

    added_at: Optional[str] = None

    agreement_state: Optional[AnnotationQueueItemAgreementState] = None
    """Whether the item's reviewers agreed across its rubric keys."""

    assigned_to: Optional[List[str]] = None

    completed_by: Optional[List[str]] = None

    effective_added_at: Optional[str] = None

    has_unresolved_keys: Optional[bool] = None
    """True while a key the reviewers disagreed on has no final answer."""

    item_type: Optional[Literal["RUN", "THREAD"]] = None

    key_agreements: Optional[Dict[str, KeyAgreements]] = None
    """The reviewers' result for each rubric key."""

    last_reviewed_time: Optional[str] = None
    """LastReviewedTime is always present on the wire (null until reviewed)."""

    project_id: Optional[str] = None

    queue_id: Optional[str] = None

    reserved_by: Optional[List[str]] = None

    run_id: Optional[str] = None

    source_proposed_example_id: Optional[str] = None

    start_time: Optional[str] = None

    thread_id: Optional[str] = None
