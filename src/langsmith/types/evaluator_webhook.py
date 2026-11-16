# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["EvaluatorWebhook"]


class EvaluatorWebhook(BaseModel):
    url: str

    headers: Optional[Dict[str, str]] = None
