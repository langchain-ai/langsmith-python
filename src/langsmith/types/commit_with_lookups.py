# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CommitWithLookups"]


class CommitWithLookups(BaseModel):
    id: Optional[str] = None
    """The commit ID"""

    commit_hash: Optional[str] = None
    """The hash of the commit"""

    created_at: Optional[datetime] = None
    """When the commit was created"""

    description: Optional[str] = None
    """Optional human-readable description for the commit"""

    example_run_ids: Optional[List[str]] = None
    """Example run IDs associated with the commit"""

    full_name: Optional[str] = None
    """Author's full name"""

    manifest: Optional[object] = None
    """The manifest of the commit"""

    manifest_sha: Optional[str] = None
    """The base64-encoded SHA-256 of the manifest"""

    num_downloads: Optional[int] = None
    """Number of API downloads"""

    num_views: Optional[int] = None
    """Number of web views"""

    parent_commit_hash: Optional[str] = None
    """The hash of the parent commit"""

    parent_id: Optional[str] = None
    """The ID of the parent commit"""

    repo_id: Optional[str] = None
    """Repository ID"""

    updated_at: Optional[datetime] = None
    """When the commit was last updated"""
