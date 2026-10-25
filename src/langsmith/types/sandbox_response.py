# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .proxy_config import ProxyConfig
from .sandbox_mount_config import SandboxMountConfig

__all__ = ["SandboxResponse", "AccessDelegation", "RunConfig", "Volume"]


class AccessDelegation(BaseModel):
    """
    AccessDelegation is the LangSmith access this sandbox was granted, absent when it has none. It is reported exactly as it was requested at create.
    """

    mode: Literal["INHERIT", "EXPLICIT"]

    permissions: Optional[List[str]] = None


class RunConfig(BaseModel):
    """
    RunConfig is what the sandbox's commands run with: the user, working directory and base env beneath env_vars.
    """

    env_vars: Optional[Dict[str, str]] = None

    user: Optional[str] = None

    work_dir: Optional[str] = None


class Volume(BaseModel):
    mount_path: Optional[str] = None

    read_only: Optional[bool] = None

    volume_id: Optional[str] = None

    volume_name: Optional[str] = None


class SandboxResponse(BaseModel):
    id: Optional[str] = None

    access_delegation: Optional[AccessDelegation] = None
    """
    AccessDelegation is the LangSmith access this sandbox was granted, absent when
    it has none. It is reported exactly as it was requested at create.
    """

    cpu_millicores: Optional[int] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    dataplane_url: Optional[str] = None

    delete_after_stop_seconds: Optional[int] = None

    fs_capacity_bytes: Optional[int] = None

    idle_ttl_seconds: Optional[int] = None

    labels: Optional[Dict[str, str]] = None

    mem_bytes: Optional[int] = None

    mount_config: Optional[SandboxMountConfig] = None

    name: Optional[str] = None

    persistent: Optional[bool] = None
    """
    Persistent (private beta) reports whether the sandbox keeps its filesystem
    across stops. When false, its writes are discarded whenever it stops and it is
    not charged for storage.
    """

    preserve_memory_on_stop: Optional[bool] = None

    proxy_config: Optional[ProxyConfig] = None

    run_config: Optional[RunConfig] = None
    """
    RunConfig is what the sandbox's commands run with: the user, working directory
    and base env beneath env_vars.
    """

    size_class: Optional[str] = None

    snapshot_id: Optional[str] = None

    status: Optional[str] = None

    status_message: Optional[str] = None

    stopped_at: Optional[str] = None

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None

    vcpus: Optional[int] = None

    volumes: Optional[List[Volume]] = None
    """Volumes (beta) are the volumes attached to the sandbox, in slot order.

    Absent when the workspace does not have sandbox volumes enabled.
    """
