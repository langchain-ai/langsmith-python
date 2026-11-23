# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ReviewerListResponse"]


class ReviewerListResponse(BaseModel):
    completed_count: Optional[int] = None

    email: Optional[str] = None

    identity_id: Optional[str] = None

    is_on_roster: Optional[bool] = None

    last_active_at: Optional[datetime] = None

    name: Optional[str] = None

    pending_count: Optional[int] = None
