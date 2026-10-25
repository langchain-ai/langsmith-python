# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .registry_response import RegistryResponse

__all__ = ["RegistryListResponse"]


class RegistryListResponse(BaseModel):
    items: Optional[List[RegistryResponse]] = None

    next_cursor: Optional[str] = None

    offset: Optional[int] = None
    """Deprecated: only applies to limit/offset requests.

    Use next_cursor when paging with a cursor.
    """

    registries: Optional[List[RegistryResponse]] = None
    """Deprecated: use items."""
