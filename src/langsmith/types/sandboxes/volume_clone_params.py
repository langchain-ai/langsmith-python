# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCloneParams"]


class VolumeCloneParams(TypedDict, total=False):
    name: Required[str]
    """Name of the new volume, unique within the workspace."""

    description: str
    """Free-text description of the new volume, at most 1024 characters."""

    labels: Dict[str, str]
    """Labels for the new volume.

    Keys are lowercase letters, digits, dots and hyphens.
    """
