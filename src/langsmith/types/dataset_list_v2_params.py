# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .data_type import DataType
from .sort_by_dataset_column import SortByDatasetColumn

__all__ = ["DatasetListV2Params"]


class DatasetListV2Params(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Return only the datasets with these IDs. Repeat the parameter for several IDs."""

    cursor: str
    """The next_cursor of the previous response. Omit it for the first page."""

    data_type: List[DataType]
    """Return only datasets of these data types.

    Repeat the parameter for several types.
    """

    exclude: List[Literal["example_count"]]
    """Fields to leave out of each dataset.

    An excluded example_count is returned as null and makes the response faster.
    """

    exclude_corrections_datasets: bool
    """Leave out datasets that store corrections for an evaluator."""

    metadata: str
    """A JSON object.

    Return only datasets whose metadata contains every key and value in it.
    """

    name: str
    """Return only the dataset with exactly this name."""

    name_contains: str
    """Return only datasets whose name contains this text, ignoring case."""

    page_size: int
    """Maximum number of datasets to return."""

    sort_by: SortByDatasetColumn
    """Field to sort by.

    last_session_start_time is the start time of the most recent experiment on the
    dataset. Datasets without a value come last in both orders. While a sort value
    changes, for example when an experiment starts, a dataset can be skipped or
    listed twice across pages. Sort by created_at for a stable walk.
    """

    sort_order: Literal["asc", "desc"]
    """Sort direction."""

    tag_value_id: SequenceNotStr[str]
    """Return only datasets tagged with all of these tag value IDs."""
