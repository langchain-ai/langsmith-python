# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkspaceSecret", "Config"]


class Config(BaseModel):
    host_pattern: str
    """Exact host or a leading '\\**.' wildcard, e.g. 'api.openai.com'."""

    source: Literal["DEFAULT", "CUSTOM"]
    """DEFAULT for a built-in provider host, CUSTOM for one an admin set."""

    id: Optional[str] = None
    """Omitted for a built-in default."""

    created_at: Optional[datetime] = None
    """Omitted for a built-in default."""

    header_name: Optional[str] = None
    """HTTP header the secret is sent in. Null leaves it to the consumer."""

    header_value_template: Optional[str] = None
    """Header value with '{value}' replaced by the secret, e.g.

    'Bearer {value}'. Null sends the raw secret.
    """

    updated_at: Optional[datetime] = None
    """Omitted for a built-in default."""


class WorkspaceSecret(BaseModel):
    """A workspace secret's key and the hosts it may be sent to. Never the value."""

    key: str
    """Secret name, e.g. OPENAI_API_KEY."""

    configs: Optional[List[Config]] = None
    """Hosts the secret may be sent to, with built-in defaults applied.

    Listed secrets include it only when include_configs is true.
    """
