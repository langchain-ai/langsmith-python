# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExampleUpdateMetadataResponse", "Status"]


class Status(BaseModel):
    id: str
    """The example ID, as submitted."""

    status: Literal["UPDATED", "NOT_FOUND"]
    """
    UPDATED if the example's metadata was changed; NOT_FOUND if the example is not
    in the dataset or was deleted.
    """

    description: Optional[str] = None
    """Why the example was not updated. Omitted when it was."""


class ExampleUpdateMetadataResponse(BaseModel):
    statuses: List[Status]
    """One entry per submitted example ID, in request order."""
