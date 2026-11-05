# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .online_evaluator_type import OnlineEvaluatorType
from .create_online_llm_evaluator_request_param import CreateOnlineLlmEvaluatorRequestParam
from .create_online_code_evaluator_request_param import CreateOnlineCodeEvaluatorRequestParam

__all__ = ["OnlineEvaluatorCreateParams"]


class OnlineEvaluatorCreateParams(TypedDict, total=False):
    code_evaluator: CreateOnlineCodeEvaluatorRequestParam

    llm_evaluator: CreateOnlineLlmEvaluatorRequestParam

    metadata: Optional[Dict[str, object]]

    name: str

    type: OnlineEvaluatorType
