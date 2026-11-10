# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .commit_manifest_response import CommitManifestResponse

__all__ = ["RepoWithLookups", "Owner"]


class Owner(BaseModel):
    """A repo owner with user details.

    Note: identity_id and email may be None when returned to users
    outside the repo's tenant (PII protection).
    """

    created_at: datetime

    email: Optional[str] = None

    full_name: Optional[str] = None

    identity_id: Optional[str] = None

    ls_user_id: str


class RepoWithLookups(BaseModel):
    """All database fields for repos, plus helpful computed fields."""

    id: str

    created_at: datetime

    full_name: str

    is_archived: bool

    is_public: bool

    num_commits: int

    num_downloads: int

    num_likes: int

    num_views: int

    owner: Optional[str] = None

    repo_handle: str

    repo_type: Literal["prompt", "file", "agent", "skill"]

    tags: List[str]

    tenant_id: str

    updated_at: datetime

    commit_tags: Optional[List[str]] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    last_commit_hash: Optional[str] = None

    latest_commit_manifest: Optional[CommitManifestResponse] = None
    """Response model for get_commit_manifest."""

    liked_by_auth_user: Optional[bool] = None

    original_repo_full_name: Optional[str] = None

    original_repo_id: Optional[str] = None

    owners: Optional[List[Owner]] = None

    readme: Optional[str] = None

    restricted_mode: Optional[bool] = None

    source: Optional[Literal["internal", "external"]] = None

    upstream_repo_full_name: Optional[str] = None

    upstream_repo_id: Optional[str] = None
