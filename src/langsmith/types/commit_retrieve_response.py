# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CommitRetrieveResponse", "Example"]


class Example(BaseModel):
    id: Optional[str] = None

    inputs: Optional[object] = None

    outputs: Optional[object] = None

    session_id: Optional[str] = None

    start_time: Optional[str] = None


class CommitRetrieveResponse(BaseModel):
    commit_hash: Optional[str] = None

    description: Optional[str] = None

    examples: Optional[List[Example]] = None

    is_draft: Optional[bool] = None

    manifest: Optional[object] = None

    api_model_config: Optional[object] = FieldInfo(alias="model_config", default=None)

    api_model_provider: Optional[str] = FieldInfo(alias="model_provider", default=None)
