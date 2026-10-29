# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EvaluatorCreateDecisionModelParams", "Questions"]


class EvaluatorCreateDecisionModelParams(TypedDict, total=False):
    display_name: Required[str]

    prompt: Required[Iterable[Iterable[object]]]
    """The prompt the model reads, as (role, template) pairs."""

    questions: Required[Dict[str, Questions]]
    """The questions, keyed by feedback key, in the order to ask them."""

    base_url: Optional[str]
    """
    Call this endpoint directly instead of through the LangSmith gateway, with the
    workspace's TYPESAFE_API_KEY or OPENAI_API_KEY secret. Required for
    typesafe_compatible.
    """

    dataset_id: Optional[str]
    """The dataset whose experiments to evaluate."""

    filter: Optional[str]
    """Only evaluate runs that match this filter."""

    max_retries: Optional[int]
    """How many times to retry a failed model call. openai_decisions only."""

    model: Optional[str]
    """Defaults to jev-latest for typesafe and gpt-6-luna for openai_decisions.

    Use semif-qwen3.5-4b for SemIf.
    """

    model_headers: Optional[Dict[str, str]]
    """Headers sent with each model call.

    They are saved in the evaluator's prompt as given, so do not put API keys here.
    """

    playground_settings_id: Optional[str]
    """
    A saved model configuration to start from: its model, endpoint, key and settings
    apply unless set here.
    """

    provider: Literal["typesafe", "typesafe_compatible", "openai_decisions"]
    """
    typesafe for Jev and SemIf, typesafe_compatible for a TypeSafe-compatible
    endpoint, or openai_decisions.
    """

    sampling_rate: float
    """The fraction of runs to evaluate."""

    session_id: Optional[str]
    """The tracing project to evaluate."""

    template_format: Literal["mustache", "f-string"]

    timeout_seconds: Optional[int]
    """Seconds to wait for each model call. openai_decisions only."""

    variable_mapping: Optional[Dict[str, str]]
    """Maps the prompt's variables to run fields."""


class Questions(TypedDict, total=False):
    """A question a decision model answers about each run."""

    instructions: Required[str]

    type: Required[Literal["noul", "choice", "score"]]
    """noul: a yes/no question scored 0 to 1.

    choice: one of the options. score: one of the levels, scored by position.
    """

    levels: Optional[SequenceNotStr[str]]
    """2 to 10 level names, lowest first. score only."""

    no: Optional[str]
    """What a no answer means. noul only; set both yes and no, or neither."""

    options: Union[SequenceNotStr[str], Dict[str, Optional[str]], None]
    """2 to 255 option names, or names mapped to descriptions. choice only."""

    yes: Optional[str]
    """What a yes answer means. noul only; set both yes and no, or neither."""
