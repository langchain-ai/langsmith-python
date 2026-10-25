"""Keep generated requests in sync with their owning handwritten client."""

from collections.abc import Awaitable, Callable, Mapping
from typing import Any

from typing_extensions import Self

from langsmith._client import AsyncLangsmith, Langsmith
from langsmith._models import FinalRequestOptions
from langsmith._types import Headers


def _set_headers(client: Langsmith | AsyncLangsmith, headers: dict[str, str]) -> None:
    # Replace the snapshot, including credentials and headers that were removed.
    client.api_key = headers.get("X-API-Key")
    client.tenant_id = headers.get("X-Tenant-Id")
    client._custom_headers = dict(headers)


def _normalize_headers(headers: Mapping[str, str]) -> dict[str, str]:
    canonical_names = {
        "x-api-key": "X-API-Key",
        "x-tenant-id": "X-Tenant-Id",
        "x-stainless-os": "X-Stainless-OS",
    }
    return {canonical_names.get(name.lower(), name.title()): value for name, value in headers.items()}


def _copy_headers(headers: dict[str, str], options: dict[str, Any]) -> dict[str, str]:
    headers = _normalize_headers(headers)
    for option, header in (("api_key", "X-API-Key"), ("tenant_id", "X-Tenant-Id")):
        if options.get(option):
            headers[header] = options[option]
    if options.get("set_default_headers") is not None:
        headers = {key: value for key, value in headers.items() if key in ("X-API-Key", "X-Tenant-Id", "Authorization")}
        headers.update(_normalize_headers(options["set_default_headers"]))
    else:
        headers.update(_normalize_headers(options.get("default_headers") or {}))
    return headers


class SyncClient(Langsmith):
    def __init__(self, *, header_provider: Callable[[], dict[str, str]], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._header_provider = header_provider

    def copy(self, **kwargs: Any) -> Self:
        extra_kwargs = dict(kwargs.pop("_extra_kwargs", {}))
        extra_kwargs["header_provider"] = lambda: _copy_headers(self._header_provider(), kwargs)
        return super().copy(_extra_kwargs=extra_kwargs, **kwargs)

    with_options = copy

    def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        _set_headers(self, self._header_provider())
        return super()._prepare_options(options)

    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if not any(name.lower() == "authorization" and value for name, value in headers.items()):
            super()._validate_headers(headers, custom_headers)


class AsyncClient(AsyncLangsmith):
    def __init__(self, *, header_provider: Callable[[], Awaitable[dict[str, str]]], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._header_provider = header_provider

    def copy(self, **kwargs: Any) -> Self:
        async def header_provider() -> dict[str, str]:
            return _copy_headers(await self._header_provider(), kwargs)

        extra_kwargs = dict(kwargs.pop("_extra_kwargs", {}))
        extra_kwargs["header_provider"] = header_provider
        return super().copy(_extra_kwargs=extra_kwargs, **kwargs)

    with_options = copy

    async def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        _set_headers(self, await self._header_provider())
        return await super()._prepare_options(options)

    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if not any(name.lower() == "authorization" and value for name, value in headers.items()):
            super()._validate_headers(headers, custom_headers)
