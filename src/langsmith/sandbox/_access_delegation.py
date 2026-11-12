"""Delegated LangSmith access for sandboxes."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal, TypedDict

AccessDelegationMode = Literal["EXPLICIT"]


class AccessDelegation(TypedDict, total=False):
    """Grant letting code inside a sandbox call the LangSmith API as the creator.

    ``mode`` is ``"EXPLICIT"`` and ``permissions`` names what is granted.
    Permissions are a ceiling re-checked on every request rather than a
    snapshot, so access the creator loses is lost here too.
    """

    mode: AccessDelegationMode
    permissions: list[str]


def _validate_access_delegation(value: Any) -> AccessDelegation:
    """Reject grants the server would refuse, without the round trip."""
    if not isinstance(value, dict):
        raise ValueError("access_delegation must be a mapping")

    mode = value.get("mode")
    if mode != "EXPLICIT":
        raise ValueError('access_delegation["mode"] must be "EXPLICIT"')

    permissions = value.get("permissions")
    if permissions is not None and (isinstance(permissions, str) or not isinstance(permissions, Sequence)):
        raise ValueError('access_delegation["permissions"] must be a list of strings')

    if not permissions:
        raise ValueError('access_delegation["permissions"] is required')
    return {"mode": "EXPLICIT", "permissions": list(permissions)}


def _access_delegation_from_dict(value: Any) -> AccessDelegation | None:
    if not isinstance(value, dict):
        return None
    permissions = value.get("permissions")
    if value.get("mode") != "EXPLICIT" or not permissions:
        return None
    return {"mode": "EXPLICIT", "permissions": list(permissions)}
