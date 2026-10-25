# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Agent", "Environment", "EnvironmentRuntimeBinding"]


class EnvironmentRuntimeBinding(BaseModel):
    id: str

    agent_environment_id: str

    source_id: str


class Environment(BaseModel):
    id: str

    agent_id: str

    environment: Literal["LOCAL", "DEVELOPMENT", "STAGING", "PRODUCTION"]

    tracer_session_id: str

    tracer_session_name: str

    runtime_bindings: Optional[List[EnvironmentRuntimeBinding]] = None


class Agent(BaseModel):
    id: str

    agent_type: Literal["CUSTOM", "CODING"]

    created_at: datetime

    environments: List[Environment]

    name: str

    source_type: Literal["LSD", "MDA", "EXTERNAL", "FLEET"]

    owner: Optional[str] = None
    """Owner is the owner's full name, falling back to email when available."""

    owner_id: Optional[str] = None

    tag_key_id: Optional[str] = None

    tag_value_id: Optional[str] = None
