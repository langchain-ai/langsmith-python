# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BoxBatchDeleteResponse", "Skipped"]


class Skipped(BaseModel):
    name: Optional[str] = None

    reason: Optional[str] = None


class BoxBatchDeleteResponse(BaseModel):
    deleted: Optional[List[str]] = None

    skipped: Optional[List[Skipped]] = None
