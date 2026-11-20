# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .workspace_tags.keys.tag_value import TagValue

__all__ = ["TagKeyWithValues"]


class TagKeyWithValues(BaseModel):
    id: str

    created_at: datetime

    key: str

    updated_at: datetime

    values: List[TagValue]

    description: Optional[str] = None
