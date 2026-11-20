# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AnnotationQueueItemAnswer"]


class AnnotationQueueItemAnswer(BaseModel):
    score: Optional[float] = None

    scores: Optional[List[float]] = None

    value: Optional[str] = None

    values: Optional[List[str]] = None
