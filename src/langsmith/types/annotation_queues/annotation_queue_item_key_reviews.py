# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .annotation_queue_item_answer import AnnotationQueueItemAnswer
from .annotation_queue_item_agreement_state import AnnotationQueueItemAgreementState

__all__ = ["AnnotationQueueItemKeyReviews", "Review"]


class Review(BaseModel):
    answer: Optional[AnnotationQueueItemAnswer] = None

    ls_user_id: Optional[str] = None


class AnnotationQueueItemKeyReviews(BaseModel):
    answer: Optional[AnnotationQueueItemAnswer] = None

    final: Optional[AnnotationQueueItemAnswer] = None

    final_set_at: Optional[datetime] = None

    final_set_by: Optional[str] = None

    has_final: Optional[bool] = None

    key: Optional[str] = None

    reviews: Optional[List[Review]] = None

    state: Optional[AnnotationQueueItemAgreementState] = None
