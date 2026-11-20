# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCloneParams"]


class VolumeCloneParams(TypedDict, total=False):
    name: Required[str]
    """Name of the new volume, unique within the workspace."""

    description: str

    labels: Dict[str, str]
