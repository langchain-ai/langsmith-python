"""Test `Client(http_pool_kwargs=...)` reaching the urllib3 connection pools."""

import pickle
import socket
from typing import Any

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.connection import HTTPConnection

from langsmith import Client
from langsmith.client import URLLIB3_SUPPORTS_BLOCKSIZE, _LangSmithHttpAdapter

KEEPALIVE_OPTIONS = HTTPConnection.default_socket_options + [(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)]


def _client(**kwargs: Any) -> Client:
    return Client(api_url="http://localhost:1984", api_key="test", auto_batch_tracing=False, **kwargs)


def _pool_conn_kw(adapter: Any, url: str = "https://example.com") -> dict[str, Any]:
    assert isinstance(adapter, HTTPAdapter)
    return adapter.poolmanager.connection_from_url(url).conn_kw


def test_adapter_forwards_pool_kwargs() -> None:
    adapter = _LangSmithHttpAdapter(pool_kwargs={"socket_options": KEEPALIVE_OPTIONS})
    assert _pool_conn_kw(adapter)["socket_options"] == KEEPALIVE_OPTIONS


def test_adapter_default_is_unchanged() -> None:
    adapter = _LangSmithHttpAdapter()
    assert "socket_options" not in _pool_conn_kw(adapter)
    if URLLIB3_SUPPORTS_BLOCKSIZE:
        assert adapter.poolmanager.connection_pool_kw["blocksize"] == 16384


@pytest.mark.skipif(not URLLIB3_SUPPORTS_BLOCKSIZE, reason="urllib3 < 2 has no blocksize")
def test_caller_blocksize_wins() -> None:
    adapter = _LangSmithHttpAdapter(blocksize=16384, pool_kwargs={"blocksize": 4096})
    assert adapter.poolmanager.connection_pool_kw["blocksize"] == 4096


def test_adapter_applies_pool_kwargs_to_proxies() -> None:
    adapter = _LangSmithHttpAdapter(pool_kwargs={"socket_options": KEEPALIVE_OPTIONS})
    manager = adapter.proxy_manager_for("http://proxy.invalid:3128")
    assert manager.connection_pool_kw["socket_options"] == KEEPALIVE_OPTIONS


def test_adapter_pickle_keeps_pool_kwargs() -> None:
    adapter = _LangSmithHttpAdapter(pool_kwargs={"socket_options": KEEPALIVE_OPTIONS})
    restored = pickle.loads(pickle.dumps(adapter))
    assert _pool_conn_kw(restored)["socket_options"] == KEEPALIVE_OPTIONS


@pytest.mark.parametrize("own_session", [False, True])
def test_client_mounts_pool_kwargs(own_session: bool) -> None:
    session = requests.Session() if own_session else None
    client = _client(session=session, http_pool_kwargs={"socket_options": KEEPALIVE_OPTIONS})
    if own_session:
        assert client.session is session
    adapter = client.session.get_adapter("https://example.com")
    assert isinstance(adapter, _LangSmithHttpAdapter)
    assert client.session.get_adapter("http://example.com") is adapter
    assert _pool_conn_kw(adapter)["socket_options"] == KEEPALIVE_OPTIONS
