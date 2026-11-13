# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .workspace_secret import WorkspaceSecret

__all__ = ["WorkspaceSecretListResponse"]

WorkspaceSecretListResponse: TypeAlias = List[WorkspaceSecret]
