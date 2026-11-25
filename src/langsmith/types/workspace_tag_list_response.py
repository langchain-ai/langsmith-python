# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tag_key_with_values import TagKeyWithValues

__all__ = ["WorkspaceTagListResponse"]

WorkspaceTagListResponse: TypeAlias = List[TagKeyWithValues]
