# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ServiceURLResponse"]


class ServiceURLResponse(BaseModel):
    token: Optional[str] = None
    """Token and ExpiresAt are empty in LangSmith login mode (no token is minted)."""

    access: Optional[Literal["restricted", "workspace"]] = None
    """
    Access echoes the enabled LangSmith login level ("restricted"/"workspace");
    omitted in token mode.
    """

    browser_url: Optional[str] = None

    embed_origins: Optional[List[str]] = None
    """
    EmbedOrigins echoes the origins that may embed the URL, normalized; omitted when
    there are none.
    """

    embed_url: Optional[str] = None
    """
    EmbedURL opens the service in an iframe: the token rides the URL fragment, which
    no server, log or Referer header sees, and the page it loads trades it for the
    cookie. Append &redirect=/path to land elsewhere than /. Omitted in LangSmith
    login mode.
    """

    expires_at: Optional[str] = None

    service_url: Optional[str] = None
