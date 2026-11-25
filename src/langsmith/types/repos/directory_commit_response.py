# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DirectoryCommitResponse", "Commit"]


class Commit(BaseModel):
    id: Optional[str] = None

    commit_hash: Optional[str] = None

    created_at: Optional[str] = None


class DirectoryCommitResponse(BaseModel):
    commit: Optional[Commit] = None
