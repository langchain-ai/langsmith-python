# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DirectorySelectorParam", "DirectoryLatestSelector", "DirectoryCommitSelector"]


class DirectoryLatestSelector(TypedDict, total=False):
    type: Required[Literal["LATEST"]]


class DirectoryCommitSelector(TypedDict, total=False):
    commit_id: Required[str]

    type: Required[Literal["COMMIT"]]


DirectorySelectorParam: TypeAlias = Union[DirectoryLatestSelector, DirectoryCommitSelector]
