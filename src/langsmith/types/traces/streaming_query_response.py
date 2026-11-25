# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..trace import Trace
from ..._models import BaseModel

__all__ = ["StreamingQueryResponse"]


class StreamingQueryResponse(BaseModel):
    items: Optional[List[Trace]] = None
    """`items` is the page of traces."""

    next_cursor: Optional[str] = None
    """`next_cursor` is the opaque cursor for the next page. Null on the final page."""
