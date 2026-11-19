# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ItemSetFinalResponse", "Answer", "Final"]


class Answer(BaseModel):
    score: Optional[float] = None

    scores: Optional[List[float]] = None

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Final(BaseModel):
    score: Optional[float] = None

    scores: Optional[List[float]] = None

    value: Optional[str] = None

    values: Optional[List[str]] = None


class ItemSetFinalResponse(BaseModel):
    answer: Optional[Answer] = None

    final: Optional[Final] = None

    final_set_at: Optional[datetime] = None

    final_set_by: Optional[str] = None

    has_final: Optional[bool] = None

    key: Optional[str] = None

    state: Optional[Literal["agreed", "disagreed", "none"]] = None
