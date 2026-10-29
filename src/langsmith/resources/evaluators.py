# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

from ..types import evaluator_list_params, evaluator_create_decision_model_params
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
from .._base_client import make_request_options
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
          prompt: The prompt the model reads, as (role, template) pairs.

          questions: The questions, keyed by feedback key, in the order to ask them.

          base_url: Call this endpoint directly instead of through the LangSmith gateway, with the
              workspace's TYPESAFE_API_KEY or OPENAI_API_KEY secret. Required for
              typesafe_compatible.

          dataset_id: The dataset whose experiments to evaluate.

          filter: Only evaluate runs that match this filter.

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
          prompt: The prompt the model reads, as (role, template) pairs.

          questions: The questions, keyed by feedback key, in the order to ask them.

          base_url: Call this endpoint directly instead of through the LangSmith gateway, with the
              workspace's TYPESAFE_API_KEY or OPENAI_API_KEY secret. Required for
              typesafe_compatible.

          dataset_id: The dataset whose experiments to evaluate.

          filter: Only evaluate runs that match this filter.

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


class EvaluatorsResourceWithRawResponse:
    def __init__(self, evaluators: EvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = to_raw_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = to_raw_response_wrapper(
            evaluators.create_decision_model,
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


class EvaluatorsResourceWithStreamingResponse:
    def __init__(self, evaluators: EvaluatorsResource) -> None:
        self._evaluators = evaluators

        self.list = to_streamed_response_wrapper(
            evaluators.list,
        )
        self.create_decision_model = to_streamed_response_wrapper(
            evaluators.create_decision_model,
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
