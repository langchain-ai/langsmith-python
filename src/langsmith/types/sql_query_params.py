# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SqlQueryParams"]


class SqlQueryParams(TypedDict, total=False):
    project_ids: Required[SequenceNotStr[str]]
    """ProjectIDs are the tracing projects the query can read."""

    query: Required[str]
    """Query is a single read-only SQL statement.

    Queries over runs need a start_time lower bound.
    """
