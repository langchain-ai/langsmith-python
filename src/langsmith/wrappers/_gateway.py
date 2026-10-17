"""Copy LangSmith LLM Gateway response metadata onto traced LLM runs."""

from __future__ import annotations

import json
from typing import Any

from langsmith import run_helpers

_GATEWAY_METADATA_HEADER = "x-langsmith-gateway-metadata"
_GATEWAY_METADATA_KEY = "ls_gateway_info"
# LangSmith uses request_id to find the gateway's own traces for this call.
_GATEWAY_METADATA_FIELDS = (
    "request_id",
    "outcome",
    "reason",
    "provider",
    "model",
    "blocking_policies",
    "attempt_details",
    "fallback_used",
)
# Run search indexes only top-level metadata keys, so the most common filters
# are also written as flat keys.
_GATEWAY_FILTER_KEY_PREFIX = "ls_gateway."
_HOOK_MARKER = "_langsmith_gateway_metadata_hook_installed"


def _filter_keys(parsed: dict) -> dict[str, Any]:
    policies = parsed.get("blocking_policies")
    blocking = (
        ", ".join(p["name"] for p in policies if isinstance(p, dict) and isinstance(p.get("name"), str))
        if isinstance(policies, list)
        else None
    )
    fields = {
        "request_id": parsed.get("request_id"),
        "outcome": parsed.get("outcome"),
        "provider": parsed.get("provider"),
        "model": parsed.get("selected_model") or parsed.get("model"),
        "fallback_used": parsed.get("fallback_used"),
        "attempts": parsed.get("attempts"),
        "blocking_policies": blocking,
    }
    return {_GATEWAY_FILTER_KEY_PREFIX + k: v for k, v in fields.items() if v is not None and v != ""}


def _add_gateway_metadata(response: Any) -> None:
    try:
        raw = response.headers.get(_GATEWAY_METADATA_HEADER)
        if not isinstance(raw, str):
            return
        run = run_helpers.get_current_run_tree()
        if run is None or run.run_type != "llm":
            return
        parsed = json.loads(raw)
        if not isinstance(parsed, dict):
            return
        info = {k: parsed[k] for k in _GATEWAY_METADATA_FIELDS if k in parsed}
        if info:
            run.add_metadata({_GATEWAY_METADATA_KEY: info, **_filter_keys(parsed)})
    except Exception:
        # Gateway metadata must never affect the provider call.
        return


def install_gateway_response_hook(client: Any) -> None:
    """Add an httpx response hook that copies gateway metadata to the LLM run."""
    try:
        import httpx

        http_client = getattr(client, "_client", None)
        if not isinstance(http_client, (httpx.Client, httpx.AsyncClient)):
            return
        if getattr(http_client, _HOOK_MARKER, False):
            return

        hooks = http_client.event_hooks
        if isinstance(http_client, httpx.AsyncClient):

            async def _async_hook(response: httpx.Response) -> None:
                _add_gateway_metadata(response)

            hooks["response"] = [*hooks.get("response", []), _async_hook]
        else:
            hooks["response"] = [*hooks.get("response", []), _add_gateway_metadata]
        # Assigning event_hooks re-validates them on the httpx client.
        http_client.event_hooks = hooks
        setattr(http_client, _HOOK_MARKER, True)
    except Exception:
        return
