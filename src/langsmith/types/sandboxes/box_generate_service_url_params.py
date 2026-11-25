# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BoxGenerateServiceURLParams"]


class BoxGenerateServiceURLParams(TypedDict, total=False):
    access: Literal["restricted", "workspace", "off"]
    """
    Access selects the login mode, mutually exclusive with the minted token. Omit
    the field for token mode: mint a short-lived service token (default).
    "restricted" — LangSmith login: the sandbox's creator, or any user with
    SandboxesExec on it (admins by default). "workspace" — LangSmith login: any
    member of the owning workspace. "off" — remove an existing LangSmith login grant
    and mint a token. A LangSmith login grant is durable; token mode is refused
    (409) while one exists.
    """

    embed_origins: SequenceNotStr[str]
    """
    EmbedOrigins are the pages allowed to show the service URL in an iframe, besides
    LangSmith itself: at most 5 origins such as https://app.example.com (http only
    for localhost). In token mode they are bound into the minted token, so they last
    as long as it does. With access "restricted" or "workspace" each call sets the
    grant's whole list, so omitting the field removes any origins set before.
    """

    expires_in_seconds: int

    port: int
