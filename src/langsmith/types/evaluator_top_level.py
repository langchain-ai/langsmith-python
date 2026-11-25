# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluatorTopLevel", "Structured"]


class Structured(BaseModel):
    """Evaluator structured output schema."""

    hub_ref: Optional[str] = None

    model: Optional[Dict[str, object]] = None

    playground_settings_id: Optional[str] = None

    prompt: Optional[List[List[object]]] = None

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """Output schema for the evaluator's feedback.

    Not accepted for decision-model (TypeSafe or OpenAI Decisions) evaluators, whose
    schema comes from their questions.
    """

    template_format: Optional[str] = None

    variable_mapping: Optional[Dict[str, str]] = None


class EvaluatorTopLevel(BaseModel):
    structured: Structured
    """Evaluator structured output schema."""
