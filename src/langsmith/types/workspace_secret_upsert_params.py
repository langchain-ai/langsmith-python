# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceSecretUpsertParams", "Config"]


class WorkspaceSecretUpsertParams(TypedDict, total=False):
    configs: Optional[Iterable[Config]]
    """Full replacement of the allowed hosts.

    Omitted or empty removes custom hosts so the built-in defaults, if any, apply.
    """

    value: Optional[str]
    """Secret value. Required to create a secret; omit to keep the current value."""


class Config(TypedDict, total=False):
    """A host a workspace secret may be sent to, and how it is sent."""

    host_pattern: Required[str]
    """Exact host or a leading '\\**.' wildcard, e.g. 'api.openai.com'."""

    header_name: Optional[str]
    """HTTP header the secret is sent in. Null leaves it to the consumer."""

    header_value_template: Optional[str]
    """Header value with '{value}' replaced by the secret, e.g.

    'Bearer {value}'. Null sends the raw secret.
    """
