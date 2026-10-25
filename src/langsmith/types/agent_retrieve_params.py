# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    include: Literal["runtime_bindings"]
    """Relation to embed.

    runtime_bindings adds each environment's runtime bindings; an empty array means
    no runtime is linked.
    """
