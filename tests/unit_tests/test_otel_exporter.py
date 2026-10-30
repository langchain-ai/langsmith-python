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
from langsmith._internal.otel._otel_exporter import (
    GEN_AI_RESPONSE_FINISH_REASONS,
    GEN_AI_TOOL_CALL_ID,
    GEN_AI_TOOL_DEFINITIONS,
    GEN_AI_TOOL_NAME,
    OTELExporter,
    _get_gen_ai_input_messages,
)
from langsmith.integrations.otel import (
    otel_safe_attribute_value,
    set_langsmith_metadata_attribute,
)
from langsmith.integrations.otel.processor import OtelSpanProcessor


def _attribute_value(span: MagicMock, name: str) -> object:
    """Return the last value assigned to an attribute on a mock span."""
    matches = [call.args[1] for call in span.set_attribute.call_args_list if call.args[0] == name]
    assert matches, f"attribute {name!r} was not set"
    return matches[-1]


def test_set_io_attributes_converts_langchain_input_messages_to_gen_ai_schema():
    """LangChain constructor messages are exported using the current OTel schema."""
    exporter = object.__new__(OTELExporter)
    span = MagicMock()
    inputs = {
        "messages": [
            [
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": ["langchain", "schema", "messages", "HumanMessage"],
                    "kwargs": {"content": "What is 2 + 2?", "type": "human"},
                }
            ]
        ]
    }
    op = SimpleNamespace(id=uuid.uuid4(), inputs=_orjson.dumps(inputs), outputs=None)

    exporter._set_io_attributes(span, op)

    assert json.loads(
        _attribute_value(span, "gen_ai.input.messages")  # type: ignore[arg-type]
    ) == [
        {
            "role": "user",
            "parts": [{"type": "text", "content": "What is 2 + 2?"}],
        }
    ]
    assert _attribute_value(span, "gen_ai.prompt") == _orjson.dumps(inputs).decode("utf-8")


def test_set_io_attributes_converts_langchain_generations_to_gen_ai_schema():
    """LangChain chat generations are exported using the current OTel schema."""
    exporter = object.__new__(OTELExporter)
    span = MagicMock()
    outputs = {
        "generations": [
            [
                {
                    "text": "4",
                    "type": "ChatGeneration",
                    "generation_info": {"finish_reason": "stop"},
                    "message": {
                        "lc": 1,
                        "type": "constructor",
                        "id": ["langchain", "schema", "messages", "AIMessage"],
                        "kwargs": {"content": "4", "type": "ai"},
                    },
                }
            ]
        ]
    }
    op = SimpleNamespace(id=uuid.uuid4(), inputs=None, outputs=_orjson.dumps(outputs))

    exporter._set_io_attributes(span, op)

    assert json.loads(
        _attribute_value(span, "gen_ai.output.messages")  # type: ignore[arg-type]
    ) == [
        {
            "role": "assistant",
            "parts": [{"type": "text", "content": "4"}],
            "finish_reason": "stop",
        }
    ]
    assert _attribute_value(span, "gen_ai.completion") == _orjson.dumps(outputs).decode("utf-8")


def test_set_io_attributes_converts_tool_call_history_to_gen_ai_schema():
    """Tool requests and responses are represented as typed GenAI parts."""
    exporter = object.__new__(OTELExporter)
    span = MagicMock()
    inputs = {
        "messages": [
            [
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": ["langchain", "schema", "messages", "AIMessage"],
                    "kwargs": {
                        "content": "",
                        "type": "ai",
                        "tool_calls": [
                            {
                                "name": "calculator",
                                "args": {"expression": "2 + 2"},
                                "id": "call_1",
                                "type": "tool_call",
                            }
                        ],
                    },
                },
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": ["langchain", "schema", "messages", "ToolMessage"],
                    "kwargs": {
                        "content": "4",
                        "type": "tool",
                        "tool_call_id": "call_1",
                    },
                },
            ]
        ]
    }
    op = SimpleNamespace(id=uuid.uuid4(), inputs=_orjson.dumps(inputs), outputs=None)

    exporter._set_io_attributes(span, op)

    assert json.loads(
        _attribute_value(span, "gen_ai.input.messages")  # type: ignore[arg-type]
    ) == [
        {
            "role": "assistant",
            "parts": [
                {"type": "text", "content": ""},
                {
                    "type": "tool_call",
                    "id": "call_1",
                    "name": "calculator",
                    "arguments": {"expression": "2 + 2"},
                },
            ],
        },
        {
            "role": "tool",
            "parts": [
                {
                    "type": "tool_call_response",
                    "id": "call_1",
                    "response": "4",
                }
            ],
        },
    ]


def test_set_io_attributes_converts_provider_style_tool_calls():
    """Provider-style tool arguments are decoded into structured GenAI parts."""
    exporter = object.__new__(OTELExporter)
    span = MagicMock()
    inputs = {
        "messages": [
            [
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": ["langchain", "schema", "messages", "AIMessage"],
                    "kwargs": {
                        "content": "",
                        "type": "ai",
                        "additional_kwargs": {
                            "tool_calls": [
                                {
                                    "id": "call_1",
                                    "type": "function",
                                    "function": {
                                        "name": "calculator",
                                        "arguments": '{"expression":"2 + 2"}',
                                    },
                                }
                            ]
                        },
                    },
                }
            ]
        ]
    }
    op = SimpleNamespace(id=uuid.uuid4(), inputs=_orjson.dumps(inputs), outputs=None)

    exporter._set_io_attributes(span, op)

    assert json.loads(
        _attribute_value(span, "gen_ai.input.messages")  # type: ignore[arg-type]
    ) == [
        {
            "role": "assistant",
            "parts": [
                {"type": "text", "content": ""},
                {
                    "type": "tool_call",
                    "id": "call_1",
                    "name": "calculator",
                    "arguments": {"expression": "2 + 2"},
                },
            ],
        }
    ]


def test_set_io_attributes_converts_tool_call_generation_to_gen_ai_schema():
    """A tool-only model generation is retained with a normalized finish reason."""
    exporter = object.__new__(OTELExporter)
    span = MagicMock()
    outputs = {
        "generations": [
            [
                {
                    "text": "",
                    "type": "ChatGeneration",
                    "generation_info": {"finish_reason": "tool_calls"},
                    "message": {
                        "lc": 1,
                        "type": "constructor",
                        "id": ["langchain", "schema", "messages", "AIMessage"],
                        "kwargs": {
                            "content": "",
                            "type": "ai",
                            "tool_calls": [
                                {
                                    "name": "calculator",
                                    "args": {"expression": "2 + 2"},
                                    "id": "call_1",
                                    "type": "tool_call",
                                }
                            ],
                        },
                    },
                }
            ]
        ]
    }
    op = SimpleNamespace(id=uuid.uuid4(), inputs=None, outputs=_orjson.dumps(outputs))

    exporter._set_io_attributes(span, op)

    assert json.loads(
        _attribute_value(span, "gen_ai.output.messages")  # type: ignore[arg-type]
    ) == [
        {
            "role": "assistant",
            "parts": [
                {"type": "text", "content": ""},
                {
                    "type": "tool_call",
                    "id": "call_1",
                    "name": "calculator",
                    "arguments": {"expression": "2 + 2"},
                },
            ],
            "finish_reason": "tool_call",
        }
    ]


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


@pytest.mark.parametrize(
    ("message_class", "kwargs", "expected"),
    [
        ("AIMessageChunk", {"content": "hi"}, {"role": "assistant", "parts": [{"type": "text", "content": "hi"}]}),
        ("HumanMessageChunk", {"content": "hi"}, {"role": "user", "parts": [{"type": "text", "content": "hi"}]}),
        (
            "ToolMessageChunk",
            {"content": "x", "tool_call_id": "c1"},
            {"role": "tool", "parts": [{"type": "tool_call_response", "response": "x", "id": "c1"}]},
        ),
        (
            "ChatMessage",
            {"content": "x", "role": "moderator"},
            {"role": "moderator", "parts": [{"type": "text", "content": "x"}]},
        ),
        (
            "ChatMessageChunk",
            {"content": "x", "role": "Message Reviewer"},
            {"role": "Message Reviewer", "parts": [{"type": "text", "content": "x"}]},
        ),
        (
            "ChatMessage",
            {"content": "x", "role": "HUMAN"},
            {"role": "user", "parts": [{"type": "text", "content": "x"}]},
        ),
        ("HumanMessage", {"content": ""}, {"role": "user", "parts": [{"type": "text", "content": ""}]}),
        ("SystemMessage", {"content": ""}, {"role": "system", "parts": [{"type": "text", "content": ""}]}),
        (
            "ToolMessage",
            {"content": "", "tool_call_id": "c1"},
            {"role": "tool", "parts": [{"type": "tool_call_response", "response": "", "id": "c1"}]},
        ),
        (
            "FunctionMessage",
            {"content": "", "name": "f"},
            {"role": "tool", "parts": [{"type": "tool_call_response", "response": ""}]},
        ),
    ],
)
def test_gen_ai_input_messages_preserve_serialized_roles_and_empty_content(
    message_class: str, kwargs: dict, expected: dict
):
    from langchain_core import messages
    from langchain_core.load.dump import dumpd

    message = getattr(messages, message_class)(**kwargs)

    assert _get_gen_ai_input_messages({"messages": [dumpd(message)]}) == [expected]


@pytest.mark.parametrize(
    "message",
    [
        {"type": "AIMessageChunk", "data": {"content": "hi"}},
        {"lc": 1, "id": ["langchain", "schema", "messages", "AIMessageChunk"], "kwargs": {"content": "hi"}},
    ],
)
def test_gen_ai_input_messages_keep_known_type_and_class_fallbacks(message: dict):
    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {"role": "assistant", "parts": [{"type": "text", "content": "hi"}]}
    ]


def test_gen_ai_input_messages_preserve_order_without_exporting_control_types():
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage

    messages = [
        dumpd(HumanMessage(content="first")),
        dumpd(RemoveMessage(id="old-message")),
        {"type": "FutureInternalMessage", "content": "internal"},
        dumpd(AIMessage(content="last")),
    ]

    assert _get_gen_ai_input_messages({"messages": [messages]}) == [
        {"role": "user", "parts": [{"type": "text", "content": "first"}]},
        {"role": "assistant", "parts": [{"type": "text", "content": "last"}]},
    ]


@pytest.mark.parametrize("direction", ["input", "output"])
@pytest.mark.parametrize(
    ("content", "expected_parts"),
    [
        ("", [{"type": "text", "content": ""}]),
        (["", {"type": "text", "text": ""}], [{"type": "text", "content": ""}, {"type": "text", "content": ""}]),
        (
            [{"type": "image_url", "image_url": {"url": "data:image/png;base64,aGVsbG8="}}],
            [{"type": "image_url", "image_url": {"url": "data:image/png;base64,aGVsbG8="}}],
        ),
        (
            [{"type": "reasoning", "content": "thinking"}, {"type": "text", "text": "answer"}],
            [{"type": "reasoning", "content": "thinking"}, {"type": "text", "content": "answer"}],
        ),
        ([{"foo": "bar"}], []),
        (
            [{"foo": "bar"}, {"type": "text", "text": "answer"}, {"type": 123}],
            [{"type": "text", "content": "answer"}],
        ),
    ],
    ids=["empty-text", "empty-text-blocks", "image", "reasoning-order", "untyped-only", "mixed-untyped"],
)
def test_set_io_attributes_preserves_message_content(direction: str, content: object, expected_parts: list):
    role = "user" if direction == "input" else "assistant"
    message = {"role": role, "content": content}
    inputs = {"messages": [message]}
    outputs = {"generations": [{"message": message, "generation_info": {"finish_reason": "stop"}}]}
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps(inputs) if direction == "input" else None,
        outputs=_orjson.dumps(outputs) if direction == "output" else None,
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    expected = {"role": role, "parts": expected_parts}
    if direction == "output":
        expected["finish_reason"] = "stop"
    assert json.loads(attrs[f"gen_ai.{direction}.messages"]) == [expected]


@pytest.mark.parametrize("direction", ["input", "output"])
@pytest.mark.parametrize(
    ("content_calls", "metadata_calls", "expected_parts"),
    [
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [{"name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "c1"},
                {"type": "text", "content": "after"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": None}],
            [{"name": "calculator", "args": {"x": 1}, "id": None}],
            [{"type": "tool_call", "name": "calculator", "arguments": {"x": 1}}, {"type": "text", "content": "after"}],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "c1"},
                {"type": "text", "content": "after"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [
                {"name": "calculator", "args": {"x": 1}, "id": "c1"},
                {"name": "calculator", "args": {"x": 2}, "id": "c2"},
            ],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "c1"},
                {"type": "text", "content": "after"},
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 2}, "id": "c2"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": None}],
            [{"name": "calculator", "args": {"x": 2}, "id": None}],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}},
                {"type": "text", "content": "after"},
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 2}},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": None}],
            [
                {"name": "calculator", "args": {"x": 1}, "id": None},
                {"name": "calculator", "args": {"x": 1}, "id": None},
            ],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}},
                {"type": "text", "content": "after"},
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}},
            ],
        ),
        (
            [{"type": "tool_call", "args": {"x": 1}, "id": "c1"}],
            [{"name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [
                {"type": "text", "content": "after"},
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "c1"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "", "args": {"x": 1}, "id": "c1"}],
            [],
            [{"type": "text", "content": "after"}],
        ),
        (
            [{"type": "tool_call", "args": {"x": 1}, "id": 7}],
            [{"name": "calculator", "args": {"x": 1}, "id": "7"}],
            [
                {"type": "text", "content": "after"},
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "7"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [{"name": "calculator", "args": {"x": 2}, "id": "c1"}],
            [
                {"type": "tool_call", "name": "calculator", "arguments": {"x": 1}, "id": "c1"},
                {"type": "text", "content": "after"},
            ],
        ),
        (
            [{"type": "tool_call", "name": "calculator", "id": "c1"}],
            [{"name": "calculator", "args": {"x": 1}, "id": "c1"}],
            [
                {"type": "tool_call", "name": "calculator", "id": "c1"},
                {"type": "text", "content": "after"},
            ],
        ),
    ],
    ids=[
        "mirrored-id",
        "mirrored-no-id",
        "content-only",
        "partial-overlap",
        "distinct-no-id",
        "repeated-no-id",
        "missing-name",
        "empty-name",
        "raw-numeric-id",
        "conflicting-arguments",
        "missing-content-arguments",
    ],
)
def test_set_io_attributes_merges_content_and_metadata_tool_calls(
    direction: str, content_calls: list, metadata_calls: list, expected_parts: list
):
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage

    message = dumpd(
        AIMessage(
            content_blocks=[{"type": "text", "text": "before"}, *content_calls, {"type": "text", "text": "after"}],
            tool_calls=metadata_calls,
        )
    )
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [message]}) if direction == "input" else None,
        outputs=_orjson.dumps(
            {"generations": [{"message": message, "generation_info": {"finish_reason": "tool_calls"}}]}
        )
        if direction == "output"
        else None,
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    expected = {"role": "assistant", "parts": [{"type": "text", "content": "before"}, *expected_parts]}
    if direction == "output":
        expected["finish_reason"] = "tool_call"
    assert json.loads(attrs[f"gen_ai.{direction}.messages"]) == [expected]


@pytest.mark.parametrize(
    "content_fields",
    [
        {"input": {"city": "SF"}},
        {},
        {"input": {}},
        {"input": None},
        {"input": {}, "partial_json": '{"city":'},
        {"input": {"city": "NY"}},
    ],
    ids=["complete", "missing-input", "empty-input", "null-input", "partial-json", "conflicting-input"],
)
def test_set_io_attributes_prefers_metadata_for_mirrored_tool_use(content_fields: dict):
    # Unlike normalized tool_call content, native tool_use defers to parsed metadata.
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage

    message = dumpd(
        AIMessage(
            content=[
                {"type": "text", "text": "before"},
                {"type": "tool_use", "id": "toolu_1", "name": "get_weather", **content_fields},
                {"type": "text", "text": "after"},
            ],
            tool_calls=[{"id": "toolu_1", "name": "get_weather", "args": {"city": "SF"}}],
        )
    )
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [[message]]}),
        outputs=_orjson.dumps({"generations": [[{"message": message}]]}),
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    expected = {
        "role": "assistant",
        "parts": [
            {"type": "text", "content": "before"},
            {"type": "tool_call", "id": "toolu_1", "name": "get_weather", "arguments": {"city": "SF"}},
            {"type": "text", "content": "after"},
        ],
    }
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert json.loads(attrs["gen_ai.input.messages"]) == [expected]
    assert json.loads(attrs["gen_ai.output.messages"]) == [{**expected, "finish_reason": "tool_call"}]


def test_set_io_attributes_preserves_merged_tool_use_chunk_arguments():
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessageChunk

    start = AIMessageChunk(
        content=[{"type": "tool_use", "index": 0, "id": "toolu_1", "name": "get_weather", "input": {}}],
        tool_call_chunks=[{"index": 0, "id": "toolu_1", "name": "get_weather", "args": ""}],
    )
    delta = AIMessageChunk(
        content=[{"type": "input_json_delta", "index": 0, "partial_json": '{"city":"SF"}'}],
        tool_call_chunks=[{"index": 0, "id": None, "name": None, "args": '{"city":"SF"}'}],
    )
    merged = start + delta
    assert merged.content[0]["input"] == {}
    assert merged.tool_calls[0]["args"] == {"city": "SF"}
    message = dumpd(merged)
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [[message]]}),
        outputs=_orjson.dumps({"generations": [[{"message": message}]]}),
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    expected = {
        "role": "assistant",
        "parts": [{"type": "tool_call", "id": "toolu_1", "name": "get_weather", "arguments": {"city": "SF"}}],
    }
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert json.loads(attrs["gen_ai.input.messages"]) == [expected]
    assert json.loads(attrs["gen_ai.output.messages"]) == [{**expected, "finish_reason": "tool_call"}]


@pytest.mark.parametrize(
    ("content_count", "metadata_arguments", "expected_arguments"),
    [
        (2, [{"a": 1}], [{"a": 1}, None]),
        (1, [{"a": 1}, {"a": 99}], [{"a": 1}, {"a": 99}]),
        (2, [{"a": 1}, {"a": 99}], [{"a": 1}, {"a": 99}]),
    ],
    ids=["repeated-content", "repeated-metadata", "repeated-both"],
)
@pytest.mark.parametrize(
    "block",
    [
        {"type": "tool_use", "id": "t1", "name": "f", "input": {}},
        {"type": "function_call", "id": "fc_item_1", "call_id": "t1", "name": "f", "arguments": "{}"},
        {"type": "custom_tool_call", "id": "ctc_item_1", "call_id": "t1", "name": "f", "input": "print(1)"},
    ],
    ids=["tool_use", "function_call", "custom_tool_call"],
)
def test_gen_ai_input_messages_match_provider_tool_calls_once(
    content_count: int, metadata_arguments: list, expected_arguments: list, block: dict
):
    message = {
        "role": "assistant",
        "content": [dict(block) for _ in range(content_count)],
        "tool_calls": [{"id": "t1", "name": "f", "args": args} for args in metadata_arguments],
    }

    parts = _get_gen_ai_input_messages({"messages": [message]})[0]["parts"]

    assert parts == [
        {"type": "tool_call", "id": "t1", "name": "f", "arguments": args} if args is not None else block
        for args in expected_arguments
    ]
    assert parts[0] is not parts[1]
    assert message["content"] == [block] * content_count


@pytest.mark.parametrize("metadata_fields", [{}, {"args": None}, {"args": {}}], ids=["missing", "null", "empty"])
def test_set_io_attributes_retains_tool_use_input_when_metadata_arguments_are_empty(metadata_fields: dict):
    message = {
        "role": "assistant",
        "content": [{"type": "tool_use", "id": "t1", "name": "f", "input": {"city": "SF"}}],
        "tool_calls": [{"id": "t1", "name": "f", **metadata_fields}],
    }
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [message]}),
        outputs=_orjson.dumps({"generations": [{"message": message}]}),
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    expected = {
        "role": "assistant",
        "parts": [{"type": "tool_call", "id": "t1", "name": "f", "arguments": {"city": "SF"}}],
    }
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert json.loads(attrs["gen_ai.input.messages"]) == [expected]
    assert json.loads(attrs["gen_ai.output.messages"]) == [{**expected, "finish_reason": "tool_call"}]


@pytest.mark.parametrize(
    "id_fields", [{"id": "other-call"}, {}, {"id": None}], ids=["different-id", "missing-id", "null-id"]
)
def test_gen_ai_input_messages_preserve_unmatched_tool_use(id_fields: dict):
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage

    block = {
        "type": "tool_use",
        **id_fields,
        "name": "get_weather",
        "input": {},
        "partial_json": '{"city":"SF"}',
        "index": 0,
        "cache_control": {"type": "ephemeral"},
    }
    message = dumpd(
        AIMessage(
            content=[block],
            tool_calls=[{"id": "toolu_1", "name": "get_weather", "args": {"city": "SF"}}],
        )
    )

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [
                block,
                {"type": "tool_call", "id": "toolu_1", "name": "get_weather", "arguments": {"city": "SF"}},
            ],
        }
    ]


@pytest.mark.parametrize(
    "content_fields",
    [{"input": '{"a":1}'}, {"input": {}, "partial_json": '{"city":"SF"}'}],
    ids=["string-input", "partial-json-only"],
)
def test_gen_ai_input_messages_do_not_parse_tool_use_argument_fallbacks(content_fields: dict):
    message = {
        "role": "assistant",
        "content": [{"type": "tool_use", "id": "t1", "name": "f", **content_fields}],
        "tool_calls": [{"id": "t1", "name": "f"}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {"role": "assistant", "parts": [{"type": "tool_call", "id": "t1", "name": "f"}]}
    ]


def test_gen_ai_input_messages_keep_unmatched_tool_use_and_metadata_without_ids():
    block = {"type": "tool_use", "name": "f", "input": {"a": 1}}
    message = {
        "role": "assistant",
        "content": [block],
        "tool_calls": [{"name": "f", "args": {"a": 1}}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {"role": "assistant", "parts": [block, {"type": "tool_call", "name": "f", "arguments": {"a": 1}}]}
    ]


@pytest.mark.parametrize("streamed", [False, True], ids=["message", "merged-chunk"])
def test_set_io_attributes_merges_responses_function_calls(streamed: bool):
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage, AIMessageChunk

    block = {
        "type": "function_call",
        "id": "fc_item_1",
        "call_id": "call_1",
        "name": "get_weather",
        "arguments": '{"city":"SF"}',
    }
    if streamed:
        start = AIMessageChunk(
            content=[{"type": "text", "text": "before"}, {**block, "index": 1, "arguments": ""}],
            tool_call_chunks=[{"index": 1, "id": "call_1", "name": "get_weather", "args": ""}],
        )
        delta = AIMessageChunk(
            content=[{"type": "function_call", "index": 1, "arguments": '{"city":"SF"}'}],
            tool_call_chunks=[{"index": 1, "id": None, "name": None, "args": '{"city":"SF"}'}],
        )
        message = start + delta
        # Pin the upstream merge preconditions this exporter depends on.
        assert message.content[1]["call_id"] == "call_1"
        assert message.content[1]["id"] == "fc_item_1"
        assert message.tool_calls[0]["args"] == {"city": "SF"}
    else:
        message = AIMessage(
            content=[{"type": "text", "text": "before"}, block],
            tool_calls=[{"id": "call_1", "name": "get_weather", "args": {"city": "SF"}}],
        )
    serialized = dumpd(message)
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [[serialized]]}),
        outputs=_orjson.dumps({"generations": [[{"message": serialized}]]}),
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    expected = {
        "role": "assistant",
        "parts": [
            {"type": "text", "content": "before"},
            {"type": "tool_call", "id": "call_1", "name": "get_weather", "arguments": {"city": "SF"}},
        ],
    }
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert json.loads(attrs["gen_ai.input.messages"]) == [expected]
    assert json.loads(attrs["gen_ai.output.messages"]) == [{**expected, "finish_reason": "tool_call"}]
    assert attrs["gen_ai.prompt"] == op.inputs.decode("utf-8")
    assert attrs["gen_ai.completion"] == op.outputs.decode("utf-8")


@pytest.mark.parametrize(
    "call_id_fields", [{}, {"call_id": None}, {"call_id": "other-call"}], ids=["missing", "null", "different"]
)
@pytest.mark.parametrize(
    "block_fields",
    [{"type": "function_call", "arguments": '{"a":1}'}, {"type": "custom_tool_call", "input": "print(1)"}],
    ids=["function_call", "custom_tool_call"],
)
def test_gen_ai_input_messages_do_not_match_responses_item_ids(call_id_fields: dict, block_fields: dict):
    # The item id deliberately equals the metadata id; it must never substitute for call_id.
    block = {"id": "call_1", "name": "f", **block_fields, **call_id_fields}
    original_block = dict(block)
    message = {
        "role": "assistant",
        "content": [block],
        "tool_calls": [{"id": "call_1", "name": "f", "args": {"a": 1}}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [block, {"type": "tool_call", "id": "call_1", "name": "f", "arguments": {"a": 1}}],
        }
    ]
    assert block == original_block


@pytest.mark.parametrize("streamed", [False, True], ids=["message", "stream-chunk"])
@pytest.mark.parametrize("text", ['print("hello")', ""], ids=["free-text", "empty-text"])
def test_set_io_attributes_merges_responses_custom_tool_calls(streamed: bool, text: str):
    from langchain_core.load.dump import dumpd
    from langchain_core.messages import AIMessage, AIMessageChunk

    block = {"type": "custom_tool_call", "id": "ctc_item_1", "call_id": "call_1", "name": "python", "input": text}
    if streamed:
        # LangChain emits the full custom-tool input with the output_item.done event.
        message = (
            AIMessageChunk(content=[{"type": "text", "text": "before"}])
            + AIMessageChunk(
                content=[{**block, "index": 1}],
                tool_call_chunks=[{"index": 1, "id": "call_1", "name": "python", "args": json.dumps({"__arg1": text})}],
            )
            + AIMessageChunk(content=[{"type": "text", "text": "after"}])
        )
        # Pin the upstream merge preconditions this exporter depends on.
        assert message.content[1]["call_id"] == "call_1"
        assert message.content[1]["id"] == "ctc_item_1"
        assert message.tool_calls[0]["args"] == {"__arg1": text}
    else:
        content = [{"type": "text", "text": "before"}, block, {"type": "text", "text": "after"}]
        message = AIMessage(content=content, tool_calls=[{"id": "call_1", "name": "python", "args": {"__arg1": text}}])
    serialized = dumpd(message)
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps({"messages": [[serialized]]}),
        outputs=_orjson.dumps({"generations": [[{"message": serialized}]]}),
    )
    span = MagicMock()

    _make_exporter()._set_io_attributes(span, op)

    expected = {
        "role": "assistant",
        "parts": [
            {"type": "text", "content": "before"},
            {"type": "tool_call", "id": "call_1", "name": "python", "arguments": {"__arg1": text}},
            {"type": "text", "content": "after"},
        ],
    }
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    assert json.loads(attrs["gen_ai.input.messages"]) == [expected]
    assert json.loads(attrs["gen_ai.output.messages"]) == [{**expected, "finish_reason": "tool_call"}]


@pytest.mark.parametrize("metadata_fields", [{}, {"args": None}, {"args": {}}], ids=["missing", "null", "empty"])
@pytest.mark.parametrize("text", ["print(1)", ""], ids=["free-text", "empty-text"])
def test_gen_ai_input_messages_fill_empty_metadata_from_custom_tool_input(metadata_fields: dict, text: str):
    message = {
        "role": "assistant",
        "content": [{"type": "custom_tool_call", "call_id": "call_1", "name": "python", "input": text}],
        "tool_calls": [{"id": "call_1", "name": "python", **metadata_fields}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [{"type": "tool_call", "id": "call_1", "name": "python", "arguments": {"__arg1": text}}],
        }
    ]


@pytest.mark.parametrize(
    "input_fields", [{}, {"input": None}, {"input": {"a": 1}}], ids=["missing", "null", "non-string"]
)
def test_gen_ai_input_messages_skip_unusable_custom_tool_input_fallbacks(input_fields: dict):
    message = {
        "role": "assistant",
        "content": [{"type": "custom_tool_call", "call_id": "call_1", "name": "python", **input_fields}],
        "tool_calls": [{"id": "call_1", "name": "python"}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {"role": "assistant", "parts": [{"type": "tool_call", "id": "call_1", "name": "python"}]}
    ]


@pytest.mark.parametrize("metadata_fields", [{}, {"args": None}, {"args": {}}], ids=["missing", "null", "empty"])
def test_gen_ai_input_messages_fill_empty_metadata_from_responses_arguments(metadata_fields: dict):
    message = {
        "role": "assistant",
        "content": [
            {"type": "function_call", "id": "fc_item_1", "call_id": "call_1", "name": "f", "arguments": '{"city":"SF"}'}
        ],
        "tool_calls": [{"id": "call_1", "name": "f", **metadata_fields}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [{"type": "tool_call", "id": "call_1", "name": "f", "arguments": {"city": "SF"}}],
        }
    ]


@pytest.mark.parametrize(
    ("arguments", "metadata_fields", "expected_part"),
    [
        ('{"city":', {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ('{"city":', {"args": None}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ('{"city":', {"args": {}}, {"type": "tool_call", "id": "call_1", "name": "f", "arguments": {}}),
        ("", {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ("5", {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ("[1,2]", {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ("{}", {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
        ("null", {}, {"type": "tool_call", "id": "call_1", "name": "f"}),
    ],
    ids=[
        "partial-json-missing-metadata-arguments",
        "partial-json-null-metadata-arguments",
        "partial-json-empty-metadata-arguments",
        "empty-string",
        "scalar",
        "array",
        "empty-object",
        "null",
    ],
)
def test_gen_ai_input_messages_skip_unusable_responses_argument_fallbacks(
    arguments: str, metadata_fields: dict, expected_part: dict
):
    message = {
        "role": "assistant",
        "content": [
            {"type": "function_call", "id": "fc_item_1", "call_id": "call_1", "name": "f", "arguments": arguments}
        ],
        "tool_calls": [{"id": "call_1", "name": "f", **metadata_fields}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [{"role": "assistant", "parts": [expected_part]}]


def test_gen_ai_input_messages_prefer_metadata_name_for_responses_calls():
    message = {
        "role": "assistant",
        "content": [{"type": "function_call", "call_id": "call_1", "name": "content_name", "arguments": '{"a":1}'}],
        "tool_calls": [{"id": "call_1", "name": "metadata_name", "args": {"a": 2}}],
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [{"type": "tool_call", "id": "call_1", "name": "metadata_name", "arguments": {"a": 2}}],
        }
    ]


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [("{}", {}), ('{"a":', '{"a":'), ("5", "5")],
    ids=["empty-object", "partial-json", "scalar"],
)
def test_gen_ai_input_messages_preserve_provider_argument_parsing(arguments: str, expected: object):
    message = {
        "role": "assistant",
        "additional_kwargs": {"tool_calls": [{"id": "call_1", "function": {"name": "f", "arguments": arguments}}]},
    }

    assert _get_gen_ai_input_messages({"messages": [message]}) == [
        {
            "role": "assistant",
            "parts": [{"type": "tool_call", "id": "call_1", "name": "f", "arguments": expected}],
        }
    ]


@pytest.mark.parametrize("direction", ["input", "output"])
@pytest.mark.parametrize("failure_stage", ["conversion", "serialization"])
def test_new_message_attribute_failure_preserves_legacy_io(direction: str, failure_stage: str):
    """Failures in new message attributes must not suppress legacy I/O."""
    exporter = _make_exporter()
    span = MagicMock()
    inputs = {"messages": [{"role": "user", "content": "hello"}]}
    outputs = {"generations": [{"text": "hi"}]}
    op = SimpleNamespace(
        id=uuid.uuid4(),
        inputs=_orjson.dumps(inputs) if direction == "input" else None,
        outputs=_orjson.dumps(outputs) if direction == "output" else None,
    )
    module = "langsmith._internal.otel._otel_exporter"
    target = (
        f"{module}._get_gen_ai_{direction}_messages" if failure_stage == "conversion" else f"{module}._orjson.dumps"
    )

    with patch(target, side_effect=ValueError("message conversion failed")) as fail:
        exporter._set_io_attributes(span, op)

    assert fail.called
    attrs = {call.args[0]: call.args[1] for call in span.set_attribute.call_args_list}
    legacy_name = "gen_ai.prompt" if direction == "input" else "gen_ai.completion"
    payload = op.inputs if direction == "input" else op.outputs
    assert attrs[legacy_name] == payload.decode("utf-8")
    assert f"gen_ai.{direction}.messages" not in attrs


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
