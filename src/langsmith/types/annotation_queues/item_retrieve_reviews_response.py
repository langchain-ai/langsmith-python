# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .annotation_queue_item_key_reviews import AnnotationQueueItemKeyReviews

__all__ = ["ItemRetrieveReviewsResponse", "Reviewer"]


class Reviewer(BaseModel):
    completed_at: Optional[datetime] = None

    email: Optional[str] = None

    identity_id: Optional[str] = None

    ls_user_id: Optional[str] = None

    name: Optional[str] = None


class ItemRetrieveReviewsResponse(BaseModel):
    keys: Optional[List[AnnotationQueueItemKeyReviews]] = None

    reviewers: Optional[List[Reviewer]] = None
