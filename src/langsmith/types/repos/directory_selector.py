# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["DirectorySelector", "DirectoryLatestSelector", "DirectoryCommitSelector"]


class DirectoryLatestSelector(BaseModel):
    type: Literal["LATEST"]


class DirectoryCommitSelector(BaseModel):
    commit_id: str

    type: Literal["COMMIT"]


DirectorySelector: TypeAlias = Annotated[
    Union[DirectoryLatestSelector, DirectoryCommitSelector], PropertyInfo(discriminator="type")
]
