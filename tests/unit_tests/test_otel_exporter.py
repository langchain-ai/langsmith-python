"""Unit tests for OTEL exporter and span processor."""

import json
import os
import threading
import time
import uuid
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from langsmith import Client
from langsmith import utils as ls_utils
from langsmith._internal import _orjson
from langsmith._internal._operations import serialize_run_dict
from langsmith._internal.otel._otel_exporter import (
    GEN_AI_RESPONSE_FINISH_REASONS,
    GEN_AI_TOOL_CALL_ID,
    GEN_AI_TOOL_DEFINITIONS,
    GEN_AI_TOOL_NAME,
    OTELExporter,
)
from langsmith.integrations.otel import (
    otel_safe_attribute_value,
    set_langsmith_metadata_attribute,
)
from langsmith.integrations.otel.processor import OtelSpanProcessor


def test_cleanup_stale_spans():
    """Test cleanup of stale spans based on TTL."""
    with patch("langsmith._internal.otel._otel_exporter._import_otel_exporter") as mock_import:
        mock_import.return_value = (MagicMock(),) * 8

        exporter = OTELExporter(span_ttl_seconds=1)

        # Add stale and fresh spans
        stale_span = MagicMock()
        fresh_span = MagicMock()
        stale_id = uuid.uuid4()
        fresh_id = uuid.uuid4()

        exporter._span_info.set(stale_id, stale_span, created_at=time.time() - 2)
        exporter._span_info.set(fresh_id, fresh_span, created_at=time.time())
        exporter._last_cleanup = 0.0  # Force cleanup

        exporter._cleanup_stale_spans()

        # Verify cleanup
        assert exporter._span_info.get(stale_id) is None
        assert exporter._span_info.get(fresh_id) is not None
        stale_span.end.assert_called_once()
        fresh_span.end.assert_not_called()


def test_cleanup_periodic_behavior():
    """Test cleanup only runs periodically."""
    with patch("langsmith._internal.otel._otel_exporter._import_otel_exporter") as mock_import:
        mock_import.return_value = (MagicMock(),) * 8

        exporter = OTELExporter(span_ttl_seconds=1)
        stale_span = MagicMock()
        stale_id = uuid.uuid4()

        exporter._span_info.set(stale_id, stale_span, created_at=time.time() - 2)
        exporter._last_cleanup = time.time() - 5  # Recent cleanup

        exporter._cleanup_stale_spans()

        # Should not clean up due to periodic check
        assert exporter._span_info.get(stale_id) is not None
        stale_span.end.assert_not_called()


def test_cleanup_stale_spans_tolerates_concurrent_mutation():
    """Cleanup plus concurrent insert/delete from other batch workers must not
    raise ``RuntimeError: dictionary changed size during iteration`` or any
    ``KeyError``. The span info store locks all access and snapshots before
    iterating.
    """
    with patch("langsmith._internal.otel._otel_exporter._import_otel_exporter") as mock_import:
        mock_import.return_value = (MagicMock(),) * 8

        exporter = OTELExporter(span_ttl_seconds=1)
        exporter._last_cleanup = 0.0  # Force cleanup

        errors: list = []
        stop = threading.Event()

        # Seed one stale span so cleanup has work to do.
        exporter._span_info.set(uuid.uuid4(), MagicMock(), created_at=time.time() - 2)

        def mutator():
            while not stop.is_set():
                sid = uuid.uuid4()
                try:
                    exporter._span_info.set(sid, MagicMock())
                    exporter._span_info.pop(sid)
                except Exception as e:  # noqa: BLE001
                    errors.append(e)

        threads = [threading.Thread(target=mutator) for _ in range(4)]
        for t in threads:
            t.start()
        try:
            deadline = time.time() + 1.0
            while time.time() < deadline:
                exporter._cleanup_stale_spans()
        finally:
            stop.set()
            for t in threads:
                t.join(timeout=2)

        assert not errors, f"concurrent access raised: {errors}"


@patch("langsmith.utils.get_env_var")
def test_env_var_ttl(mock_get_env_var):
    """Test TTL loading from environment variable with correct default."""
    with patch("langsmith._internal.otel._otel_exporter._import_otel_exporter") as mock_import:
        mock_import.return_value = (MagicMock(),) * 8
        mock_get_env_var.return_value = "1800"

        exporter = OTELExporter()

        assert exporter._span_ttl_seconds == 1800
        mock_get_env_var.assert_any_call("OTEL_SPAN_TTL_SECONDS", default="3600")


def test_safe_attribute_value_preserves_primitives():
    """OTel-safe primitive values are returned unchanged."""
    for value in (True, b"bytes", 1, 1.5, "text"):
        safe_value = otel_safe_attribute_value(value)
        assert safe_value == value
        assert type(safe_value) is type(value)


class _Unserializable:
    def __repr__(self):
        return "unserializable"


def test_safe_attribute_value_serializes_structured_values():
    """Structured metadata values are converted to strings."""
    assert otel_safe_attribute_value(None) is None
    assert otel_safe_attribute_value({"nested": {"a": 1}}) == '{"nested":{"a":1}}'
    assert otel_safe_attribute_value(["a", 1]) == '["a",1]'
    assert otel_safe_attribute_value({"bad": _Unserializable()}) == "{'bad': unserializable}"


def test_set_langsmith_metadata_attribute_sets_safe_values():
    """Metadata helper sets converted attributes and skips None."""
    span = MagicMock()

    set_langsmith_metadata_attribute(span, "extra", {"a": 1})
    set_langsmith_metadata_attribute(span, "empty", None)

    span.set_attribute.assert_called_once_with("langsmith.metadata.extra", '{"a":1}')


@patch(
    "langsmith.integrations.otel.processor.OtelExporter",
    return_value=MagicMock(),
)
@patch(
    "langsmith.integrations.otel.processor.OTEL_AVAILABLE",
    True,
)
def test_set_metadata_propagates_to_spans(mock_exporter_cls):
    """Test that set_metadata propagates attributes to every span on_start."""
    mock_inner_processor = MagicMock()
    processor = OtelSpanProcessor(api_key="test", project="test", SpanProcessor=lambda _: mock_inner_processor)

    processor.set_metadata({"thread_id": "t-123", "session_id": "s-456", "extra": {"a": 1}})

    span = MagicMock()
    processor.on_start(span, parent_context=None)

    span.set_attribute.assert_any_call("langsmith.metadata.thread_id", "t-123")
    span.set_attribute.assert_any_call("langsmith.metadata.session_id", "s-456")
    span.set_attribute.assert_any_call("langsmith.metadata.extra", '{"a":1}')
    mock_inner_processor.on_start.assert_called_once_with(span, None)


# --- Tests for get_otlp_tracer_provider ---


def _make_mock_otel_imports():
    """Build mock return value for _import_otel_client."""
    MockExporter = MagicMock(name="OTLPSpanExporter")
    MockSERVICE_NAME = "service.name"
    MockResource = MagicMock(name="Resource")
    MockTracerProvider = MagicMock(name="TracerProvider")
    MockBatchSpanProcessor = MagicMock(name="BatchSpanProcessor")
    return (
        MockExporter,
        MockSERVICE_NAME,
        MockResource,
        MockTracerProvider,
        MockBatchSpanProcessor,
    )


def _make_exporter() -> OTELExporter:
    with patch(
        "langsmith._internal.otel._otel_exporter._import_otel_exporter",
        return_value=(MagicMock(),) * 8,
    ):
        return OTELExporter()


def _attributes_for_outputs(outputs: dict) -> dict:
    span = MagicMock()
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=None,
        outputs=json.dumps(outputs).encode(),
    )
    _make_exporter()._set_io_attributes(span, op)
    return {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}


def test_finish_reasons_preserve_all_openai_choices_as_a_list():
    attrs = _attributes_for_outputs(
        {
            "choices": [
                {"finish_reason": "stop"},
                {"finish_reason": "length"},
            ]
        }
    )

    assert attrs[GEN_AI_RESPONSE_FINISH_REASONS] == ["stop", "length"]


def test_finish_reasons_support_anthropic_and_gemini_shapes():
    assert _attributes_for_outputs({"stop_reason": "tool_use"})[GEN_AI_RESPONSE_FINISH_REASONS] == ["tool_use"]
    assert _attributes_for_outputs({"finish_reason": "STOP"})[GEN_AI_RESPONSE_FINISH_REASONS] == ["STOP"]


def test_choices_finish_reasons_take_precedence_over_top_level_reason():
    attrs = _attributes_for_outputs(
        {
            "choices": [{"finish_reason": "stop"}],
            "stop_reason": "tool_use",
            "finish_reason": "STOP",
        }
    )

    assert attrs[GEN_AI_RESPONSE_FINISH_REASONS] == ["stop"]


def test_missing_finish_reason_is_omitted_and_commas_are_not_split():
    assert GEN_AI_RESPONSE_FINISH_REASONS not in _attributes_for_outputs({"content": "hello"})
    assert _attributes_for_outputs({"stop_reason": "provider,custom"})[GEN_AI_RESPONSE_FINISH_REASONS] == [
        "provider,custom"
    ]


@pytest.mark.parametrize(
    "extra",
    [
        {"tool_call_id": "toolu_123", "metadata": {}},
        {"metadata": {"tool_call_id": "toolu_123"}},
    ],
    ids=["langchain", "metadata"],
)
def test_tool_attributes_use_run_name_and_tool_call_id(extra):
    span = MagicMock()
    op = SimpleNamespace(id=uuid.uuid4(), inputs=None, outputs=None, operation="post")
    _make_exporter()._set_span_attributes(
        span,
        {"run_type": "tool", "name": "Bash", "extra": extra},
        op,
    )

    calls = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert calls[GEN_AI_TOOL_NAME] == "Bash"
    assert calls[GEN_AI_TOOL_CALL_ID] == "toolu_123"


def test_tool_attributes_are_optional_and_tool_only():
    span = MagicMock()
    op = SimpleNamespace(id=uuid.uuid4(), inputs=None, outputs=None, operation="post")
    _make_exporter()._set_span_attributes(
        span,
        {"run_type": "tool", "name": "Bash", "extra": {"metadata": {}}},
        op,
    )
    _make_exporter()._set_span_attributes(
        span,
        {
            "run_type": "llm",
            "name": "model",
            "extra": {"metadata": {"tool_call_id": "toolu_123"}},
        },
        op,
    )

    keys = [call.args[0] for call in span.set_attribute.call_args_list]
    assert GEN_AI_TOOL_NAME in keys
    assert GEN_AI_TOOL_CALL_ID not in keys


def _attributes_for_run(run_info: dict) -> dict:
    span = MagicMock()
    op = SimpleNamespace(id=uuid.uuid4(), inputs=None, outputs=None, operation="post")
    _make_exporter()._set_span_attributes(span, run_info, op)
    return {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}


def test_tool_definitions_pass_through_provider_shapes():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the weather",
                "parameters": {"type": "object", "properties": {}},
            },
        },
        {"name": "search", "description": "Search", "input_schema": {}},
        {"type": "tool_search"},
    ]
    attrs = _attributes_for_run({"run_type": "llm", "extra": {"invocation_params": {"tools": tools}}})

    assert json.loads(attrs[GEN_AI_TOOL_DEFINITIONS]) == tools


@pytest.mark.parametrize(
    "extra",
    [{}, {"invocation_params": {}}, {"invocation_params": {"tools": []}}],
)
def test_tool_definitions_are_omitted_without_tools(extra):
    attrs = _attributes_for_run({"run_type": "llm", "extra": extra})

    assert GEN_AI_TOOL_DEFINITIONS not in attrs


def test_langchain_tool_attributes_reach_otel_spans():
    from langchain_core.language_models.fake_chat_models import (
        GenericFakeChatModel,
    )
    from langchain_core.messages import AIMessage
    from langchain_core.tools import tool
    from langchain_core.tracers.langchain import LangChainTracer
    from langchain_core.utils.function_calling import convert_to_openai_tool
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )

    @tool
    def get_weather(city: str) -> str:
        """Get the weather for a city."""
        return "sunny"

    provider = TracerProvider()
    sink = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(sink))
    client = Client(
        api_key="test",
        api_url="http://localhost:1984",
        tracing_mode="otel",
        otel_tracer_provider=provider,
    )
    tracer = LangChainTracer(client=client)
    tool_definition = convert_to_openai_tool(get_weather)
    try:
        model = GenericFakeChatModel(messages=iter([AIMessage("ok")]))
        model.bind(tools=[tool_definition]).invoke("hi", config={"callbacks": [tracer]})
        get_weather.invoke(
            {
                "type": "tool_call",
                "id": "call_123",
                "name": "get_weather",
                "args": {"city": "Paris"},
            },
            config={"callbacks": [tracer]},
        )
        tracer.wait_for_futures()
        client.flush()

        spans = {span.attributes["langsmith.span.kind"]: span.attributes for span in sink.get_finished_spans()}
        assert json.loads(spans["llm"][GEN_AI_TOOL_DEFINITIONS]) == [tool_definition]
        assert spans["tool"][GEN_AI_TOOL_CALL_ID] == "call_123"
    finally:
        provider.shutdown()


@patch("langsmith._internal.otel._otel_client._import_otel_client")
@patch("langsmith._internal.otel._otel_client.ls_utils")
def test_get_otlp_tracer_provider_does_not_mutate_env(mock_utils, mock_import):
    """Env vars must not be written by get_otlp_tracer_provider."""
    mock_import.return_value = _make_mock_otel_imports()
    mock_utils.get_api_url.return_value = "https://api.smith.langchain.com"
    mock_utils.get_api_key.return_value = "lsv2_pt_test123"
    mock_utils.get_tracer_project.return_value = "my-project"

    # Snapshot env before
    env_before = dict(os.environ)

    from langsmith._internal.otel._otel_client import get_otlp_tracer_provider

    get_otlp_tracer_provider()

    # These specific keys must not have been added
    assert "OTEL_EXPORTER_OTLP_ENDPOINT" not in os.environ
    assert "OTEL_EXPORTER_OTLP_HEADERS" not in os.environ

    # Restore env (safety)
    os.environ.clear()
    os.environ.update(env_before)


@patch("langsmith._internal.otel._otel_client._import_otel_client")
@patch("langsmith._internal.otel._otel_client.ls_utils")
def test_get_otlp_tracer_provider_passes_defaults_to_exporter(mock_utils, mock_import):
    """Default endpoint and headers are passed directly to OTLPSpanExporter."""
    mocks = _make_mock_otel_imports()
    mock_import.return_value = mocks
    MockExporter = mocks[0]

    mock_utils.get_api_url.return_value = "https://api.smith.langchain.com"
    mock_utils.get_api_key.return_value = "lsv2_pt_test123"
    mock_utils.get_tracer_project.return_value = "my-project"

    from langsmith._internal.otel._otel_client import get_otlp_tracer_provider

    get_otlp_tracer_provider()

    MockExporter.assert_called_once_with(
        endpoint="https://api.smith.langchain.com/otel/v1/traces",
        headers={"x-api-key": "lsv2_pt_test123", "Langsmith-Project": "my-project"},
    )


@patch("langsmith._internal.otel._otel_client._import_otel_client")
@patch("langsmith._internal.otel._otel_client.ls_utils")
def test_get_otlp_tracer_provider_honors_env_overrides(mock_utils, mock_import):
    """User-set OTEL env vars are read and passed through to the exporter."""
    mocks = _make_mock_otel_imports()
    mock_import.return_value = mocks
    MockExporter = mocks[0]

    env_patch = {
        "OTEL_EXPORTER_OTLP_ENDPOINT": "https://custom-collector:4318",
        "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer custom-token",
    }

    from langsmith._internal.otel._otel_client import get_otlp_tracer_provider

    with patch.dict(os.environ, env_patch):
        get_otlp_tracer_provider()

    MockExporter.assert_called_once_with(
        endpoint="https://custom-collector:4318/v1/traces",
        headers={"Authorization": "Bearer custom-token"},
    )
    # LangSmith utils should NOT have been called for key/endpoint
    mock_utils.get_api_key.assert_not_called()
    mock_utils.get_api_url.assert_not_called()


@patch("langsmith._internal.otel._otel_client._import_otel_client")
@patch("langsmith._internal.otel._otel_client.ls_utils")
def test_get_otlp_tracer_provider_no_project(mock_utils, mock_import):
    """When no project is configured, headers contain only the API key."""
    mocks = _make_mock_otel_imports()
    mock_import.return_value = mocks
    MockExporter = mocks[0]

    mock_utils.get_api_url.return_value = "https://api.smith.langchain.com"
    mock_utils.get_api_key.return_value = "lsv2_pt_test123"
    mock_utils.get_tracer_project.return_value = None

    from langsmith._internal.otel._otel_client import get_otlp_tracer_provider

    get_otlp_tracer_provider()

    MockExporter.assert_called_once_with(
        endpoint="https://api.smith.langchain.com/otel/v1/traces",
        headers={"x-api-key": "lsv2_pt_test123"},
    )


@pytest.mark.parametrize(
    ("endpoint_env", "expected_endpoint"),
    [
        ({}, "https://dev.api.smith.langchain.com/otel/v1/traces"),
        (
            {"OTEL_EXPORTER_OTLP_ENDPOINT": "https://collector:4318"},
            "https://collector:4318/v1/traces",
        ),
        (
            {"OTEL_EXPORTER_OTLP_ENDPOINT": "https://collector:4318/otel/"},
            "https://collector:4318/otel/v1/traces",
        ),
        (
            {"OTEL_EXPORTER_OTLP_ENDPOINT": "https://collector/otel/v1/traces"},
            "https://collector/otel/v1/traces",
        ),
        (
            {"OTEL_EXPORTER_OTLP_ENDPOINT": "https://collector/custom/traces"},
            "https://collector/custom/traces",
        ),
        (
            {"OTEL_EXPORTER_OTLP_ENDPOINT": "https://collector/not-traces"},
            "https://collector/not-traces/v1/traces",
        ),
        (
            {"OTEL_EXPORTER_OTLP_TRACES_ENDPOINT": "https://collector/custom/traces"},
            "https://collector/custom/traces",
        ),
        (
            {
                "OTEL_EXPORTER_OTLP_ENDPOINT": "https://ignored:4318/traces",
                "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT": "https://collector/otel/v1/traces",
            },
            "https://collector/otel/v1/traces",
        ),
    ],
)
def test_get_otlp_tracer_provider_resolves_real_exporter_endpoint(
    monkeypatch, endpoint_env, expected_endpoint, request
):
    from langsmith import utils as ls_utils
    from langsmith._internal.otel._otel_client import (
        _warn_legacy_traces_endpoint,
        get_otlp_tracer_provider,
    )

    _warn_legacy_traces_endpoint.cache_clear()
    ls_utils.get_env_var.cache_clear()
    request.addfinalizer(ls_utils.get_env_var.cache_clear)
    for name in ("OTEL_EXPORTER_OTLP_ENDPOINT", "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("LANGSMITH_ENDPOINT", "https://dev.api.smith.langchain.com")
    monkeypatch.setenv("LANGSMITH_API_KEY", "test-key")
    for name, value in endpoint_env.items():
        monkeypatch.setenv(name, value)
    env_before = dict(os.environ)

    with (
        patch("opentelemetry.sdk.trace.export.BatchSpanProcessor") as processor,
        patch("langsmith._internal.otel._otel_client.warnings.warn") as warn,
    ):
        for _ in range(2):
            provider = get_otlp_tracer_provider()
            exporter = processor.call_args.args[0]
            try:
                assert exporter._endpoint == expected_endpoint
                assert dict(os.environ) == env_before
            finally:
                exporter.shutdown()
                provider.shutdown()
        legacy_endpoint = endpoint_env.get("OTEL_EXPORTER_OTLP_ENDPOINT", "")
        should_warn = legacy_endpoint.endswith("/traces") and not endpoint_env.get("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT")
        assert warn.call_count == int(should_warn)
        if should_warn:
            assert "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT" in warn.call_args.args[0]
            assert "preserved unchanged" in warn.call_args.args[0]
            assert "removed in the v1 release" in warn.call_args.args[0]
    _warn_legacy_traces_endpoint.cache_clear()


def test_io_attributes_are_str_not_bytes():
    """Export input/output JSON strings regardless of OTel version."""
    with patch("langsmith._internal.otel._otel_exporter._import_otel_exporter") as mock_import:
        mock_import.return_value = (MagicMock(),) * 8
        exporter = OTELExporter(span_ttl_seconds=1)

    inputs = {"messages": [{"role": "user", "content": "こんにちは 🌍"}]}
    outputs = {"generations": [[{"text": "café ✅"}]]}
    span = MagicMock()
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps(inputs),
        outputs=_orjson.dumps(outputs),
    )

    exporter._set_io_attributes(span, op)

    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert isinstance(attrs["gen_ai.prompt"], str)
    assert isinstance(attrs["gen_ai.completion"], str)
    assert json.loads(attrs["gen_ai.prompt"]) == inputs
    assert json.loads(attrs["gen_ai.completion"]) == outputs


_AGENT_ENV = (
    "LANGSMITH_AGENT_ID",
    "LANGSMITH_AGENT_ENVIRONMENT",
    "LANGSMITH_PROJECT",
    "LANGCHAIN_PROJECT",
    "LANGCHAIN_SESSION",
    "OTEL_EXPORTER_OTLP_HEADERS",
    "OTEL_EXPORTER_OTLP_ENDPOINT",
)


@pytest.fixture
def set_env(monkeypatch):
    """Return a setter for the env a destination reads, from an empty start.

    The env lookups are cached, so the caches are cleared with every change and
    again afterwards.
    """

    def clear_caches():
        ls_utils.get_env_var.cache_clear()
        ls_utils.get_tracer_project.cache_clear()

    for name in _AGENT_ENV:
        monkeypatch.delenv(name, raising=False)

    def setter(env: dict) -> None:
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        clear_caches()

    setter({})
    yield setter
    monkeypatch.undo()
    clear_caches()


def _provider_headers(set_env, env: dict, project):
    set_env(env)
    mocks = _make_mock_otel_imports()
    with (
        patch(
            "langsmith._internal.otel._otel_client._import_otel_client",
            return_value=mocks,
        ),
        patch("langsmith._internal.otel._otel_client.ls_utils") as mock_utils,
    ):
        mock_utils.get_api_url.return_value = "https://api.smith.langchain.com"
        mock_utils.get_api_key.return_value = "lsv2_pt_test123"
        mock_utils.get_tracer_project.return_value = project
        from langsmith._internal.otel._otel_client import get_otlp_tracer_provider

        get_otlp_tracer_provider()
    return mocks[0].call_args.kwargs["headers"]


def test_tracer_provider_addresses_the_env_agent(set_env):
    headers = _provider_headers(
        set_env,
        {
            "LANGSMITH_AGENT_ID": "support-agent",
            "LANGSMITH_AGENT_ENVIRONMENT": "Staging",
        },
        project=None,
    )

    assert headers == {
        "x-api-key": "lsv2_pt_test123",
        "Langsmith-Agent-Id": "support-agent",
        "Langsmith-Agent-Environment": "staging",
    }


@pytest.mark.parametrize(
    "env, project",
    [
        ({"LANGSMITH_AGENT_ID": "support-agent"}, None),
        (
            {
                "LANGSMITH_AGENT_ID": "support-agent",
                "LANGSMITH_AGENT_ENVIRONMENT": "staging",
            },
            "my-project",
        ),
    ],
    ids=["half-an-address", "address-and-project"],
)
def test_tracer_provider_sends_no_destination_for_an_unusable_env(set_env, env, project):
    headers = _provider_headers(set_env, env, project)

    assert headers == {"x-api-key": "lsv2_pt_test123"}


def _otel_exporter_headers(**kwargs) -> dict:
    from langsmith.integrations.otel.processor import OtelExporter

    with patch(
        "langsmith.integrations.otel.processor.OTLPSpanExporter.__init__",
        return_value=None,
    ) as init:
        OtelExporter(api_key="lsv2_pt_test123", **kwargs)
    return init.call_args.kwargs["headers"]


def test_otel_exporter_addresses_an_agent(set_env):
    from langsmith.address import agent_address

    headers = _otel_exporter_headers(address=agent_address("support-agent", "production"))

    assert headers == {
        "x-api-key": "lsv2_pt_test123",
        "Langsmith-Agent-Id": "support-agent",
        "Langsmith-Agent-Environment": "production",
    }


def test_otel_exporter_takes_the_env_agent_when_nothing_is_named(set_env):
    set_env({"LANGSMITH_AGENT_ID": "support-agent", "LANGSMITH_AGENT_ENVIRONMENT": "local"})

    headers = _otel_exporter_headers()

    assert headers["Langsmith-Agent-Id"] == "support-agent"
    assert "Langsmith-Project" not in headers


def test_otel_exporter_keeps_the_project_default(set_env):
    headers = _otel_exporter_headers()

    assert headers == {"x-api-key": "lsv2_pt_test123", "Langsmith-Project": "default"}


def test_otel_exporter_rejects_a_project_and_an_address(set_env):
    from langsmith.address import agent_address
    from langsmith.utils import LangSmithUserError

    with pytest.raises(LangSmithUserError, match="both set"):
        _otel_exporter_headers(
            project="my-project",
            address=agent_address("support-agent", "production"),
        )


# --- Tests for token usage promotion (extra.metadata.usage_metadata fallback) ---


def _export_single_run(run_data: dict) -> list:
    """Serialize ``run_data`` as a 'post' op and export it through a real
    OTELExporter backed by a real OTEL SDK TracerProvider, returning the
    finished spans recorded by an in-memory span exporter.
    """
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )

    provider = TracerProvider()
    sink = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(sink))
    try:
        exporter = OTELExporter(tracer_provider=provider)
        op = serialize_run_dict("post", dict(run_data))
        exporter.export_batch([op], {})
        return list(sink.get_finished_spans())
    finally:
        provider.shutdown()


def _base_llm_run(**fields) -> dict:
    run_id = uuid.uuid4()
    trace_id = uuid.uuid4()
    return {
        "id": run_id,
        "trace_id": trace_id,
        "dotted_order": f"20240101T000000000000Z{trace_id}.{run_id}",
        "name": "example-turn",
        "run_type": "llm",
        "start_time": "2024-01-01T00:00:00+00:00",
        "end_time": "2024-01-01T00:00:01+00:00",
        "inputs": {"messages": [{"role": "user", "content": "hi"}]},
        **fields,
    }


def _extra_usage(input_tokens: int, output_tokens: int) -> dict:
    return {
        "metadata": {
            "usage_metadata": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens,
            }
        }
    }


def _usage_attributes(span) -> tuple:
    attributes = span.attributes
    return (
        attributes.get("gen_ai.usage.input_tokens"),
        attributes.get("gen_ai.usage.output_tokens"),
        attributes.get("gen_ai.usage.total_tokens"),
    )


def test_export_batch_promotes_usage_from_extra_metadata():
    """Usage recorded only under extra.metadata.usage_metadata (where
    ``RunTree.set(usage_metadata=...)`` and integrations such as
    claude_agent_sdk put it) is promoted to the gen_ai.usage.* span attributes.
    """
    run_data = _base_llm_run(
        # A turn's real output content, with no usage anywhere inside it.
        outputs={"content": [{"type": "text", "text": "hello"}], "role": "assistant"},
        extra=_extra_usage(21400, 7),
    )

    spans = _export_single_run(run_data)

    assert len(spans) == 1
    assert _usage_attributes(spans[0]) == (21400, 7, 21407)


def test_export_batch_promotes_usage_from_extra_metadata_without_outputs():
    """The fallback does not depend on outputs: an operation can carry usage
    in extra.metadata while having no outputs at all.
    """
    run_data = _base_llm_run(extra=_extra_usage(21400, 7))
    assert "outputs" not in run_data

    spans = _export_single_run(run_data)

    assert len(spans) == 1
    assert _usage_attributes(spans[0]) == (21400, 7, 21407)


def test_export_batch_outputs_usage_takes_precedence_over_extra_metadata():
    """Usage found in run.outputs wins over extra.metadata.usage_metadata."""
    run_data = _base_llm_run(
        outputs={"usage_metadata": {"input_tokens": 100, "output_tokens": 20, "total_tokens": 120}},
        extra=_extra_usage(999, 999),
    )

    spans = _export_single_run(run_data)

    assert len(spans) == 1
    assert _usage_attributes(spans[0]) == (100, 20, 120)


def test_export_batch_run_token_fields_take_precedence_over_extra_metadata():
    """The run's top-level token fields win over extra.metadata.usage_metadata."""
    run_data = _base_llm_run(
        outputs={"content": [{"type": "text", "text": "hello"}], "role": "assistant"},
        prompt_tokens=50,
        completion_tokens=5,
        total_tokens=55,
        extra=_extra_usage(999, 999),
    )

    spans = _export_single_run(run_data)

    assert len(spans) == 1
    assert _usage_attributes(spans[0]) == (50, 5, 55)


def test_export_batch_no_usage_anywhere_sets_no_usage_attributes():
    """No usage source present: no gen_ai.usage.* attributes are set."""
    run_data = _base_llm_run(
        outputs={"content": [{"type": "text", "text": "hi"}], "role": "assistant"},
        extra={"metadata": {}},
    )

    spans = _export_single_run(run_data)

    assert len(spans) == 1
    assert _usage_attributes(spans[0]) == (None, None, None)
