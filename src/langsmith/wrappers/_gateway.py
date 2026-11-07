"""Copy LangSmith LLM Gateway response metadata onto traced LLM runs."""

from __future__ import annotations

import importlib
import json
from collections.abc import Mapping
from typing import Any, Optional

from langsmith import run_helpers
from langsmith.run_trees import RunTree

_GATEWAY_METADATA_HEADER = "x-langsmith-gateway-metadata"
_GATEWAY_METADATA_KEY = "ls_gateway_info"
_HOOK_MARKER = "_langsmith_gateway_metadata_hook_installed"


def _get_header(headers: Any) -> Any:
    raw = headers.get(_GATEWAY_METADATA_HEADER)
    # Plain dicts, such as google-genai's response headers, keep the case the
    # server sent.
    if raw is None and isinstance(headers, Mapping):
        raw = next(
            (value for key, value in headers.items() if str(key).lower() == _GATEWAY_METADATA_HEADER),
            None,
        )
    return raw


def add_gateway_metadata(headers: Any, run: Optional[RunTree] = None) -> None:
    """Copy gateway metadata from response headers onto the LLM run.

    Defaults to the current run. Pass `run` when the response is read outside
    the run's context, such as a stream iterated after its call returned.
    """
    try:
        if headers is None:
            return
        raw = _get_header(headers)
        if not isinstance(raw, str):
            return
        run = run or run_helpers.get_current_run_tree()
        if run is None or run.run_type != "llm":
            return
        parsed = json.loads(raw)
        if not isinstance(parsed, dict) or not parsed:
            return
        run.add_metadata({_GATEWAY_METADATA_KEY: parsed})
    except Exception:
        # Gateway metadata must never affect the provider call.
        return


def add_gateway_response_metadata(response: Any) -> None:
    add_gateway_metadata(getattr(response, "headers", None))


def _httpx_client_types() -> tuple[tuple[type[Any], ...], tuple[type[Any], ...]]:
    """Return the sync and async client types of every installed HTTPX backend.

    Provider SDKs choose their backend independently of this package: openai 3.x
    uses httpx2, while older releases use httpx.
    """
    sync_types: list[type[Any]] = []
    async_types: list[type[Any]] = []
    for name in ("httpx2", "httpx"):
        try:
            module = importlib.import_module(name)
        except ImportError:
            continue
        sync_types.append(module.Client)
        async_types.append(module.AsyncClient)
    return tuple(sync_types), tuple(async_types)


def install_gateway_response_hook(client: Any) -> None:
    """Add an httpx response hook that copies gateway metadata to the LLM run."""
    try:
        sync_types, async_types = _httpx_client_types()
        http_client = getattr(client, "_client", None)
        if not isinstance(http_client, sync_types + async_types):
            return
        if getattr(http_client, _HOOK_MARKER, False):
            return

        hooks = http_client.event_hooks
        if isinstance(http_client, async_types):

            async def _async_hook(response: Any) -> None:
                add_gateway_response_metadata(response)

            hooks["response"] = [*hooks.get("response", []), _async_hook]
        else:
            hooks["response"] = [*hooks.get("response", []), add_gateway_response_metadata]
        # Assigning event_hooks re-validates them on the httpx client.
        http_client.event_hooks = hooks
        setattr(http_client, _HOOK_MARKER, True)
    except Exception:
        return
