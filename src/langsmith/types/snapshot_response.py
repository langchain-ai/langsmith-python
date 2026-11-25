# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .proxy_config import ProxyConfig
from .sandbox_mount_config import SandboxMountConfig

__all__ = ["SnapshotResponse", "RunConfig"]


class RunConfig(BaseModel):
    """RunConfig is what sandboxes from this snapshot boot with.

    Absent on
    snapshots built before it was recorded, which run as root with their own env.
    """

    env_vars: Optional[Dict[str, str]] = None

    user: Optional[str] = None

    work_dir: Optional[str] = None


class SnapshotResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    description: Optional[str] = None
    """
    Description says what this snapshot's image can do, so a caller can hand it to
    an agent as a capability summary.
    """

    docker_image: Optional[str] = None

    fs_capacity_bytes: Optional[int] = None

    fs_used_bytes: Optional[int] = None

    image_digest: Optional[str] = None

    included: Optional[List[Literal["mounts", "proxy_config", "env_vars", "resources", "lifecycle", "labels"]]] = None
    """
    The settings this snapshot carries, in include terms: sandboxes created from it
    start with each one their create request leaves unset. Env var values are never
    returned.
    """

    labels: Optional[Dict[str, str]] = None

    memory_snapshot_size_bytes: Optional[int] = None
    """
    MemorySnapshotSizeBytes is non-nil iff the snapshot was captured with VM memory
    state. A non-nil value is the canonical signal that this snapshot can
    warm-restore from memory; nil means rootfs only.
    """

    mount_config: Optional[SandboxMountConfig] = None
    """
    The mount_config sandboxes created from this snapshot start with when their
    create request has none, with secret values redacted. Present only on snapshots
    captured with include "mounts" or "all" from a sandbox that had mounts.
    """

    name: Optional[str] = None

    proxy_config: Optional[ProxyConfig] = None
    """
    The proxy_config sandboxes created from this snapshot start with when their
    create request has none, with secret values redacted. Present only on snapshots
    captured with include "proxy_config" or "all".
    """

    registry_id: Optional[str] = None

    run_config: Optional[RunConfig] = None
    """RunConfig is what sandboxes from this snapshot boot with.

    Absent on snapshots built before it was recorded, which run as root with their
    own env.
    """

    source_sandbox_id: Optional[str] = None

    status: Optional[str] = None

    status_message: Optional[str] = None

    tags: Optional[List[str]] = None
    """Tags currently resolving to this snapshot, under Name.

    A snapshot with no tags is dangling — addressable only by id.
    """

    updated_at: Optional[str] = None
