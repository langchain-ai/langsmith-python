# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ...types import SortByDatasetColumn, dataset_list_v2_params
from ..._httpx import httpx
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from .examples import (
    ExamplesResource,
    AsyncExamplesResource,
    ExamplesResourceWithRawResponse,
    AsyncExamplesResourceWithRawResponse,
    ExamplesResourceWithStreamingResponse,
    AsyncExamplesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dataset import Dataset
from .experiment_runs import (
    ExperimentRunsResource,
    AsyncExperimentRunsResource,
    ExperimentRunsResourceWithRawResponse,
    AsyncExperimentRunsResourceWithRawResponse,
    ExperimentRunsResourceWithStreamingResponse,
    AsyncExperimentRunsResourceWithStreamingResponse,
)
from ...types.data_type import DataType
from ...types.sort_by_dataset_column import SortByDatasetColumn

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def examples(self) -> ExamplesResource:
        return ExamplesResource(self._client)

    @cached_property
    def experiment_runs(self) -> ExperimentRunsResource:
        return ExperimentRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        data_type: List[DataType] | Omit = omit,
        exclude: List[Literal["example_count"]] | Omit = omit,
        exclude_corrections_datasets: bool | Omit = omit,
        metadata: str | Omit = omit,
        name: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: SortByDatasetColumn | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[Dataset]:
        """
        Returns one page of the datasets in the workspace, filtered and sorted by the
        query parameters. Pass the next_cursor of a response as cursor, with the same
        filters and sort, to get the next page. next_cursor is null on the last page.

        Args:
          id: Return only the datasets with these IDs. Repeat the parameter for several IDs.

          cursor: The next_cursor of the previous response. Omit it for the first page.

          data_type: Return only datasets of these data types. Repeat the parameter for several
              types.

          exclude: Fields to leave out of each dataset. An excluded example_count is returned as
              null and makes the response faster.

          exclude_corrections_datasets: Leave out datasets that store corrections for an evaluator.

          metadata: A JSON object. Return only datasets whose metadata contains every key and value
              in it.

          name: Return only the dataset with exactly this name.

          name_contains: Return only datasets whose name contains this text, ignoring case.

          page_size: Maximum number of datasets to return.

          sort_by: Field to sort by. last_session_start_time is the start time of the most recent
              experiment on the dataset. Datasets without a value come last in both orders.
              While a sort value changes, for example when an experiment starts, a dataset can
              be skipped or listed twice across pages. Sort by created_at for a stable walk.

          sort_order: Sort direction.

          tag_value_id: Return only datasets tagged with all of these tag value IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/datasets",
            page=SyncItemsCursorGetPagination[Dataset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "data_type": data_type,
                        "exclude": exclude,
                        "exclude_corrections_datasets": exclude_corrections_datasets,
                        "metadata": metadata,
                        "name": name,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "tag_value_id": tag_value_id,
                    },
                    dataset_list_v2_params.DatasetListV2Params,
                ),
            ),
            model=Dataset,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def examples(self) -> AsyncExamplesResource:
        return AsyncExamplesResource(self._client)

    @cached_property
    def experiment_runs(self) -> AsyncExperimentRunsResource:
        return AsyncExperimentRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        data_type: List[DataType] | Omit = omit,
        exclude: List[Literal["example_count"]] | Omit = omit,
        exclude_corrections_datasets: bool | Omit = omit,
        metadata: str | Omit = omit,
        name: str | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: SortByDatasetColumn | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Dataset, AsyncItemsCursorGetPagination[Dataset]]:
        """
        Returns one page of the datasets in the workspace, filtered and sorted by the
        query parameters. Pass the next_cursor of a response as cursor, with the same
        filters and sort, to get the next page. next_cursor is null on the last page.

        Args:
          id: Return only the datasets with these IDs. Repeat the parameter for several IDs.

          cursor: The next_cursor of the previous response. Omit it for the first page.

          data_type: Return only datasets of these data types. Repeat the parameter for several
              types.

          exclude: Fields to leave out of each dataset. An excluded example_count is returned as
              null and makes the response faster.

          exclude_corrections_datasets: Leave out datasets that store corrections for an evaluator.

          metadata: A JSON object. Return only datasets whose metadata contains every key and value
              in it.

          name: Return only the dataset with exactly this name.

          name_contains: Return only datasets whose name contains this text, ignoring case.

          page_size: Maximum number of datasets to return.

          sort_by: Field to sort by. last_session_start_time is the start time of the most recent
              experiment on the dataset. Datasets without a value come last in both orders.
              While a sort value changes, for example when an experiment starts, a dataset can
              be skipped or listed twice across pages. Sort by created_at for a stable walk.

          sort_order: Sort direction.

          tag_value_id: Return only datasets tagged with all of these tag value IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/datasets",
            page=AsyncItemsCursorGetPagination[Dataset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "data_type": data_type,
                        "exclude": exclude,
                        "exclude_corrections_datasets": exclude_corrections_datasets,
                        "metadata": metadata,
                        "name": name,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "tag_value_id": tag_value_id,
                    },
                    dataset_list_v2_params.DatasetListV2Params,
                ),
            ),
            model=Dataset,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.list_v2 = to_raw_response_wrapper(
            datasets.list_v2,
        )

    @cached_property
    def examples(self) -> ExamplesResourceWithRawResponse:
        return ExamplesResourceWithRawResponse(self._datasets.examples)

    @cached_property
    def experiment_runs(self) -> ExperimentRunsResourceWithRawResponse:
        return ExperimentRunsResourceWithRawResponse(self._datasets.experiment_runs)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.list_v2 = async_to_raw_response_wrapper(
            datasets.list_v2,
        )

    @cached_property
    def examples(self) -> AsyncExamplesResourceWithRawResponse:
        return AsyncExamplesResourceWithRawResponse(self._datasets.examples)

    @cached_property
    def experiment_runs(self) -> AsyncExperimentRunsResourceWithRawResponse:
        return AsyncExperimentRunsResourceWithRawResponse(self._datasets.experiment_runs)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.list_v2 = to_streamed_response_wrapper(
            datasets.list_v2,
        )

    @cached_property
    def examples(self) -> ExamplesResourceWithStreamingResponse:
        return ExamplesResourceWithStreamingResponse(self._datasets.examples)

    @cached_property
    def experiment_runs(self) -> ExperimentRunsResourceWithStreamingResponse:
        return ExperimentRunsResourceWithStreamingResponse(self._datasets.experiment_runs)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.list_v2 = async_to_streamed_response_wrapper(
            datasets.list_v2,
        )

    @cached_property
    def examples(self) -> AsyncExamplesResourceWithStreamingResponse:
        return AsyncExamplesResourceWithStreamingResponse(self._datasets.examples)

    @cached_property
    def experiment_runs(self) -> AsyncExperimentRunsResourceWithStreamingResponse:
        return AsyncExperimentRunsResourceWithStreamingResponse(self._datasets.experiment_runs)
