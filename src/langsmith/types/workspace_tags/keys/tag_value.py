# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TagValue"]


class TagValue(BaseModel):
    id: str

    created_at: datetime

    tag_key_id: str

    updated_at: datetime

    value: str

    description: Optional[str] = None
