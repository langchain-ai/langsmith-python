# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitCreateParams"]


class CommitCreateParams(TypedDict, total=False):
    owner: Required[str]

    manifest: Required[object]

    description: str

    parent_commit: str

    skip_webhooks: object
    """SkipWebhooks allows skipping webhook notifications.

    Can be true (boolean) to skip all, or an array of webhook UUIDs to skip specific
    ones.
    """
