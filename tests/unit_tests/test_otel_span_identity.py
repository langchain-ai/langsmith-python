import asyncio
import datetime
import os
import uuid
from concurrent.futures import ThreadPoolExecutor

import pytest
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import SpanProcessor, TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.sdk.trace.sampling import ALWAYS_OFF, ParentBased

from langsmith import Client, traceable, tracing_context
from langsmith._internal._operations import serialize_run_dict
from langsmith._internal._otel_utils import get_otel_span_id_from_uuid
from langsmith._internal.otel._otel_exporter import OTELExporter


@pytest.fixture
def otel_environment(monkeypatch, request):
    for name in os.environ:
        if name.startswith(("LANGSMITH_", "LANGCHAIN_", "OTEL_")):
            monkeypatch.delenv(name)
    provider = TracerProvider(
        resource=Resource.create({"service.name": "identity-test"}),
        sampler=getattr(request, "param", None),
    )
    sink = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(sink))
    try:
        yield provider, sink
    finally:
        provider.shutdown()


def _operation(run_id, trace_id, *, parent_id=None, ended=True, operation="post"):
    now = datetime.datetime.now(datetime.timezone.utc)
    return serialize_run_dict(
        operation,
        {
            "id": run_id,
            "trace_id": trace_id,
            "name": str(run_id),
            "run_type": "chain",
            "parent_run_id": str(parent_id) if parent_id else None,
            "start_time": now,
            "end_time": now if ended else None,
        },
    )


def _assert_native_parent(sink):
    spans = {span.name: span for span in sink.get_finished_spans()}
    assert set(spans) == {"langsmith-parent", "native-child"}
    parent, child = spans["langsmith-parent"], spans["native-child"]
    assert child.parent.span_id == parent.context.span_id
    assert child.context.trace_id == parent.context.trace_id
    assert parent.parent is None


@pytest.mark.parametrize("external_parent", [False, True])
def test_native_child_points_to_exported_run(otel_environment, external_parent):
    provider, sink = otel_environment
    client = Client(api_key="test", tracing_mode="otel", otel_tracer_provider=provider)
    native_tracer = provider.get_tracer("native")

    @traceable(name="langsmith-parent", client=client)
    def parent():
        with native_tracer.start_as_current_span("native-child"):
            pass

    try:
        with tracing_context(enabled=True):
            if external_parent:
                with native_tracer.start_as_current_span("external"):
                    parent()
            else:
                parent()
        client.flush()
        if external_parent:
            spans = {span.name: span for span in sink.get_finished_spans()}
            run_span, child, external = (spans[name] for name in ("langsmith-parent", "native-child", "external"))
            assert child.parent.span_id == run_span.context.span_id
            assert child.context.trace_id == run_span.context.trace_id == external.context.trace_id
            assert run_span.parent.span_id == external.context.span_id
            return
        _assert_native_parent(sink)
    finally:
        client.close()


@pytest.mark.parametrize("external_parent", [False, True])
async def test_async_native_child_points_to_exported_run(otel_environment, external_parent):
    provider, sink = otel_environment
    client = Client(api_key="test", tracing_mode="otel", otel_tracer_provider=provider)
    native_tracer = provider.get_tracer("native")

    @traceable(name="langsmith-parent", client=client)
    async def parent():
        await asyncio.sleep(0)
        with native_tracer.start_as_current_span("native-child"):
            pass

    try:
        with tracing_context(enabled=True):
            if external_parent:
                with native_tracer.start_as_current_span("external"):
                    await parent()
            else:
                await parent()
        await asyncio.to_thread(client.flush)
        if external_parent:
            spans = {span.name: span for span in sink.get_finished_spans()}
            run_span, child, external = (spans[name] for name in ("langsmith-parent", "native-child", "external"))
            assert child.parent.span_id == run_span.context.span_id
            assert child.context.trace_id == run_span.context.trace_id == external.context.trace_id
            assert run_span.parent.span_id == external.context.span_id
            return
        _assert_native_parent(sink)
    finally:
        client.close()


@pytest.mark.parametrize("child_first", [False, True])
def test_nested_runs_keep_parent_identity_across_batches(otel_environment, child_first):
    provider, sink = otel_environment
    exporter = OTELExporter(tracer_provider=provider)
    root_id, child_id = uuid.uuid4(), uuid.uuid4()
    root = _operation(root_id, root_id)
    child = _operation(child_id, root_id, parent_id=root_id)
    for operation in [child, root] if child_first else [root, child]:
        exporter.export_batch([operation], {})
    spans = {span.name: span for span in sink.get_finished_spans()}
    root_span, child_span = spans[str(root_id)], spans[str(child_id)]
    assert root_span.parent is None
    assert root_span.context.span_id == get_otel_span_id_from_uuid(root_id)
    assert child_span.context.span_id == get_otel_span_id_from_uuid(child_id)
    assert child_span.parent.span_id == root_span.context.span_id
    assert child_span.context.trace_id == root_span.context.trace_id == root_id.int


def test_existing_parent_and_provider_are_preserved(otel_environment):
    provider, sink = otel_environment
    exporter = OTELExporter(tracer_provider=provider)
    native_tracer = provider.get_tracer("native")
    original_generator = provider.id_generator
    langsmith_tracer = provider.get_tracer("langsmith")
    global_provider = trace.get_tracer_provider()
    run_id = uuid.uuid4()
    with native_tracer.start_as_current_span("external") as parent:
        exporter.export_batch([_operation(run_id, uuid.uuid4())], {run_id: trace.set_span_in_context(parent)})
    spans = {span.name: span for span in sink.get_finished_spans()}
    run_span = spans[str(run_id)]
    external = spans["external"]
    assert run_span.context.span_id == get_otel_span_id_from_uuid(run_id)
    assert run_span.parent.span_id == external.context.span_id
    assert run_span.context.trace_id == external.context.trace_id
    assert run_span.resource.attributes["service.name"] == "identity-test"
    assert run_span.instrumentation_scope.name == "langsmith"
    assert provider.id_generator is langsmith_tracer.id_generator is original_generator
    assert trace.get_tracer_provider() is global_provider


def test_updates_end_the_same_span(otel_environment):
    provider, sink = otel_environment
    exporter = OTELExporter(tracer_provider=provider)
    run_id = uuid.uuid4()
    exporter.export_batch([_operation(run_id, run_id, ended=False)], {})
    assert not sink.get_finished_spans()
    exporter.export_batch([_operation(run_id, run_id, operation="patch")], {})
    spans = sink.get_finished_spans()
    assert len(spans) == 1
    assert spans[0].context.span_id == get_otel_span_id_from_uuid(run_id)
    assert not exporter._span_info


def test_concurrent_exports_do_not_share_ids(otel_environment):
    provider, sink = otel_environment
    exporter = OTELExporter(tracer_provider=provider)
    started_ids = []

    class RecordingProcessor(SpanProcessor):
        def on_start(self, span, parent_context=None):
            started_ids.append(span.get_span_context().span_id)

    provider.add_span_processor(RecordingProcessor())
    run_ids = [uuid.uuid4() for _ in range(40)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda run_id: exporter.export_batch([_operation(run_id, run_id)], {}), run_ids))
    spans = sink.get_finished_spans()
    assert len(spans) == len(run_ids)
    assert sorted(started_ids) == sorted(span.context.span_id for span in spans)
    for span in spans:
        run_id = uuid.UUID(span.name)
        assert span.context.trace_id == run_id.int
        assert span.context.span_id == get_otel_span_id_from_uuid(run_id)
        assert span.parent is None


def test_provider_registered_after_exporter_creation(otel_environment, monkeypatch):
    provider, sink = otel_environment
    monkeypatch.setattr(trace, "_TRACER_PROVIDER", None)
    exporter = OTELExporter()
    assert isinstance(exporter._tracer, trace.ProxyTracer)
    monkeypatch.setattr(trace, "_TRACER_PROVIDER", provider)
    run_id = uuid.uuid4()
    exporter.export_batch([_operation(run_id, run_id)], {})
    (span,) = sink.get_finished_spans()
    assert span.context.span_id == get_otel_span_id_from_uuid(run_id)
    assert span.context.trace_id == run_id.int
    assert span.parent is None


def test_root_does_not_inherit_export_worker_context(otel_environment):
    provider, sink = otel_environment
    exporter = OTELExporter(tracer_provider=provider)
    run_id = uuid.uuid4()
    with provider.get_tracer("worker").start_as_current_span("worker"):
        exporter.export_batch([_operation(run_id, run_id)], {})
    spans = {span.name: span for span in sink.get_finished_spans()}
    run_span = spans[str(run_id)]
    assert run_span.parent is None
    assert run_span.context.trace_id == run_id.int


def test_provider_sampler_is_respected():
    provider = TracerProvider(sampler=ALWAYS_OFF)
    sink = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(sink))
    try:
        run_id = uuid.uuid4()
        OTELExporter(tracer_provider=provider).export_batch([_operation(run_id, run_id)], {})
        assert not sink.get_finished_spans()
    finally:
        provider.shutdown()


@pytest.mark.parametrize("otel_environment", [ParentBased(ALWAYS_OFF)], indirect=True)
@pytest.mark.parametrize("sampled", [False, True])
def test_native_children_inherit_external_sampling(otel_environment, sampled):
    provider, sink = otel_environment
    client = Client(api_key="test", tracing_mode="otel", otel_tracer_provider=provider)
    native_tracer = provider.get_tracer("native")
    external = trace.SpanContext(
        trace_id=1234,
        span_id=5678,
        is_remote=True,
        trace_flags=trace.TraceFlags(trace.TraceFlags.SAMPLED if sampled else trace.TraceFlags.DEFAULT),
        trace_state=trace.TraceState([("origin", "test")]),
    )

    @traceable(name="langsmith-parent", client=client)
    def parent():
        with native_tracer.start_as_current_span("native-child"):
            pass

    try:
        with trace.use_span(trace.NonRecordingSpan(external)), tracing_context(enabled=True):
            parent()
        client.flush()
        spans = {span.name: span for span in sink.get_finished_spans()}
        if not sampled:
            assert not spans
            return
        assert set(spans) == {"langsmith-parent", "native-child"}
        run_span, child = spans["langsmith-parent"], spans["native-child"]
        assert child.parent.span_id == run_span.context.span_id
        assert run_span.parent.span_id == external.span_id
        for span in spans.values():
            assert span.context.trace_id == external.trace_id
            assert span.context.trace_state == external.trace_state
    finally:
        client.close()
