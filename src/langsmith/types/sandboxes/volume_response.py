# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VolumeResponse", "Attachment"]


class Attachment(BaseModel):
    mount_path: Optional[str] = None

    read_only: Optional[bool] = None

    sandbox_id: Optional[str] = None

    sandbox_name: Optional[str] = None


class VolumeResponse(BaseModel):
    id: Optional[str] = None

    attachments: Optional[List[Attachment]] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    labels: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    size_bytes: Optional[int] = None

    source_volume_id: Optional[str] = None

    status: Optional[str] = None

    status_message: Optional[str] = None

    updated_at: Optional[datetime] = None

    updated_by: Optional[str] = None
