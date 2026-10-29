# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CodeEvaluatorTopLevel"]


class CodeEvaluatorTopLevel(BaseModel):
    code: str

    advanced_features_enabled: Optional[bool] = None

    code_evaluator_input: Optional[
        Literal["thread", "all_messages", "human_ai_pairs", "first_human_last_ai", "trajectory"]
    ] = None
    """Input provided to a code evaluator."""

    language: Optional[Literal["python", "javascript"]] = None

    require_attachments: Optional[bool] = None
