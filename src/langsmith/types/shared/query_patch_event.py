# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .query_patch_operation import QueryPatchOperation

__all__ = ["QueryPatchEvent"]

QueryPatchEvent: TypeAlias = List[QueryPatchOperation]
