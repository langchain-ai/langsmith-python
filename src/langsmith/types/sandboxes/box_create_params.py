# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..proxy_config_param import ProxyConfigParam
from ..sandbox_mount_config_param import SandboxMountConfigParam

__all__ = ["BoxCreateParams", "AccessDelegation", "RunConfig", "Volume"]


class BoxCreateParams(TypedDict, total=False):
    access_delegation: AccessDelegation
    """
    AccessDelegation lets code inside the sandbox call the LangSmith API as you,
    with at most the permissions granted here. Omit for no access.
    """

    cpu_millicores: int
    """CPUMillicores optionally requests CPU at millicore granularity (e.g.

    500 = 0.5 vCPU); takes precedence over VCPUs. Fractional (sub-vCPU) values are
    not available for every sandbox.
    """

    delete_after_stop_seconds: int

    env_vars: Dict[str, str]

    fs_capacity_bytes: int

    idle_ttl_seconds: int

    labels: Dict[str, str]
    """
    Labels are free-form key/value metadata persisted with the sandbox and returned
    on reads. Labels from the source snapshot are inherited unless overridden here.
    """

    mem_bytes: int
    """Memory for the sandbox, in bytes.

    Memory is tied to CPU at 4 GiB per vCPU: omit it and it follows that ratio; set
    it and it must stay within 50% of the ratio for the requested CPU, so a 1 vCPU
    sandbox accepts 2-6 GiB. Setting memory without CPU derives the CPU from the
    same ratio. Maximum 64 GiB.
    """

    mount_config: SandboxMountConfigParam

    name: str

    persistent: bool
    """
    Persistent (private beta) keeps the sandbox's filesystem across stops (the
    default, true). Set it to false for a disposable sandbox: its writes are
    discarded whenever it stops, the next start boots it fresh from its snapshot,
    and it is never charged for storage. A sandbox that is not persistent cannot
    preserve memory on stop or have its filesystem captured as a snapshot (exporting
    a Docker image from it with docker_image still works), and some snapshots
    captured from other sandboxes cannot start one; such a create is rejected.
    Setting it to false requires the private beta to be enabled for your workspace.
    """

    preserve_memory_on_stop: bool
    """
    PreserveMemoryOnStop, when true, suspends the sandbox's memory on a voluntary
    stop (idle timeout or explicit stop) so the next start resumes from where it
    left off. Default false discards memory and keeps only the filesystem, so the
    next start is a cold boot. Restarts triggered by infrastructure maintenance
    always preserve memory regardless of this setting.
    """

    proxy_config: ProxyConfigParam

    restore_memory: bool
    """RestoreMemory selects how the sandbox handles a snapshot's captured memory:

    nil → if-present: resume from memory when the snapshot has it, else cold-boot
    (default). true → always: resume from memory; rejected if the snapshot has none.
    false → never: always cold-boot.

    Applies to this request only.
    """

    run_config: RunConfig
    """
    RunConfig overrides the snapshot's run config for this sandbox: user and
    work_dir replace the snapshot's, env_vars merge over it. The result is what the
    sandbox boots with, and what a snapshot captured from it carries.
    """

    snapshot: str
    """Snapshot is a Docker-style name or name:tag reference to boot from.

    A bare name resolves to name:latest.
    """

    snapshot_id: str

    snapshot_name: str
    """
    SnapshotName is a synonym for Snapshot, accepted for compatibility with clients
    that predate it. Set one or the other.
    """

    tag_value_ids: SequenceNotStr[str]

    vcpus: int

    volumes: Iterable[Volume]
    """Volumes (beta) attaches existing volumes at mount paths inside the sandbox.

    At most 4; requires sandbox volumes to be enabled for your workspace. Attaching
    a volume requires being its creator or holding sandboxes:exec.
    """


class AccessDelegation(TypedDict, total=False):
    """
    AccessDelegation lets code inside the sandbox call the LangSmith API as you, with at most the permissions granted here. Omit for no access.
    """

    mode: Required[Literal["INHERIT", "EXPLICIT"]]

    permissions: SequenceNotStr[str]


class RunConfig(TypedDict, total=False):
    """
    RunConfig overrides the snapshot's run config for this sandbox: user and
    work_dir replace the snapshot's, env_vars merge over it. The result is
    what the sandbox boots with, and what a snapshot captured from it carries.
    """

    env_vars: Dict[str, str]

    user: str

    work_dir: str


class Volume(TypedDict, total=False):
    mount_path: Required[str]
    """
    MountPath is the absolute directory inside the sandbox where the volume appears.
    """

    volume: Required[str]
    """Volume is the volume's ID or name."""

    read_only: bool
    """ReadOnly mounts the volume read-only; many sandboxes may do so at once."""
