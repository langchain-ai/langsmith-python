# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..thread import Thread
from ..._models import BaseModel

__all__ = ["StreamingQueryResponse"]


class StreamingQueryResponse(BaseModel):
    items: Optional[List[Thread]] = None
    """
    `items` is the page of thread summaries, sorted by the thread's most recent
    activity.
    """

    next_cursor: Optional[str] = None
    """`next_cursor` is the opaque cursor to pass as `cursor` on the next request.

    Null on the final page.
    """
