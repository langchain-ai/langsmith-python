# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SandboxListUsageCostsResponse"]


class SandboxListUsageCostsResponse(BaseModel):
    lcu: str
    """
    Recorded compute usage in LangSmith Compute Units (LCU), as a decimal string
    with up to six fractional digits and trailing zeros omitted. Snapshots return
    "0".
    """

    lsu: str
    """
    Allocated storage usage in LangSmith Storage Units (LSU), as a decimal string
    with up to six fractional digits and trailing zeros omitted.
    """

    period_start: datetime

    resource_id: str

    resource_type: Literal["SANDBOX", "SNAPSHOT"]

    compute_standard_units: Optional[str] = None
    """
    Recorded compute usage in Standard Units, as a decimal string, separate from
    LCU. Null means complete Standard compute usage is unavailable; "0" means known
    zero usage.
    """

    memory_gib_hours: Optional[str] = None
    """Memory usage in GiB-hours, as a decimal string.

    Available with RESOURCE granularity; null means complete usage is unavailable.
    """

    storage_gib_hours: Optional[str] = None
    """Recorded storage usage in GiB-hours from hourly samples, including checkpoints.

    Available with RESOURCE granularity. Missing intervals are excluded; null means
    no usable measurements are available.
    """

    storage_standard_units: Optional[str] = None
    """
    Allocated storage usage in Standard Units, as a decimal string, separate from
    LSU. Null means complete Standard storage usage is unavailable; "0" means known
    zero usage.
    """

    vcpu_hours: Optional[str] = None
    """CPU usage in vCPU-hours, as a decimal string.

    Available with RESOURCE granularity; null means complete usage is unavailable.
    """
