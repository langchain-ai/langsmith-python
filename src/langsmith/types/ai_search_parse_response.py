# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AISearchParseResponse", "Clarification", "ClarificationOption"]


class ClarificationOption(BaseModel):
    filter: Optional[str] = None
    """Filter expression for the query API's filter parameter.

    Omitted when there is none.
    """

    label: Optional[str] = None
    """Short description of this interpretation to show the user."""

    max_start_time: Optional[datetime] = None
    """
    Upper bound on start time (RFC 3339, UTC) for the query API's max_start_time
    parameter. Omitted when the search names no end; keep your own time range.
    """

    min_start_time: Optional[datetime] = None
    """
    Lower bound on start time (RFC 3339, UTC) for the query API's min_start_time
    parameter. Omitted when the search names no start; keep your own time range.
    """

    scope: Optional[Literal["runs", "traces", "threads"]] = None
    """Query API this interpretation is planned for."""

    sem_filter: Optional[str] = None
    """
    Plain-language criterion for the query API's sem_filter parameter, matched
    against conversation messages. Null when the search has no conversational
    criterion.
    """

    thread_filter: Optional[str] = None
    """Filter expression for the threads query API's thread_filter parameter.

    Omitted when there is none.
    """

    trace_filter: Optional[str] = None
    """Filter expression for the query API's trace_filter parameter.

    Omitted when there is none.
    """

    tree_filter: Optional[str] = None
    """Filter expression for the query API's tree_filter parameter.

    Omitted when there is none.
    """


class Clarification(BaseModel):
    """Interpretations to choose from.

    Returned only when allow_clarification is true and the search is ambiguous; no other fields are set.
    """

    options: Optional[List[ClarificationOption]] = None
    """Two or three interpretations of the search."""


class AISearchParseResponse(BaseModel):
    clarification: Optional[Clarification] = None
    """Interpretations to choose from.

    Returned only when allow_clarification is true and the search is ambiguous; no
    other fields are set.
    """

    filter: Optional[str] = None
    """Filter expression for the query API's filter parameter.

    Omitted when there is none.
    """

    max_start_time: Optional[datetime] = None
    """
    Upper bound on start time (RFC 3339, UTC) for the query API's max_start_time
    parameter. Omitted when the search names no end; keep your own time range.
    """

    min_start_time: Optional[datetime] = None
    """
    Lower bound on start time (RFC 3339, UTC) for the query API's min_start_time
    parameter. Omitted when the search names no start; keep your own time range.
    """

    scope: Optional[Literal["runs", "traces", "threads"]] = None
    """Query API to send the plan to: runs, traces or threads."""

    sem_filter: Optional[str] = None
    """
    Plain-language criterion for the query API's sem_filter parameter, matched
    against conversation messages. Null when the search has no conversational
    criterion.
    """

    thread_filter: Optional[str] = None
    """Filter expression for the threads query API's thread_filter parameter.

    Omitted when there is none.
    """

    trace_filter: Optional[str] = None
    """Filter expression for the query API's trace_filter parameter.

    Omitted when there is none.
    """

    tree_filter: Optional[str] = None
    """Filter expression for the query API's tree_filter parameter.

    Omitted when there is none.
    """
