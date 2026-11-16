# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .commit_with_lookups import CommitWithLookups

__all__ = ["CommitCreateResponse"]


class CommitCreateResponse(BaseModel):
    commit: Optional[CommitWithLookups] = None
