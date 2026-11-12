# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

from ..types import (
    evaluator_list_params,
    evaluator_list_v2_params,
    evaluator_create_decision_model_params,
)
from .._httpx import httpx
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncItemsCursorGetPagination, AsyncItemsCursorGetPagination
from ..types.rule import Rule
from .._base_client import AsyncPaginator, make_request_options
from ..types.evaluator import Evaluator
from ..types.evaluator_list_response import EvaluatorListResponse

__all__ = ["EvaluatorsResource", "AsyncEvaluatorsResource"]


class EvaluatorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return EvaluatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return EvaluatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        evaluator_id: Optional[str] | Omit = omit,
        include_backfill_progress: bool | Omit = omit,
        name_contains: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        tag_value_id: Optional[SequenceNotStr[str]] | Omit = omit,
        type: Optional[Literal["session", "dataset"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorListResponse:
        """
        List all run rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/runs/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "dataset_id": dataset_id,
                        "evaluator_id": evaluator_id,
                        "include_backfill_progress": include_backfill_progress,
                        "name_contains": name_contains,
                        "session_id": session_id,
                        "tag_value_id": tag_value_id,
                        "type": type,
                    },
                    evaluator_list_params.EvaluatorListParams,
                ),
            ),
            cast_to=EvaluatorListResponse,
        )

    def create_decision_model(
        self,
        *,
        display_name: str,
        prompt: Iterable[Iterable[object]],
        questions: Dict[str, evaluator_create_decision_model_params.Questions],
        base_url: Optional[str] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        group_by: Optional[Literal["thread_id"]] | Omit = omit,
        max_retries: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        model_headers: Optional[Dict[str, str]] | Omit = omit,
        playground_settings_id: Optional[str] | Omit = omit,
        provider: Literal["typesafe", "typesafe_compatible", "openai_decisions"] | Omit = omit,
        sampling_rate: float | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        template_format: Literal["mustache", "f-string"] | Omit = omit,
        timeout_seconds: Optional[int] | Omit = omit,
        variable_mapping: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluator:
        """
        Create a decision-model evaluator (Jev, SemIf or OpenAI Decisions) from its
        prompt and questions, and attach it to a project or dataset. Each question's key
        becomes a feedback key.

        Args:
          display_name: The evaluator's name.

          prompt: The prompt the model reads, as (role, template) pairs.

          questions: The questions, keyed by feedback key, in the order to ask them.

          base_url: Call this endpoint directly instead of through the LangSmith gateway, with the
              workspace's TYPESAFE_API_KEY or OPENAI_API_KEY secret. Required for
              typesafe_compatible.

          dataset_id: The dataset whose experiments to evaluate.

          filter: Only evaluate runs that match this filter.

          group_by: Set to thread_id to evaluate each thread once it goes idle, instead of each run.
              Requires session_id. Decision models don't support trajectory_id.

          max_retries: How many times to retry a failed model call. openai_decisions only.

          model: Defaults to jev-latest for typesafe and gpt-6-luna for openai_decisions. Use
              semif-qwen3.5-4b for SemIf.

          model_headers: Headers sent with each model call. They are saved in the evaluator's prompt as
              given, so do not put API keys here.

          playground_settings_id: A saved model configuration to start from: its model, endpoint, key and settings
              apply unless set here.

          provider: typesafe for Jev and SemIf, typesafe_compatible for a TypeSafe-compatible
              endpoint, or openai_decisions.

          sampling_rate: The fraction of runs to evaluate.

          session_id: The tracing project to evaluate.

          timeout_seconds: Seconds to wait for each model call. openai_decisions only.

          variable_mapping: Maps the prompt's variables to run fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/runs/rules/decision-models",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "prompt": prompt,
                    "questions": questions,
                    "base_url": base_url,
                    "dataset_id": dataset_id,
                    "filter": filter,
                    "group_by": group_by,
                    "max_retries": max_retries,
                    "model": model,
                    "model_headers": model_headers,
                    "playground_settings_id": playground_settings_id,
                    "provider": provider,
                    "sampling_rate": sampling_rate,
                    "session_id": session_id,
                    "template_format": template_format,
                    "timeout_seconds": timeout_seconds,
                    "variable_mapping": variable_mapping,
                },
                evaluator_create_decision_model_params.EvaluatorCreateDecisionModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluator,
        )

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_id: str | Omit = omit,
        evaluator_id: str | Omit = omit,
        include_backfill_progress: bool | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        type: Literal["PROJECT", "DATASET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursorGetPagination[Rule]:
        """List workspace rules in descending updated_at and id order.

        Filters combine with
        AND. Pass next_cursor unchanged with the same filters to continue; concurrent
        changes can affect later pages.

        Args:
          id: Rule UUIDs

          cursor: Cursor from the previous page

          dataset_id: Source dataset UUID

          evaluator_id: Linked evaluator UUID

          include_backfill_progress: Include backfill progress

          name_contains: Case-insensitive display-name pattern

          page_size: Page size

          project_id: Source project UUID

          tag_value_id: Source must have every tag UUID

          type: Rule source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/runs/rules",
            page=SyncItemsCursorGetPagination[Rule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "dataset_id": dataset_id,
                        "evaluator_id": evaluator_id,
                        "include_backfill_progress": include_backfill_progress,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "project_id": project_id,
                        "tag_value_id": tag_value_id,
                        "type": type,
                    },
                    evaluator_list_v2_params.EvaluatorListV2Params,
                ),
            ),
            model=Rule,
        )

    list_v1 = list


class AsyncEvaluatorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/langchain-ai/langsmith-python#with_streaming_response
        """
        return AsyncEvaluatorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        evaluator_id: Optional[str] | Omit = omit,
        include_backfill_progress: bool | Omit = omit,
        name_contains: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        tag_value_id: Optional[SequenceNotStr[str]] | Omit = omit,
        type: Optional[Literal["session", "dataset"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorListResponse:
        """
        List all run rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/runs/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "dataset_id": dataset_id,
                        "evaluator_id": evaluator_id,
                        "include_backfill_progress": include_backfill_progress,
                        "name_contains": name_contains,
                        "session_id": session_id,
                        "tag_value_id": tag_value_id,
                        "type": type,
                    },
                    evaluator_list_params.EvaluatorListParams,
                ),
            ),
            cast_to=EvaluatorListResponse,
        )

    async def create_decision_model(
        self,
        *,
        display_name: str,
        prompt: Iterable[Iterable[object]],
        questions: Dict[str, evaluator_create_decision_model_params.Questions],
        base_url: Optional[str] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        group_by: Optional[Literal["thread_id"]] | Omit = omit,
        max_retries: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        model_headers: Optional[Dict[str, str]] | Omit = omit,
        playground_settings_id: Optional[str] | Omit = omit,
        provider: Literal["typesafe", "typesafe_compatible", "openai_decisions"] | Omit = omit,
        sampling_rate: float | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        template_format: Literal["mustache", "f-string"] | Omit = omit,
        timeout_seconds: Optional[int] | Omit = omit,
        variable_mapping: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluator:
        """
        Create a decision-model evaluator (Jev, SemIf or OpenAI Decisions) from its
        prompt and questions, and attach it to a project or dataset. Each question's key
        becomes a feedback key.

        Args:
          display_name: The evaluator's name.

          prompt: The prompt the model reads, as (role, template) pairs.

          questions: The questions, keyed by feedback key, in the order to ask them.

          base_url: Call this endpoint directly instead of through the LangSmith gateway, with the
              workspace's TYPESAFE_API_KEY or OPENAI_API_KEY secret. Required for
              typesafe_compatible.

          dataset_id: The dataset whose experiments to evaluate.

          filter: Only evaluate runs that match this filter.

          group_by: Set to thread_id to evaluate each thread once it goes idle, instead of each run.
              Requires session_id. Decision models don't support trajectory_id.

          max_retries: How many times to retry a failed model call. openai_decisions only.

          model: Defaults to jev-latest for typesafe and gpt-6-luna for openai_decisions. Use
              semif-qwen3.5-4b for SemIf.

          model_headers: Headers sent with each model call. They are saved in the evaluator's prompt as
              given, so do not put API keys here.

          playground_settings_id: A saved model configuration to start from: its model, endpoint, key and settings
              apply unless set here.

          provider: typesafe for Jev and SemIf, typesafe_compatible for a TypeSafe-compatible
              endpoint, or openai_decisions.

          sampling_rate: The fraction of runs to evaluate.

          session_id: The tracing project to evaluate.

          timeout_seconds: Seconds to wait for each model call. openai_decisions only.

          variable_mapping: Maps the prompt's variables to run fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/runs/rules/decision-models",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "prompt": prompt,
                    "questions": questions,
                    "base_url": base_url,
                    "dataset_id": dataset_id,
                    "filter": filter,
                    "group_by": group_by,
                    "max_retries": max_retries,
                    "model": model,
                    "model_headers": model_headers,
                    "playground_settings_id": playground_settings_id,
                    "provider": provider,
                    "sampling_rate": sampling_rate,
                    "session_id": session_id,
                    "template_format": template_format,
                    "timeout_seconds": timeout_seconds,
                    "variable_mapping": variable_mapping,
                },
                evaluator_create_decision_model_params.EvaluatorCreateDecisionModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Evaluator,
        )

    def list_v2(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_id: str | Omit = omit,
        evaluator_id: str | Omit = omit,
        include_backfill_progress: bool | Omit = omit,
        name_contains: str | Omit = omit,
        page_size: int | Omit = omit,
        project_id: str | Omit = omit,
        tag_value_id: SequenceNotStr[str] | Omit = omit,
        type: Literal["PROJECT", "DATASET"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Rule, AsyncItemsCursorGetPagination[Rule]]:
        """List workspace rules in descending updated_at and id order.

        Filters combine with
        AND. Pass next_cursor unchanged with the same filters to continue; concurrent
        changes can affect later pages.

        Args:
          id: Rule UUIDs

          cursor: Cursor from the previous page

          dataset_id: Source dataset UUID

          evaluator_id: Linked evaluator UUID

          include_backfill_progress: Include backfill progress

          name_contains: Case-insensitive display-name pattern

          page_size: Page size

          project_id: Source project UUID

          tag_value_id: Source must have every tag UUID

          type: Rule source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/runs/rules",
            page=AsyncItemsCursorGetPagination[Rule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "dataset_id": dataset_id,
                        "evaluator_id": evaluator_id,
                        "include_backfill_progress": include_backfill_progress,
                        "name_contains": name_contains,
                        "page_size": page_size,
                        "project_id": project_id,
                        "tag_value_id": tag_value_id,
                        "type": type,
                    },
                    evaluator_list_v2_params.EvaluatorListV2Params,
                ),
            ),
            model=Rule,
        )

    list_v1 = list


class EvaluatorsResourceWithRawResponse:
    def __init__(self, evaluators: EvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = to_raw_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = to_raw_response_wrapper(
            evaluators.create_decision_model,
        )
        self.list_v2 = to_raw_response_wrapper(
            evaluators.list_v2,
        )
        self.list_v1 = to_raw_response_wrapper(
            evaluators.list_v1,
        )


class AsyncEvaluatorsResourceWithRawResponse:
    def __init__(self, evaluators: AsyncEvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = async_to_raw_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = async_to_raw_response_wrapper(
            evaluators.create_decision_model,
        )
        self.list_v2 = async_to_raw_response_wrapper(
            evaluators.list_v2,
        )
        self.list_v1 = async_to_raw_response_wrapper(
            evaluators.list_v1,
        )


class EvaluatorsResourceWithStreamingResponse:
    def __init__(self, evaluators: EvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = to_streamed_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = to_streamed_response_wrapper(
            evaluators.create_decision_model,
        )
        self.list_v2 = to_streamed_response_wrapper(
            evaluators.list_v2,
        )
        self.list_v1 = to_streamed_response_wrapper(
            evaluators.list_v1,
        )


class AsyncEvaluatorsResourceWithStreamingResponse:
    def __init__(self, evaluators: AsyncEvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = async_to_streamed_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = async_to_streamed_response_wrapper(
            evaluators.create_decision_model,
        )
        self.list_v2 = async_to_streamed_response_wrapper(
            evaluators.list_v2,
        )
        self.list_v1 = async_to_streamed_response_wrapper(
            evaluators.list_v1,
        )
