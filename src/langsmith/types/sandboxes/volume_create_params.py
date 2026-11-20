# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCreateParams"]


class VolumeCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name is unique within the workspace."""

    size_bytes: Required[int]
    """SizeBytes is the volume's capacity, rounded up to a whole GiB."""

    description: str

    labels: Dict[str, str]
