# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SqlQueryResponse", "Column"]


class Column(BaseModel):
    data_type: Optional[
        Literal[
            "uuid", "string", "integer", "float", "boolean", "timestamp", "date", "binary", "list", "object", "null"
        ]
    ] = None
    """
    DataType is how the column's values are encoded in JSON: uuid, string, integer,
    float, boolean, timestamp and date (RFC 3339 strings), binary (base64 strings),
    list, object or null. Float values JSON cannot represent are the strings "NaN",
    "Infinity" and "-Infinity".
    """

    name: Optional[str] = None


class SqlQueryResponse(BaseModel):
    columns: Optional[List[Column]] = None

    execution_time_ms: Optional[float] = None

    is_truncated: Optional[bool] = None
    """IsTruncated reports that the query matched rows not included in Rows."""

    row_count: Optional[int] = None

    rows: Optional[List[List[object]]] = None
    """
    Rows holds at most the configured row limit (1000 by default), each ordered like
    Columns.
    """

    truncation_reason: Optional[Literal["row_limit", "size_limit"]] = None
    """
    TruncationReason is "row_limit" when the query matched more rows than the row
    limit, "size_limit" when the rows past about 10 MB were left out, or null.
    """

    warnings: Optional[List[str]] = None
    """Warnings contains query planning warnings. Empty when there are no warnings."""
