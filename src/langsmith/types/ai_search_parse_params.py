# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AISearchParseParams"]


class AISearchParseParams(TypedDict, total=False):
    ai_search: Required[str]
    """
    Natural-language description of the runs, traces or threads to find, at most
    2000 UTF-8 bytes.
    """

    project_ids: Required[SequenceNotStr[str]]
    """Tracing project UUIDs used to interpret the search.

    Send the same projects to the query API.
    """

    allow_clarification: bool
    """
    When true, an ambiguous search returns clarification options instead of a single
    plan. Defaults to false.
    """

    scope: Literal["runs", "traces", "threads"]
    """Query API to plan for: runs, traces or threads.

    When omitted, it is inferred from the search and defaults to traces.
    """
