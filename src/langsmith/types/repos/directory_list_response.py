# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .file_entry import FileEntry
from .directory_selector import DirectorySelector

__all__ = ["DirectoryListResponse", "Files", "FilesDirectoryAgentEntryOutput", "FilesDirectorySkillEntryOutput"]


class FilesDirectoryAgentEntryOutput(BaseModel):
    commit_hash: str

    owner: str

    repo_handle: str

    type: Literal["agent"]

    selector: Optional[DirectorySelector] = None
    """The authored selection policy for this linked directory."""


class FilesDirectorySkillEntryOutput(BaseModel):
    commit_hash: str

    owner: str

    repo_handle: str

    type: Literal["skill"]

    selector: Optional[DirectorySelector] = None
    """The authored selection policy for this linked directory."""


Files: TypeAlias = Annotated[
    Union[FileEntry, FilesDirectoryAgentEntryOutput, FilesDirectorySkillEntryOutput], PropertyInfo(discriminator="type")
]


class DirectoryListResponse(BaseModel):
    commit_hash: str

    commit_id: str

    files: Dict[str, Files]
