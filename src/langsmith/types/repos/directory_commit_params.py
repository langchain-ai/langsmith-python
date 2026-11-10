# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .file_entry_param import FileEntryParam
from .directory_selector_param import DirectorySelectorParam

__all__ = ["DirectoryCommitParams", "Files", "FilesDirectoryAgentEntryInput", "FilesDirectorySkillEntryInput"]


class DirectoryCommitParams(TypedDict, total=False):
    owner: Required[str]

    files: Dict[str, Optional[Files]]
    """Paths to create, update, link, delete, or unlink.

    Use null to delete or unlink an existing path.
    """

    parent_commit: str

    skip_webhooks: bool
    """SkipWebhooks suppresses Context Hub commit webhooks for this commit."""


class FilesDirectoryAgentEntryInput(TypedDict, total=False):
    repo_handle: Required[str]

    type: Required[Literal["agent"]]

    commit_id: str
    """Deprecated write input.

    It is accepted for compatibility but ignored for selection, so the link resolves
    as LATEST. Omit it for LATEST or replace it with selector {"type": "COMMIT",
    "commit_id": "<uuid>"} to pin a commit. commit_id and selector are mutually
    exclusive.
    """

    selector: DirectorySelectorParam
    """How to select the linked commit. Omit this field to use LATEST."""


class FilesDirectorySkillEntryInput(TypedDict, total=False):
    repo_handle: Required[str]

    type: Required[Literal["skill"]]

    commit_id: str
    """Deprecated write input.

    It is accepted for compatibility but ignored for selection, so the link resolves
    as LATEST. Omit it for LATEST or replace it with selector {"type": "COMMIT",
    "commit_id": "<uuid>"} to pin a commit. commit_id and selector are mutually
    exclusive.
    """

    selector: DirectorySelectorParam
    """How to select the linked commit. Omit this field to use LATEST."""


Files: TypeAlias = Union[FileEntryParam, FilesDirectoryAgentEntryInput, FilesDirectorySkillEntryInput]
