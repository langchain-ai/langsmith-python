# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AnnotationQueuePopulateParams"]


class AnnotationQueuePopulateParams(TypedDict, total=False):
    queue_id: Required[str]
    """ID of the annotation queue to add runs to."""

    session_ids: Required[SequenceNotStr[str]]
    """Experiments whose runs are added to the queue.

    Each must be an experiment on a dataset.
    """

    extend_trace_retention: bool
    """Upgrade the added traces from short-lived to extended retention."""
