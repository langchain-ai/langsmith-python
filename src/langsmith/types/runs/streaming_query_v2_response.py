# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..run import Run
from ..._models import BaseModel

__all__ = ["StreamingQueryV2Response"]


class StreamingQueryV2Response(BaseModel):
    items: Optional[List[Run]] = None
    """`items` is the page of runs, sorted by `start_time` descending."""

    next_cursor: Optional[str] = None
    """`next_cursor` is the opaque cursor to pass as `cursor` on the next request.

    Null on the final page.
    """
