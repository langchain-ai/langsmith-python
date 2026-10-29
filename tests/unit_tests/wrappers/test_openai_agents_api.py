"""wrap_openai on the Agents API: each finished turn's OTLP trace is forwarded to LangSmith."""

from __future__ import annotations

import asyncio
import json
import threading
import time
import uuid
import warnings
from types import SimpleNamespace
from typing import Any, Optional
from unittest import mock

import pytest

import langsmith as ls
from langsmith import run_helpers
from langsmith.run_helpers import tracing_context
from langsmith.wrappers import _openai_agents_api as agents_api
from langsmith.wrappers._openai import wrap_openai


def _otlp(turn_id: str, n_children: int = 1, usage: bool = True) -> dict:
    root = {
        "traceId": "ab" * 16,
        "spanId": f"{abs(hash(turn_id)) % 16**16:016x}",
        "name": "invoke_agent",
        "startTimeUnixNano": "1792921647000000000",
        "endTimeUnixNano": "1792921650000000000",
        "attributes": [{"key": "openai.managed_agents.turn.id", "value": {"stringValue": turn_id}}]
        + ([{"key": "gen_ai.usage.input_tokens", "value": {"intValue": "100"}}] if usage else []),
    }
    children = [
        {
            "traceId": "ab" * 16,
            "spanId": f"{(abs(hash(turn_id)) + i + 1) % 16**16:016x}",
            "parentSpanId": root["spanId"],
            "name": "chat gpt-5.4-mini",
            "startTimeUnixNano": "1792921647500000000",
            "endTimeUnixNano": "1792921649000000000",
            "attributes": [],
        }
        for i in range(n_children)
    ]
    return {"resourceSpans": [{"scopeSpans": [{"spans": [root, *children]}]}]}


class FakeAgentsBackend:
    """In-memory stand-in for OpenAI's sessions / turns / traces endpoints."""

    def __init__(self) -> None:
        self.turns: dict[str, list[SimpleNamespace]] = {}
        self.traces: dict[str, list[SimpleNamespace]] = {}
        self.deleted: list[str] = []
        self.lock = threading.Lock()
        self._n = 0

    def new_session(self) -> str:
        self._n += 1
        session_id = f"sess_{uuid.uuid4().hex[:12]}"  # unique across tests: forwarders outlive a test
        self.turns[session_id], self.traces[session_id] = [], []
        return session_id

    def start_turn(self, session_id: str) -> str:
        with self.lock:
            turn_id = f"turn_{session_id}_{len(self.turns[session_id]) + 1}"
            self.turns[session_id].append(
                SimpleNamespace(id=turn_id, status="in_progress", subagent_id=None, created_at=int(time.time()))
            )
        return turn_id

    def finish_turn(self, session_id: str, turn_id: str, publish: bool = True) -> None:
        with self.lock:
            next(t for t in self.turns[session_id] if t.id == turn_id).status = "completed"
        if publish:
            self.publish(session_id, turn_id)

    def publish(self, session_id: str, turn_id: str, usage: bool = True) -> None:
        """Publish a turn's trace, or republish it (OpenAI can add token usage after publishing)."""
        with self.lock:
            self.traces[session_id] = [tr for tr in self.traces[session_id] if tr.id != turn_id]
            self.traces[session_id].append(SimpleNamespace(id=turn_id, otlp=_otlp(turn_id, usage=usage)))
            order = [t.id for t in self.turns[session_id]]
            self.traces[session_id].sort(key=lambda tr: order.index(tr.id))

    # --- the openai client surface used by the wrapper -------------------------------------------

    def list_turns(self, session_id: str, **_: Any) -> list:
        with self.lock:
            return list(self.turns[session_id])

    def list_traces(self, session_id: str, after: Optional[str] = None, **_: Any) -> list:
        with self.lock:
            traces = list(self.traces[session_id])
            order = [t.id for t in self.turns[session_id]]
        if after:
            traces = [tr for tr in traces if order.index(tr.id) > order.index(after)]
        return traces


class FakeStream:
    """Like openai's Stream: iteration reads `self._iterator`."""

    def __init__(self, events: list) -> None:
        self._iterator = iter(events)

    def __iter__(self):
        yield from self._iterator


MESSAGE = {"type": "agent.session.input.message", "input": [{"role": "user", "content": "go on"}]}


def make_client(backend: FakeAgentsBackend, *, create_delay: float = 0.0) -> Any:
    def create(**kwargs: Any) -> Any:
        session_id = backend.new_session()
        if kwargs.get("input"):
            backend.start_turn(session_id)
        time.sleep(create_delay)
        if kwargs.get("stream"):
            return FakeStream(
                [
                    SimpleNamespace(type="agent.session.created", session=SimpleNamespace(id=session_id)),
                    SimpleNamespace(type="agent.session.turn.created", session_id=session_id),
                ]
            )
        return SimpleNamespace(object="agent.session", id=session_id, status="idle")

    def events_create(session_id: str, events: list, **_: Any) -> None:
        # Like the API: only user messages start a turn; tool results, cancels and approvals don't.
        if any(e["type"] == "agent.session.input.message" for e in events):
            backend.start_turn(session_id)

    def stream(session_id: str, input: str, **_: Any) -> Any:
        # Like openai's sessions.stream helper: submits the input through (the patched) events.create.
        sessions.events.create(session_id, events=[{**MESSAGE, "input": [{"role": "user", "content": input}]}])
        return FakeStream([])

    def delete(session_id: str, **_: Any) -> Any:
        backend.deleted.append(session_id)
        return SimpleNamespace(deleted=True)

    sessions = SimpleNamespace(
        create=create,
        delete=delete,
        stream=stream,
        events=SimpleNamespace(create=events_create),
        turns=SimpleNamespace(list=backend.list_turns),
        traces=SimpleNamespace(list=backend.list_traces),
        subagents=SimpleNamespace(list=lambda session_id, **_: [], turns=SimpleNamespace(list=lambda *a, **k: [])),
    )
    noop = mock.MagicMock()
    return SimpleNamespace(
        beta=SimpleNamespace(agents=SimpleNamespace(sessions=sessions), chat=noop),
        chat=noop,
        completions=noop,
        responses=noop,
    )


@pytest.fixture
def backend(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(agents_api, "_POLL_INTERVAL", (0.01, 0.05))
    monkeypatch.setattr(agents_api, "_sync_twin", lambda client: client)
    # Pin tracing on for this test: other tests in the same worker change the global setting.
    with tracing_context(enabled=True):
        yield FakeAgentsBackend()


@pytest.fixture
def ls_client() -> mock.MagicMock:
    return mock.MagicMock()


def posted(ls_client: mock.MagicMock) -> list[tuple[dict, dict]]:
    """(OTLP body, headers) for every POST the wrapper sent to LangSmith."""
    out = []
    for call in ls_client.request_with_retries.call_args_list:
        assert call.args[:2] == ("POST", "/otel/v1/traces")
        kwargs = call.kwargs["request_kwargs"]
        out.append((json.loads(kwargs["data"]), kwargs["headers"]))
    return out


def turn_ids(bodies: list[tuple[dict, dict]]) -> list[str]:
    return [
        next(
            a["value"]["stringValue"]
            for a in agents_api._spans(body)[0]["attributes"]
            if a["key"] == "openai.managed_agents.turn.id"
        )
        for body, _ in bodies
    ]


def attrs(span: dict) -> dict[str, str]:
    return {a["key"]: next(iter(a["value"].values())) for a in span["attributes"]}


def wait_for(condition, timeout: float = 5.0) -> None:
    deadline = time.monotonic() + timeout
    while not condition():
        assert time.monotonic() < deadline, "timed out"
        time.sleep(0.01)


def test_non_streamed_create_forwards_the_turn_trace(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client, "metadata": {"team": "a"}})

    session = client.beta.agents.sessions.create(input="hi", environment={"type": "openai_hosted"})
    turn_id = backend.turns[session.id][0].id
    time.sleep(0.05)
    assert posted(ls_client) == []  # nothing until the turn ends and OpenAI publishes

    backend.finish_turn(session.id, turn_id)
    wait_for(lambda: posted(ls_client))
    [(body, headers)] = posted(ls_client)
    assert turn_ids([(body, headers)]) == [turn_id]
    assert headers["Content-Type"] == "application/json"
    root = agents_api._spans(body)[0]
    assert attrs(root)["langsmith.metadata.team"] == "a"
    assert len(agents_api._spans(body)) == 2


def test_streamed_create_passes_events_through_and_forwards(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})

    stream = client.beta.agents.sessions.create(input="hi", environment={}, stream=True)
    events = [event.type for event in stream]
    assert events == ["agent.session.created", "agent.session.turn.created"]

    session_id = next(iter(backend.turns))
    backend.finish_turn(session_id, backend.turns[session_id][0].id)
    wait_for(lambda: posted(ls_client))
    assert turn_ids(posted(ls_client)) == [backend.turns[session_id][0].id]


def test_each_turn_is_forwarded_once(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="turn 1", environment={})
    turn1 = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn1)
    wait_for(lambda: len(posted(ls_client)) == 1)

    client.beta.agents.sessions.events.create(session.id, events=[MESSAGE])
    turn2 = backend.turns[session.id][1].id
    backend.finish_turn(session.id, turn2)
    wait_for(lambda: len(posted(ls_client)) == 2)
    time.sleep(0.1)
    assert turn_ids(posted(ls_client)) == [turn1, turn2]


def test_turn_held_by_a_background_subagent_is_not_skipped(backend, ls_client):
    # Turn 1's trace is published after turn 2's, as when a background subagent holds it.
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="turn 1", environment={})
    turn1 = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn1, publish=False)
    client.beta.agents.sessions.events.create(session.id, events=[MESSAGE])
    turn2 = backend.turns[session.id][1].id
    backend.finish_turn(session.id, turn2)
    wait_for(lambda: len(posted(ls_client)) == 1)

    backend.publish(session.id, turn1)
    wait_for(lambda: len(posted(ls_client)) == 2)
    assert sorted(turn_ids(posted(ls_client))) == sorted([turn1, turn2])


def test_turn_started_inside_traceable_nests_under_it(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})

    @run_helpers.traceable(client=ls_client)
    def my_app() -> tuple[str, Any]:
        session = client.beta.agents.sessions.create(input="hi", environment={})
        return session.id, run_helpers.get_current_run_tree()

    session_id, parent = my_app()
    backend.finish_turn(session_id, backend.turns[session_id][0].id)
    wait_for(lambda: posted(ls_client))
    [(body, _)] = posted(ls_client)
    root, child = agents_api._spans(body)
    root_attrs, child_attrs = attrs(root), attrs(child)
    assert root_attrs["langsmith.trace.id"] == child_attrs["langsmith.trace.id"] == str(parent.trace_id)
    assert root_attrs["langsmith.span.parent_id"] == str(parent.id)
    assert child_attrs["langsmith.span.parent_id"] == root_attrs["langsmith.span.id"]
    assert root_attrs["langsmith.span.dotted_order"].startswith(parent.dotted_order + ".")
    assert child_attrs["langsmith.span.dotted_order"].startswith(root_attrs["langsmith.span.dotted_order"] + ".")
    assert child_attrs["langsmith.span.dotted_order"].endswith(child_attrs["langsmith.span.id"])


def test_delete_waits_for_the_pending_trace(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id, publish=False)
    threading.Timer(0.2, backend.publish, args=(session.id, turn_id)).start()

    client.beta.agents.sessions.delete(session.id)
    assert backend.deleted == [session.id]
    assert turn_ids(posted(ls_client)) == [turn_id]  # forwarded before the delete went through


def test_delete_waits_past_the_exit_timeout_for_a_held_trace(backend, ls_client, monkeypatch):
    # A background subagent keeps OpenAI from publishing the turn for a while; delete must not give up early.
    monkeypatch.setattr(agents_api, "_DRAIN_TIMEOUT", 0.05)
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id, publish=False)
    threading.Timer(0.3, backend.publish, args=(session.id, turn_id)).start()

    client.beta.agents.sessions.delete(session.id)
    assert turn_ids(posted(ls_client)) == [turn_id]


def test_session_deleted_elsewhere_stops_being_watched(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    forwarder = next(f for f in agents_api._FORWARDERS if session.id in f._active)

    def gone(session_id: str, **_: Any) -> list:
        raise type("NotFoundError", (Exception,), {"status_code": 404})()

    backend.list_turns = gone  # type: ignore[method-assign]
    client.beta.agents.sessions.turns.list = gone
    assert forwarder.drain(session.id, timeout=2)
    assert posted(ls_client) == []


def test_nothing_is_forwarded_when_tracing_is_off(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    with tracing_context(enabled=False):
        session = client.beta.agents.sessions.create(input="hi", environment={})
    backend.finish_turn(session.id, backend.turns[session.id][0].id)
    time.sleep(0.2)
    assert posted(ls_client) == []


def test_client_without_agents_api_is_still_wrapped(backend, ls_client):
    client = make_client(backend)
    del client.beta.agents
    assert wrap_openai(client, tracing_extra={"client": ls_client}) is client


def _like_openai_async(fn):
    """openai decorates its async methods, so they don't look like coroutine functions."""

    def method(*args: Any, **kwargs: Any) -> Any:
        return fn(*args, **kwargs)

    return method


def test_async_create_forwards_the_turn_trace(backend, ls_client):
    openai = pytest.importorskip("openai")
    sync_sessions = make_client(backend).beta.agents.sessions

    async def acreate(**kwargs: Any) -> Any:
        return sync_sessions.create(**kwargs)

    async def adelete(session_id: str, **kwargs: Any) -> Any:
        return sync_sessions.delete(session_id, **kwargs)

    async_client = openai.AsyncOpenAI(api_key="test")
    async_client.beta = SimpleNamespace(  # type: ignore[misc]
        agents=SimpleNamespace(
            sessions=SimpleNamespace(
                create=_like_openai_async(acreate),
                delete=_like_openai_async(adelete),
                events=SimpleNamespace(create=_like_openai_async(acreate)),
                turns=sync_sessions.turns,
                traces=sync_sessions.traces,
                subagents=sync_sessions.subagents,
            )
        ),
        chat=mock.MagicMock(),
    )
    client = wrap_openai(async_client, tracing_extra={"client": ls_client})

    async def run() -> str:
        session = await client.beta.agents.sessions.create(input="hi", environment={})
        turn_id = backend.turns[session.id][0].id
        backend.finish_turn(session.id, turn_id, publish=False)
        threading.Timer(0.1, backend.publish, args=(session.id, turn_id)).start()
        await client.beta.agents.sessions.delete(session.id)
        return session.id

    session_id = asyncio.run(run())
    assert backend.deleted == [session_id]
    assert turn_ids(posted(ls_client)) == [backend.turns[session_id][0].id]


def test_calls_that_start_no_turn_do_not_hold_delete(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(environment={})  # no input: no turn
    client.beta.agents.sessions.events.create(
        session.id, events=[{"type": "agent.session.input.tool_result", "call_id": "c", "success": True}]
    )

    start = time.monotonic()
    client.beta.agents.sessions.delete(session.id)
    assert time.monotonic() - start < 1
    assert backend.deleted == [session.id]


def test_each_streamed_turn_nests_under_its_own_parent(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(environment={})

    @run_helpers.traceable(client=ls_client)
    def ask(question: str) -> Any:
        client.beta.agents.sessions.stream(session.id, input=question)
        turn = backend.turns[session.id][-1].id
        backend.finish_turn(session.id, turn)
        wait_for(lambda: turn in turn_ids(posted(ls_client)))
        return run_helpers.get_current_run_tree()

    first, second = ask("a"), ask("b")
    parent_of = {
        turn: attrs(agents_api._spans(body)[0])["langsmith.span.parent_id"]
        for turn, (body, _) in zip(turn_ids(posted(ls_client)), posted(ls_client))
    }
    turn1, turn2 = (t.id for t in backend.turns[session.id])
    assert parent_of == {turn1: str(first.id), turn2: str(second.id)}


def test_slow_non_streamed_create_is_still_traced(backend, ls_client, monkeypatch):
    # The turn starts before create returns, longer ago than the clock slack. The slack still has to
    # cover created_at being whole seconds, as in the API.
    monkeypatch.setattr(agents_api, "_CLOCK_SLACK", 1.0)
    client = wrap_openai(make_client(backend, create_delay=1.2), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={"type": "openai_hosted"})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id)
    wait_for(lambda: posted(ls_client))
    assert turn_ids(posted(ls_client)) == [turn_id]


def test_turns_follow_the_agent_address(backend, ls_client):
    address = ls.agent_address("support", "production")
    expected = {"Langsmith-Agent-Id": "support", "Langsmith-Agent-Environment": "production"}
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client, "address": address})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    backend.finish_turn(session.id, backend.turns[session.id][0].id)

    # Like @traceable, the parent run's destination outranks tracing_extra.
    other = wrap_openai(make_client(backend), tracing_extra={"client": ls_client, "project_name": "other"})

    @run_helpers.traceable(client=ls_client, address=address)
    def my_app() -> str:
        with tracing_context(project_name="other"):  # a child keeps its parent's destination
            return other.beta.agents.sessions.create(input="hi", environment={}).id

    nested = my_app()
    backend.finish_turn(nested, backend.turns[nested][0].id)

    with tracing_context(address=address):
        in_context = other.beta.agents.sessions.create(input="hi", environment={}).id
    backend.finish_turn(in_context, backend.turns[in_context][0].id)
    wait_for(lambda: len(posted(ls_client)) == 3)
    for _, headers in posted(ls_client):
        assert {k: v for k, v in headers.items() if k.startswith("Langsmith-")} == expected


def test_missing_trace_permission_stops_tracing_the_client(backend, ls_client, caplog):
    def forbidden(session_id: str, **_: Any) -> list:
        raise type("PermissionDeniedError", (Exception,), {"status_code": 403})()

    raw = make_client(backend)
    raw.beta.agents.sessions.traces.list = forbidden
    client = wrap_openai(raw, tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    backend.finish_turn(session.id, backend.turns[session.id][0].id)

    start = time.monotonic()
    client.beta.agents.sessions.delete(session.id)
    assert time.monotonic() - start < 2
    assert "won't be traced" in caplog.text
    assert posted(ls_client) == []


def test_worker_thread_exits_when_idle_and_restarts(backend, ls_client, monkeypatch):
    monkeypatch.setattr(agents_api, "_IDLE_EXIT", 0.1)
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="turn 1", environment={})
    forwarder = next(f for f in agents_api._FORWARDERS if session.id in f._sessions)
    backend.finish_turn(session.id, backend.turns[session.id][0].id)
    wait_for(lambda: len(posted(ls_client)) == 1)
    wait_for(lambda: forwarder._thread is None)

    client.beta.agents.sessions.events.create(session.id, events=[MESSAGE])
    backend.finish_turn(session.id, backend.turns[session.id][1].id)
    wait_for(lambda: len(posted(ls_client)) == 2)


class AsyncKey:
    """A key provider that is an object with `async def __call__`, not a coroutine function."""

    async def __call__(self) -> str:
        return "sk-from-callable"


async def key_function() -> str:
    return "sk-from-function"


@pytest.mark.parametrize("provider", [key_function, AsyncKey()], ids=["async function", "async callable object"])
def test_async_client_with_a_key_provider_gets_a_working_sync_twin(ls_client, provider):
    openai = pytest.importorskip("openai")
    try:
        async_client = openai.AsyncOpenAI(api_key=provider)
    except Exception:
        pytest.skip("this openai version has no api_key provider")
    wrap_openai(async_client, tracing_extra={"client": ls_client})  # used to raise "Missing credentials"
    twin = agents_api._sync_twin(async_client)
    assert isinstance(twin, openai.OpenAI)
    if getattr(twin, "_api_key_provider", None) is not None:
        assert twin._api_key_provider() in ("sk-from-function", "sk-from-callable")


def test_beta_warning_only_for_agents_api_users(backend, ls_client):
    from langsmith._internal._beta_decorator import LangSmithBetaWarning, _warn_once

    _warn_once.cache_clear()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
        assert not [w for w in caught if issubclass(w.category, LangSmithBetaWarning)]  # chat-only users: none

        client.beta.agents.sessions.create(input="hi", environment={})
    assert [str(w.message) for w in caught if issubclass(w.category, LangSmithBetaWarning)] == [
        "Tracing OpenAI Agents API sessions with wrap_openai is in beta."
    ]


def test_strict_warnings_fail_before_any_session_is_created(backend, ls_client):
    from langsmith._internal._beta_decorator import LangSmithBetaWarning, _warn_once

    _warn_once.cache_clear()
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    with warnings.catch_warnings():
        warnings.simplefilter("error", LangSmithBetaWarning)
        with pytest.raises(LangSmithBetaWarning):
            client.beta.agents.sessions.create(input="hi", environment={})
    assert backend.turns == {}  # nothing created at OpenAI, so nothing is lost


def _span(span_id: str, name: str, start_s: float, end_s: float, parent: str = "", **attrs: Any) -> dict:
    span = {
        "traceId": "ab" * 16,
        "spanId": span_id,
        "name": name,
        "startTimeUnixNano": str(int(start_s * 1e9)),
        "endTimeUnixNano": str(int(end_s * 1e9)),
        "attributes": [{"key": k.replace("__", "."), "value": {"stringValue": str(v)}} for k, v in attrs.items()],
    }
    if parent:
        span["parentSpanId"] = parent
    return span


def _turn_with_subagent() -> dict:
    t = 1792921647.0
    usage = {"gen_ai__usage__input_tokens": 100, "gen_ai__usage__output_tokens": 10}
    spans = [
        _span("a" * 16, "invoke_agent", t, t + 9, **usage),
        _span("b" * 16, "chat gpt-5.4-mini", t, t + 2, parent="a" * 16),
        _span("c" * 16, "invoke_agent Kepler", t + 2, t + 6, parent="a" * 16, gen_ai__usage__input_tokens=40),
        _span("d" * 16, "chat gpt-5.4-mini", t + 2, t + 5, parent="c" * 16),
        _span("e" * 16, "chat gpt-5.4-mini", t + 6, t + 9, parent="a" * 16),
    ]
    return {"resourceSpans": [{"scopeSpans": [{"spans": spans}]}]}


def test_agent_runs_are_chains_and_usage_moves_to_the_last_model_call():
    spans = {
        s["spanId"][0]: attrs(s)
        for s in agents_api._spans(agents_api._prepare_otlp(_turn_with_subagent(), None, {}, []))
    }

    for agent in ("a", "c"):  # root and subagent
        assert spans[agent]["langsmith.span.kind"] == "chain"
        assert not [k for k in spans[agent] if k.startswith("gen_ai.usage.")]
    # the root's own tokens on its last call, the subagent's on its own last call; earlier calls untouched
    assert (
        spans["e"]["gen_ai.usage.input_tokens"] == "100"
        and spans["e"]["langsmith.metadata.usage_scope"] == "agent_total"
    )
    assert spans["d"]["gen_ai.usage.input_tokens"] == "40"
    assert "gen_ai.usage.input_tokens" not in spans["b"]


def test_run_ids_are_deterministic_uuid7_with_the_root_as_trace():
    first = agents_api._spans(agents_api._prepare_otlp(_turn_with_subagent(), None, {}, []))
    again = agents_api._spans(agents_api._prepare_otlp(_turn_with_subagent(), None, {}, []))
    ids = [attrs(s)["langsmith.span.id"] for s in first]

    assert ids == [attrs(s)["langsmith.span.id"] for s in again]  # a re-post maps to the same runs
    assert all(uuid.UUID(i).version == 7 for i in ids) and len(set(ids)) == len(ids)
    root, child = attrs(first[0]), attrs(first[1])
    assert root["langsmith.trace.id"] == root["langsmith.span.id"] == child["langsmith.trace.id"]
    assert "langsmith.span.parent_id" not in root and child["langsmith.span.parent_id"] == root["langsmith.span.id"]
    assert "." not in root["langsmith.span.dotted_order"]
    assert child["langsmith.span.dotted_order"].startswith(root["langsmith.span.dotted_order"] + ".")


def test_agents_setup_failure_never_breaks_wrap_openai(backend, ls_client, monkeypatch):
    def boom(*_: Any, **__: Any) -> None:
        raise RuntimeError("unexpected client shape")

    monkeypatch.setattr(agents_api, "wrap_agents_sessions", boom)
    client = make_client(backend)
    assert wrap_openai(client, tracing_extra={"client": ls_client}) is client


def test_trace_published_before_its_usage_is_forwarded_with_usage(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id, publish=False)
    backend.publish(session.id, turn_id, usage=False)  # first copy, without token usage
    time.sleep(0.3)
    assert posted(ls_client) == []  # held: LangSmith keeps the first copy of a run

    backend.publish(session.id, turn_id)  # OpenAI adds the usage
    wait_for(lambda: posted(ls_client))
    [(body, _)] = posted(ls_client)
    model_call = agents_api._spans(body)[1]
    assert attrs(model_call)["langsmith.metadata.usage_scope"] == "agent_total"


def test_trace_without_usage_is_still_sent_after_the_grace_period(backend, ls_client, monkeypatch):
    monkeypatch.setattr(agents_api, "_USAGE_GRACE", 0.2)
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id, publish=False)
    backend.publish(session.id, turn_id, usage=False)
    wait_for(lambda: posted(ls_client))
    assert turn_ids(posted(ls_client)) == [turn_id]


def test_failed_spans_get_an_exception_event():
    otlp = _turn_with_subagent()
    root = agents_api._spans(otlp)[0]
    root["status"] = {"code": 2, "message": "Artifact publication failed"}
    spans = agents_api._spans(agents_api._prepare_otlp(otlp, None, {}, []))

    [event] = spans[0]["events"]
    assert event["name"] == "exception"
    assert attrs(event)["exception.message"] == "Artifact publication failed"
    assert not any(s.get("events") for s in spans[1:])  # spans without an error status are untouched


def test_rate_limit_pauses_polling_for_retry_after(backend, ls_client):
    calls: list[float] = []
    list_turns = backend.list_turns

    def rate_limited_once(session_id: str, **kwargs: Any) -> list:
        calls.append(time.monotonic())
        if len(calls) == 1:
            error = type("RateLimitError", (Exception,), {"status_code": 429})()
            error.response = SimpleNamespace(headers={"retry-after": "0.5"})
            raise error
        return list_turns(session_id, **kwargs)

    raw = make_client(backend)
    raw.beta.agents.sessions.turns.list = rate_limited_once
    client = wrap_openai(raw, tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    backend.finish_turn(session.id, backend.turns[session.id][0].id)

    wait_for(lambda: posted(ls_client))
    assert calls[1] - calls[0] >= 0.5  # nothing polled during the Retry-After window


def test_every_run_follows_coding_agent_v1():
    otlp = _turn_with_subagent()
    for span in agents_api._spans(otlp):
        span["attributes"].append({"key": "openai.managed_agents.turn.id", "value": {"stringValue": "turn_1"}})
    kepler = agents_api._spans(otlp)[2]
    kepler["attributes"].append({"key": "openai.managed_agents.subagent.id", "value": {"stringValue": "subagent_k"}})

    spans = agents_api._spans(
        agents_api._prepare_otlp(otlp, None, {"ls_integration": "mine", "team": "a"}, [], 3, "openai_hosted")
    )
    md = [
        {k.removeprefix("langsmith.metadata."): v for k, v in attrs(s).items() if k.startswith("langsmith.metadata.")}
        for s in spans
    ]
    for run in md:  # identity, versions and turn on every run
        assert run["ls_agent_purpose"] == "coding" and "ls_agent_kind" not in run
        assert run["ls_integration"] == "openai-agents-api"
        assert run["ls_agent_runtime"] == "OpenAI Agents API" and run["ls_trace_schema_version"] == "coding-agent-v1"
        assert run["turn_id"] == "turn_1" and run["turn_number"] == "3" and run["sandbox_type"] == "openai_hosted"
        assert "ls_integration_version" in run and "ls_agent_runtime_version" in run
    assert md[0]["team"] == "a" and "team" not in md[1]  # user metadata on the root only, can't shadow the contract
    # root agent subtree vs subagent subtree: a, b, e belong to the root agent; c (Kepler) and d to the subagent
    assert [m["ls_agent_type"] for m in md] == ["root", "root", "subagent", "subagent", "root"]
    assert [m.get("ls_subagent_id") for m in md] == [None, None, "subagent_k", "subagent_k", None]


def test_exit_sends_a_trace_still_waiting_for_usage(backend, ls_client, monkeypatch):
    monkeypatch.setattr(agents_api, "_DRAIN_TIMEOUT", 3)  # shorter than the usage wait
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="hi", environment={})
    turn_id = backend.turns[session.id][0].id
    backend.finish_turn(session.id, turn_id, publish=False)
    backend.publish(session.id, turn_id, usage=False)

    agents_api._drain_at_exit()
    assert turn_ids(posted(ls_client)) == [turn_id]


def test_retry_after_as_http_date():
    from datetime import datetime, timedelta, timezone
    from email.utils import format_datetime

    when = format_datetime(datetime.now(timezone.utc) + timedelta(seconds=90), usegmt=True)
    error = SimpleNamespace(response=SimpleNamespace(headers={"retry-after": when}))
    assert 85 <= agents_api._retry_after(error) <= 90


def test_every_run_gets_the_session_as_thread_id():
    otlp = _turn_with_subagent()
    for span in agents_api._spans(otlp):
        span["attributes"].append({"key": "openai.managed_agents.session.id", "value": {"stringValue": "sess_1"}})

    spans = agents_api._spans(agents_api._prepare_otlp(otlp, None, {}, []))
    assert {attrs(s)["langsmith.metadata.thread_id"] for s in spans} == {"sess_1"}

    # a thread_id the user set wins on the root
    spans = agents_api._spans(agents_api._prepare_otlp(otlp, None, {"thread_id": "mine"}, []))
    assert [
        a["value"]["stringValue"] for a in spans[0]["attributes"] if a["key"] == "langsmith.metadata.thread_id"
    ] == ["mine"]


def test_turn_number_and_sandbox_type_come_from_the_session(backend, ls_client):
    client = wrap_openai(make_client(backend), tracing_extra={"client": ls_client})
    session = client.beta.agents.sessions.create(input="turn 1", environment={"type": "openai_hosted"})
    backend.finish_turn(session.id, backend.turns[session.id][0].id)
    client.beta.agents.sessions.events.create(session.id, events=[MESSAGE])
    backend.finish_turn(session.id, backend.turns[session.id][1].id)
    wait_for(lambda: len(posted(ls_client)) == 2)

    roots = [attrs(agents_api._spans(body)[0]) for body, _ in posted(ls_client)]
    assert [r["langsmith.metadata.turn_number"] for r in roots] == ["1", "2"]
    assert {r["langsmith.metadata.sandbox_type"] for r in roots} == {"openai_hosted"}
