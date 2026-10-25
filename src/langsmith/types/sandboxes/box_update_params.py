# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..proxy_config_param import ProxyConfigParam

__all__ = ["BoxUpdateParams", "RunConfig"]


class BoxUpdateParams(TypedDict, total=False):
    cpu_millicores: int

    delete_after_stop_seconds: int

    fs_capacity_bytes: int

    idle_ttl_seconds: int

    mem_bytes: int
    """New memory for the sandbox, in bytes.

    The 4 GiB per vCPU ratio applies when the sandbox is created; a resize enforces
    only the maximum of 64 GiB.
    """

    body_name: Annotated[str, PropertyInfo(alias="name")]

    proxy_config: ProxyConfigParam

    run_config: RunConfig
    """
    RunConfig changes what subsequent commands run with: user and work_dir replace
    the current values, env_vars merge over them. Commands already running are
    unaffected.
    """

    tag_value_ids: SequenceNotStr[str]

    vcpus: int


class RunConfig(TypedDict, total=False):
    """
    RunConfig changes what subsequent commands run with: user and work_dir
    replace the current values, env_vars merge over them. Commands already
    running are unaffected.
    """

    env_vars: Dict[str, str]

    user: str

    work_dir: str
