"""Integrations take an agent address wherever they take a project name."""

from unittest import mock

import pytest

import langsmith as ls
from langsmith import Client
from langsmith import utils as ls_utils
from langsmith._internal.voice.session import start_session
from langsmith.integrations.claude_agent_sdk._config import get_tracing_config, set_tracing_config
from langsmith.integrations.google_adk import _config as adk_config
from langsmith.integrations.google_adk._client import create_traced_session_context

SUPPORT = ls.agent_address("support", "production")
STAGING = ls.agent_address("support", "staging")


@pytest.fixture
def client() -> Client:
    return Client(session=mock.MagicMock(), api_key="test", api_url="http://x")


def test_voice_session_root_carries_the_address(client: Client) -> None:
    with mock.patch("langsmith.run_trees.RunTree.post"):
        session = start_session(thread_id="t", sample_rate=16000, address=SUPPORT, client=client, integration="test")
    assert session.run.address == SUPPORT


def test_voice_session_rejects_project_and_address(client: Client) -> None:
    with mock.patch("langsmith.run_trees.RunTree.post"):
        with pytest.raises(ls_utils.LangSmithUserError):
            start_session(
                thread_id="t",
                sample_rate=16000,
                project_name="p",
                address=SUPPORT,
                client=client,
                integration="test",
            )


def test_claude_agent_sdk_config_keeps_the_address() -> None:
    set_tracing_config(address=SUPPORT)
    try:
        assert get_tracing_config()["address"] == SUPPORT
    finally:
        set_tracing_config()


def test_google_adk_session_context_uses_configured_address(client: Client) -> None:
    adk_config.set_tracing_config(address=SUPPORT)
    try:
        with ls.tracing_context(enabled=True, client=client):
            with create_traced_session_context() as run:
                assert run.address == SUPPORT
            # A destination passed in replaces the configured one.
            with create_traced_session_context(project_name="p") as run:
                assert run.address is None
                assert run.session_name == "p"
            with create_traced_session_context(address=STAGING) as run:
                assert run.address == STAGING
    finally:
        adk_config.set_tracing_config()


def test_positional_arguments_keep_their_order() -> None:
    set_tracing_config("name", "project", {"k": "v"}, ["tag"])
    try:
        config = get_tracing_config()
        assert (config["metadata"], config["tags"], config["address"]) == ({"k": "v"}, ["tag"], None)
    finally:
        set_tracing_config()
    adk_config.set_tracing_config("name", "project", {"k": "v"}, ["tag"])
    try:
        config = adk_config.get_tracing_config()
        assert (config["metadata"], config["tags"], config["address"]) == ({"k": "v"}, ["tag"], None)
    finally:
        adk_config.set_tracing_config()
