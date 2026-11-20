# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SandboxRetrieveUsageResponse"]


class SandboxRetrieveUsageResponse(BaseModel):
    cpu_limit_millicores: Optional[int] = None

    cpu_used_millicores: Optional[int] = None

    memory_limit_bytes: Optional[int] = None

    memory_used_bytes: Optional[int] = None

    pools_count: Optional[int] = None

    registries_count: Optional[int] = None

    sandbox_direct_count: Optional[int] = None

    sandbox_pool_replicas_count: Optional[int] = None

    sandbox_running_count: Optional[int] = None

    sandbox_stopped_count: Optional[int] = None

    sandboxes_limit: Optional[int] = None

    sandboxes_used: Optional[int] = None

    snapshots_count: Optional[int] = None

    templates_count: Optional[int] = None
