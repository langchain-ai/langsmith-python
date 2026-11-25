# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BoxCreateSnapshotParams", "ImageConfig", "RunConfig"]


class BoxCreateSnapshotParams(TypedDict, total=False):
    body_name: Required[Annotated[str, PropertyInfo(alias="name")]]

    checkpoint: str
    """if omitted, creates a fresh checkpoint from the running VM"""

    confirm_allow_snapshot_secret_values: bool
    """
    Must be true when the included settings hold literal secret values (opaque
    values rather than workspace secret references, and any env var value),
    acknowledging that the snapshot stores them and every sandbox created from it
    can use them.
    """

    description: str
    """
    Description says what this snapshot's image can do, so a caller can hand it to
    an agent as a capability summary. At most 1024 characters.
    """

    docker_image: str
    """sandbox-local Docker image to export"""

    fs_capacity_bytes: int
    """required for Docker image export unless the sandbox has a capacity"""

    image_config: ImageConfig
    """
    ImageConfig sets the command and ports the snapshot records, as a Docker image's
    ENTRYPOINT, CMD and EXPOSE do. By default a capture keeps those of the snapshot
    the sandbox was created from; each field given here replaces that one, and an
    empty list clears it. A function serving the snapshot runs this command and
    listens on its one exposed port.
    """

    include: List[Literal["all", "mounts", "proxy_config", "env_vars", "resources", "lifecycle", "labels"]]
    """Sandbox settings to carry into the snapshot.

    Sandboxes created from it start with each carried setting their create request
    leaves unset: "mounts" (the mount_config, with its auth), "proxy_config",
    "env_vars", "resources" (CPU and memory), "lifecycle" (idle_ttl_seconds,
    delete_after_stop_seconds, preserve_memory_on_stop), and "labels" (merged under
    this request's labels; reserved com.langchain.\\** labels are left out). "all"
    names every one of these. VM memory is captured with include_memory, not here.
    Warning: mounts, proxy_config and env_vars carry the sandbox's credentials, and
    every sandbox created from the snapshot can use them.
    """

    include_memory: bool
    """
    IncludeMemory, when true, captures a full VM memory snapshot alongside the
    filesystem clone. Only honored when the sandbox is running AND Checkpoint is
    omitted (i.e. a fresh in-VM checkpoint is requested). Defaults to false to keep
    snapshots small unless memory restore is explicitly desired.
    """

    labels: Dict[str, str]
    """Labels seed the captured snapshot's labels."""

    run_config: RunConfig
    """
    RunConfig overrides the runtime configuration the snapshot carries: for a
    docker_image export, the image's USER, WORKDIR and ENV; for a capture of the
    running VM, the sandbox's own. user and work_dir replace, env_vars merge.
    """

    tag: str
    """mutable Docker-style tag; defaults to "latest" """


class ImageConfig(TypedDict, total=False):
    """
    ImageConfig sets the command and ports the snapshot records, as a Docker image's ENTRYPOINT, CMD and EXPOSE do. By default a capture keeps
    those of the snapshot the sandbox was created from; each field given here replaces that one, and an empty list clears it. A function
    serving the snapshot runs this command and listens on its one exposed port.
    """

    cmd: SequenceNotStr[str]
    """
    Cmd follows Entrypoint, as CMD: its arguments, or the whole command when
    Entrypoint is empty.
    """

    entrypoint: SequenceNotStr[str]
    """Entrypoint is the program the command starts with, as ENTRYPOINT."""

    exposed_ports: Iterable[int]
    """ExposedPorts are the TCP ports the command listens on, as EXPOSE."""


class RunConfig(TypedDict, total=False):
    """
    RunConfig overrides the runtime configuration the snapshot carries: for a
    docker_image export, the image's USER, WORKDIR and ENV; for a capture of
    the running VM, the sandbox's own. user and work_dir replace, env_vars
    merge.
    """

    env_vars: Dict[str, str]

    user: str

    work_dir: str
