# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WorkspaceTagListParams"]


class WorkspaceTagListParams(TypedDict, total=False):
    resource_type: Optional[
        Literal[
            "agent",
            "custom_app",
            "dashboard",
            "dataset",
            "deployment",
            "evaluator",
            "experiment",
            "fleet_integration",
            "mcp_server",
            "project",
            "prompt",
            "queue",
            "sandbox",
            "skill",
            "snapshot_name",
        ]
    ]
