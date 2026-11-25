# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ExampleUpdateMetadataParams", "Operation"]


class ExampleUpdateMetadataParams(TypedDict, total=False):
    example_ids: Required[SequenceNotStr[str]]
    """The IDs of the examples to change; at most 10000.

    IDs of examples that are not in the dataset, or were deleted, are skipped and
    reported as NOT_FOUND.
    """

    operations: Required[Iterable[Operation]]
    """
    The metadata changes to apply, in order; at most 50, of which at most 10 are
    array operations.
    """


class Operation(TypedDict, total=False):
    key: Required[str]
    """The top-level metadata key to change, at most 255 bytes.

    Use dataset_split with ARRAY_ADD or ARRAY_REMOVE to change which splits the
    examples belong to.
    """

    operation: Required[Literal["SET", "ARRAY_ADD", "ARRAY_REMOVE"]]
    """
    The change to make: SET replaces the value at key; ARRAY_ADD adds values to the
    list at key; ARRAY_REMOVE removes values from it. For array operations, a
    missing or non-list value starts as an empty list, except for dataset_split,
    where it starts as the base split.
    """

    value: object
    """The new value for a SET operation; any JSON value, at most 64 KB.

    Ignored by array operations.
    """

    values: SequenceNotStr[str]
    """
    The values to add or remove for an array operation; at most 1000 values of at
    most 255 bytes each. Ignored by SET.
    """
