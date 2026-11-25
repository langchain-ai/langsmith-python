# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCreateParams"]


class VolumeCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the volume, unique within the workspace."""

    size_bytes: Required[int]
    """Capacity in bytes, rounded up to a whole GiB."""

    description: str
    """Free-text description, at most 1024 characters."""

    labels: Dict[str, str]
    """Labels to filter and identify the volume by.

    Keys are lowercase letters, digits, dots and hyphens.
    """
