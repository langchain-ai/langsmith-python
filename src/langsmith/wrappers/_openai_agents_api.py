"""Trace OpenAI's hosted Agents API (``client.beta.agents.sessions``) to LangSmith.

The agent loop runs on OpenAI's side. OpenAI publishes one OTLP trace per root turn
after it ends; a background thread fetches it and posts it to ``/otel/v1/traces``.
"""

from __future__ import annotations

import asyncio
import atexit
import copy
import email.utils
import functools
import inspect
import json
import logging
import threading
import time
import uuid
import weakref
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional

import langsmith._internal._context as _context
from langsmith import run_helpers
from langsmith import run_trees as ls_run_trees
from langsmith import utils as ls_utils
from langsmith._internal import _addressing
from langsmith._internal._beta_decorator import _warn_once
from langsmith._internal._package_version import get_package_version

logger = logging.getLogger(__name__)

_TERMINAL = frozenset({"completed", "failed", "cancelled"})
# Poll interval, backing off from the first to the second value while nothing changes.
_POLL_INTERVAL = (2.0, 30.0)
# Give up on an unpublished trace after this. OpenAI holds it while subagent work runs.
_PUBLISH_TIMEOUT = 3600.0
# OpenAI can add token usage after publishing a trace: wait this long for it, then send as is.
_USAGE_GRACE = 120.0
# Pause on 429: Retry-After, or the first value without one, capped at the second.
_RATE_LIMIT_BACKOFF = (30.0, 300.0)
# Drop a registration that started no turn after this long.
_REGISTRATION_GRACE = 60.0
# Max wait for pending traces at interpreter exit.
_DRAIN_TIMEOUT = 60.0
# Max wait for pending traces in sessions.delete.
_DELETE_DRAIN_TIMEOUT = 600.0
# Clock slack between us and OpenAI when matching turns to the calls that started them.
_CLOCK_SLACK = 5.0
# The worker thread exits after this long idle, and restarts on the next turn.
_IDLE_EXIT = 60.0


@dataclass
class _Parent:
    """The LangSmith run active when a turn was started, so the turn nests under it."""

    trace_id: str
    run_id: str
    dotted_order: str


# (project, address) a turn is sent to, as `_addressing.resolve` returns it.
_Destination = tuple[Optional[str], Optional[Any]]


@dataclass
class _Session:
    since: float
    registrations: list[tuple[float, Optional[_Parent], _Destination]] = field(default_factory=list)
    seen: set[str] = field(default_factory=set)
    parents: dict[str, tuple[Optional[_Parent], Optional[_Destination]]] = field(default_factory=dict)
    finished_at: dict[str, float] = field(default_factory=dict)
    done: set[str] = field(default_factory=set)
    usage_wait_since: dict[str, float] = field(default_factory=dict)
    turn_numbers: dict[str, int] = field(default_factory=dict)
    sandbox_type: Optional[str] = None


def _attr(key: str, value: Any) -> dict:
    if isinstance(value, int) and not isinstance(value, bool):
        return {"key": key, "value": {"intValue": str(value)}}
    return {"key": key, "value": {"stringValue": value if isinstance(value, str) else json.dumps(value, default=str)}}


def _spans(otlp: dict) -> list[dict]:
    return [
        span
        for resource_spans in otlp.get("resourceSpans", [])
        for scope_spans in resource_spans.get("scopeSpans", [])
        for span in scope_spans.get("spans", [])
    ]


def _run_id(span: dict) -> uuid.UUID:
    """Deterministic UUIDv7 from the span start (ms) and span id, so a re-post hits the same run (409)."""
    ms = int(span["startTimeUnixNano"]) // 1_000_000 & (2**48 - 1)
    rand = int(span["spanId"], 16)  # 64 bits: 12 go in rand_a, 62 in rand_b
    value = ms << 80 | 0x7 << 76 | (rand >> 52 & 0xFFF) << 64 | 0b10 << 62 | rand & (2**62 - 1)
    return uuid.UUID(int=value)


def _dotted_part(span: dict) -> str:
    start = datetime.fromtimestamp(int(span["startTimeUnixNano"]) / 1e9, timezone.utc)
    return start.strftime("%Y%m%dT%H%M%S%fZ") + str(_run_id(span))


def _retry_after(error: Any) -> float:
    """Seconds to pause after a 429: the Retry-After header when present, within _RATE_LIMIT_BACKOFF."""
    headers = getattr(getattr(error, "response", None), "headers", None) or {}
    value = headers.get("retry-after") or ""
    try:
        seconds = float(value)
    except (TypeError, ValueError):
        try:  # Retry-After can also be an HTTP date
            seconds = (email.utils.parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds()
        except (TypeError, ValueError):
            seconds = _RATE_LIMIT_BACKOFF[0]
    return min(max(seconds, 0.0), _RATE_LIMIT_BACKOFF[1])


def _is_agent(span: dict) -> bool:
    return span.get("name") == "invoke_agent" or span.get("name", "").startswith("invoke_agent ")


def _usage_ready(otlp: dict) -> bool:
    """True once every agent span carries its token usage."""
    return all(
        any(a["key"] == "gen_ai.usage.input_tokens" for a in s.get("attributes", []))
        for s in _spans(otlp)
        if _is_agent(s)
    )


def _status_to_exception(spans: list[dict]) -> None:
    """Add an exception event to failed spans: OpenAI only sets the status, LangSmith reads the events."""
    for span in spans:
        status = span.get("status") or {}
        failed = status.get("code") in (2, "STATUS_CODE_ERROR")
        if failed and not any(e.get("name") == "exception" for e in span.get("events") or []):
            span.setdefault("events", []).append(
                {
                    "name": "exception",
                    "timeUnixNano": span.get("endTimeUnixNano") or span.get("startTimeUnixNano"),
                    "attributes": [_attr("exception.message", status.get("message") or "error")],
                }
            )


_SESSION_ID_KEY = "openai.managed_agents.session.id"


def _move_usage_to_last_model_call(spans: list[dict]) -> None:
    """Agent spans become chains; their usage moves to their last model call (OpenAI has none per call)."""
    for agent in (s for s in spans if _is_agent(s)):
        attributes = agent.setdefault("attributes", [])
        usage = [a for a in attributes if a["key"].startswith("gen_ai.usage.")]
        agent["attributes"] = [a for a in attributes if not a["key"].startswith("gen_ai.usage.")]
        agent["attributes"].append(_attr("langsmith.span.kind", "chain"))
        calls = [s for s in spans if s.get("parentSpanId") == agent["spanId"] and s.get("name", "").startswith("chat")]
        if usage and calls:
            last = max(calls, key=lambda s: int(s.get("endTimeUnixNano") or 0))
            last.setdefault("attributes", []).extend([*usage, _attr("langsmith.metadata.usage_scope", "agent_total")])
        elif usage:
            agent["attributes"].extend(usage)  # no model call to carry it


_TURN_ID_KEY = "openai.managed_agents.turn.id"
_SUBAGENT_ID_KEY = "openai.managed_agents.subagent.id"


def _str_attr(span: dict, key: str) -> Optional[str]:
    return next((a["value"].get("stringValue") for a in span.get("attributes", []) if a["key"] == key), None)


def _prepare_otlp(
    otlp: dict,
    parent: Optional[_Parent],
    metadata: dict[str, Any],
    tags: list[str],
    turn_number: Optional[int] = None,
    sandbox_type: Optional[str] = None,
) -> dict:
    """A copy of one turn's OTLP ready for LangSmith, nested under `parent` if any.

    Ids go in langsmith.* attributes: an OTLP span id can't hold a 16-byte run id.
    """
    otlp = copy.deepcopy(otlp)
    spans = _spans(otlp)
    _move_usage_to_last_model_call(spans)
    _status_to_exception(spans)
    by_id = {span["spanId"]: span for span in spans}
    dotted: dict[str, str] = {}

    def dotted_order(span: dict) -> str:
        if span["spanId"] not in dotted:
            parent_span = by_id.get(span.get("parentSpanId", ""))
            prefix = dotted_order(parent_span) if parent_span else (parent.dotted_order if parent else None)
            dotted[span["spanId"]] = f"{prefix}.{_dotted_part(span)}" if prefix else _dotted_part(span)
        return dotted[span["spanId"]]

    def root_of(span: dict) -> dict:
        parent_span = by_id.get(span.get("parentSpanId", ""))
        return root_of(parent_span) if parent_span else span

    def agent_of(span: Optional[dict]) -> Optional[dict]:
        while span is not None and not _is_agent(span):
            span = by_id.get(span.get("parentSpanId", ""))
        return span

    for span in spans:
        parent_span = by_id.get(span.get("parentSpanId", ""))
        attributes = span.setdefault("attributes", [])
        # coding-agent-v1 trace metadata, on every run. Unknown values are left out.
        agent = agent_of(span)
        is_subagent = agent is not None and agent_of(by_id.get(agent.get("parentSpanId", ""))) is not None
        contract = {
            "ls_agent_purpose": "coding",
            "ls_integration": "openai-agents-api",
            "ls_agent_runtime": "OpenAI Agents API",
            "ls_trace_schema_version": "coding-agent-v1",
            "ls_integration_version": get_package_version("langsmith"),
            "ls_agent_runtime_version": get_package_version("openai"),
            "thread_id": _str_attr(span, _SESSION_ID_KEY),  # one LangSmith thread per OpenAI session
            "turn_id": _str_attr(span, _TURN_ID_KEY),
            "turn_number": turn_number,
            "ls_agent_type": ("subagent" if is_subagent else "root") if agent else None,
            "ls_subagent_id": _str_attr(agent, _SUBAGENT_ID_KEY) if agent and is_subagent else None,
            "sandbox_type": sandbox_type,
        }
        if not parent_span:
            # User metadata goes on the root; it can override thread_id, not the contract.
            contract = {
                **metadata,
                **contract,
                **({"thread_id": metadata["thread_id"]} if "thread_id" in metadata else {}),
            }
        attributes.extend(_attr(f"langsmith.metadata.{k}", v) for k, v in contract.items() if v not in (None, ""))
        attributes += [
            _attr("langsmith.trace.id", parent.trace_id if parent else str(_run_id(root_of(span)))),
            _attr("langsmith.span.id", str(_run_id(span))),
            _attr("langsmith.span.dotted_order", dotted_order(span)),
        ]
        if parent_span:
            attributes.append(_attr("langsmith.span.parent_id", str(_run_id(parent_span))))
        elif parent:
            attributes.append(_attr("langsmith.span.parent_id", parent.run_id))
        if not parent_span and tags:
            attributes.append(_attr("langsmith.span.tags", ",".join(tags)))
    return otlp


class _TraceForwarder:
    """Watches registered sessions on one OpenAI client and forwards finished turns' traces."""

    def __init__(self, openai_client: Any, tracing_extra: dict) -> None:
        self._user_client = openai_client
        self._openai: Any = None  # sync twin of the user's client, built on first use by the worker
        self._disabled = False
        self._ls_client = tracing_extra.get("client")
        self._project_name = tracing_extra.get("project_name")
        self._address = tracing_extra.get("address")
        self._metadata = dict(tracing_extra.get("metadata") or {})
        self._tags = list(tracing_extra.get("tags") or [])
        # ponytail: keeps per-session state for the process lifetime; prune finished sessions if this grows
        self._sessions: dict[str, _Session] = {}
        self._active: set[str] = set()
        self._cond = threading.Condition()
        self._thread: Optional[threading.Thread] = None
        self._paused_until = 0.0  # monotonic time; set when OpenAI rate-limits the worker
        self._exiting = False  # at interpreter exit, send traces without waiting for token usage
        _FORWARDERS.add(self)

    def _destination(self, run_tree: Any = None) -> _Destination:
        """Where a turn goes, as for a `@traceable` run: its parent's, else the first level naming one."""
        if run_tree:
            return run_tree.session_name, run_tree.address
        return _addressing.resolve(
            (_context._PROJECT_NAME.get(), _context._ADDRESS.get()),
            (self._project_name, self._address),
            (_context._GLOBAL_PROJECT_NAME, _context._GLOBAL_ADDRESS),
        )

    def remember_sandbox(self, session_id: Optional[str], sandbox_type: Optional[str]) -> None:
        """Keep the session's environment type for sandbox_type, known only from the create call."""
        if session_id and sandbox_type:
            with self._cond:
                self._sessions.setdefault(
                    session_id, _Session(since=time.time() - _CLOCK_SLACK)
                ).sandbox_type = sandbox_type

    def register(self, session_id: Optional[str], started_at: Optional[float] = None) -> None:
        """Watch `session_id` for the turn the caller started at `started_at`. Never raises."""
        try:
            if not session_id or self._disabled or not ls_utils.tracing_is_enabled():
                return
            run_tree = run_helpers.get_current_run_tree()
            if run_tree is None or not run_tree.dotted_order:
                run_tree = None
            parent = _Parent(str(run_tree.trace_id), str(run_tree.id), run_tree.dotted_order) if run_tree else None
            destination = self._destination(run_tree)  # here: context vars aren't visible to the worker
            now = time.time()
            with self._cond:
                since = (started_at or now) - _CLOCK_SLACK
                session = self._sessions.setdefault(session_id, _Session(since=since))
                session.since = min(session.since, since)  # remember_sandbox may have set it after the call
                session.registrations.append((now, parent, destination))
                self._active.add(session_id)
                if self._thread is None or not self._thread.is_alive():
                    self._thread = threading.Thread(target=self._run, name="langsmith-openai-agents", daemon=True)
                    self._thread.start()
                self._cond.notify_all()
        except Exception:
            logger.debug("Failed to register OpenAI agent session %s for tracing", session_id, exc_info=True)

    def drain(self, session_id: Optional[str] = None, timeout: float = _DRAIN_TIMEOUT) -> bool:
        """Wait until `session_id` (or every session) has no pending trace. Returns False on timeout."""
        deadline = time.monotonic() + timeout

        def pending() -> bool:
            return session_id in self._active if session_id else bool(self._active)

        with self._cond:
            while pending():
                remaining = deadline - time.monotonic()
                if remaining <= 0 or self._thread is None or not self._thread.is_alive():
                    return False
                self._cond.notify_all()
                self._cond.wait(remaining)
        return True

    def forget(self, session_id: Optional[str]) -> None:
        """Stop watching a session that no longer exists, warning about turns that never got a trace."""
        with self._cond:
            if session_id not in self._active:
                return
            self._active.discard(session_id)
            state = self._sessions.get(session_id)
            lost = [t for t in state.finished_at if t not in state.done] if state else []
            self._cond.notify_all()
        if lost:
            logger.warning(
                "OpenAI agent session %s was deleted before OpenAI published the trace of turn(s) %s; not traced.",
                session_id,
                lost,
            )

    def _disable(self, reason: str) -> None:
        """Stop tracing agent sessions for this client, once, and release anyone waiting in drain()."""
        with self._cond:
            if self._disabled:
                return
            self._disabled = True
            # Before waking drain(), whose caller may look for the reason right away.
            logger.warning("OpenAI agent sessions on this client won't be traced to LangSmith: %s", reason)
            self._active.clear()
            self._cond.notify_all()

    def _client(self) -> Any:
        if self._openai is None:
            self._openai = _sync_twin(self._user_client)
        return self._openai

    def _run(self) -> None:
        interval = _POLL_INTERVAL[0]
        while True:
            with self._cond:
                while not self._active:
                    if not self._cond.wait(_IDLE_EXIT) and not self._active:
                        self._thread = None  # register() starts a new one
                        return
                active = list(self._active)
            try:
                self._client()
            except Exception as e:
                self._disable(f"couldn't build a sync OpenAI client from the wrapped one ({e})")
                return
            pause = self._paused_until - time.monotonic()
            if pause > 0:  # rate-limited: drain() and register() wake us, but don't poll before the pause ends
                with self._cond:
                    self._cond.wait(pause)
                continue
            changed = False
            for session_id in active:
                try:
                    changed |= self._poll(session_id)
                except Exception as e:
                    status = getattr(e, "status_code", None)
                    if status == 429:
                        # The rate limit may be shared with the user's own calls: pause everything.
                        self._paused_until = time.monotonic() + _retry_after(e)
                        logger.debug("OpenAI rate-limited agent trace polling; pausing", exc_info=True)
                        break
                    if status == 404:  # deleted elsewhere: its traces are gone too
                        self.forget(session_id)
                    elif status in (401, 403):
                        self._disable(
                            f"OpenAI answered HTTP {status} when listing session traces. Trace export must be "
                            "enabled for the OpenAI organization, and the key needs api.traces.read or "
                            "api.agents.read."
                        )
                        return
                    else:
                        logger.warning(
                            "Failed to forward OpenAI agent traces for session %s", session_id, exc_info=True
                        )
            with self._cond:
                self._cond.notify_all()  # wake drain() callers
                interval = _POLL_INTERVAL[0] if changed else min(interval * 2, _POLL_INTERVAL[1])
                self._cond.wait(interval)

    def _poll(self, session_id: str) -> bool:
        """One pass over a session. Returns True when something moved."""
        sessions = self._client().beta.agents.sessions
        state = self._sessions[session_id]
        now = time.time()
        # ponytail: lists every root turn each pass; page with `after` if sessions grow to hundreds of turns
        roots = [
            t for t in sessions.turns.list(session_id, order="asc", limit=100) if not getattr(t, "subagent_id", None)
        ]
        state.turn_numbers.update({t.id: i for i, t in enumerate(roots, start=1)})
        turns = [t for t in roots if (t.created_at or now) >= state.since]
        changed = False
        for turn in turns:
            if turn.id not in state.seen:
                state.seen.add(turn.id)
                # Pair each new turn with the oldest registration, which carries the parent run.
                state.parents[turn.id] = state.registrations.pop(0)[1:] if state.registrations else (None, None)
                changed = True
            if turn.status in _TERMINAL and turn.id not in state.finished_at:
                state.finished_at[turn.id] = now
                changed = True
        state.registrations = [r for r in state.registrations if now - r[0] < _REGISTRATION_GRACE]

        pending = [t.id for t in turns if t.id in state.finished_at and t.id not in state.done]
        if pending:
            # Start before the oldest pending turn: a held-back turn can publish after later ones.
            ids = [t.id for t in turns]
            first = ids.index(pending[0])
            after = {"after": ids[first - 1]} if first > 0 else {}
            for trace in sessions.traces.list(session_id, order="asc", limit=100, **after):
                if trace.id in state.finished_at and trace.id not in state.done:
                    if not _usage_ready(trace.otlp):
                        waited = now - state.usage_wait_since.setdefault(trace.id, now)
                        if waited < _USAGE_GRACE and not self._exiting:
                            continue  # LangSmith keeps the first copy of a run
                        logger.debug("Forwarding agent turn %s without token usage after %ss", trace.id, waited)
                    parent, destination = state.parents.get(trace.id, (None, None))
                    self._forward(trace.otlp, parent, destination, state.turn_numbers.get(trace.id), state.sandbox_type)
                    state.done.add(trace.id)
                    changed = True
            late = [t for t in pending if t not in state.done and now - state.finished_at[t] > _PUBLISH_TIMEOUT]
            if late:
                logger.warning(
                    "OpenAI published no trace for agent turn(s) %s of session %s within %ss; not traced.",
                    late,
                    session_id,
                    _PUBLISH_TIMEOUT,
                )
                state.done.update(late)

        running = any(t.status not in _TERMINAL for t in turns)
        if not running and not state.registrations and all(t in state.done for t in state.finished_at):
            with self._cond:
                self._active.discard(session_id)
        return changed

    def _forward(
        self,
        otlp: dict,
        parent: Optional[_Parent],
        destination: Optional[_Destination] = None,
        turn_number: Optional[int] = None,
        sandbox_type: Optional[str] = None,
    ) -> None:
        client = self._ls_client or ls_run_trees.get_cached_client()
        project, address = destination or self._destination()
        body = _prepare_otlp(otlp, parent, self._metadata, self._tags, turn_number, sandbox_type)
        client.request_with_retries(
            "POST",
            "/otel/v1/traces",
            request_kwargs={
                "data": json.dumps(body),
                "headers": {
                    "Content-Type": "application/json",
                    **_addressing.otlp_destination_headers(project, address),
                },
            },
            stop_after_attempt=3,
            # 409 = already sent, and it fails the whole request: one turn per POST.
            to_ignore=[ls_utils.LangSmithConflictError],
            _context="OpenAI agent session trace",
        )


_FORWARDERS: weakref.WeakSet[_TraceForwarder] = weakref.WeakSet()


@atexit.register
def _drain_at_exit() -> None:
    for forwarder in list(_FORWARDERS):
        forwarder._exiting = True  # the usage wait outlasts the exit wait: a turn without tokens beats none
        if not forwarder.drain(timeout=_DRAIN_TIMEOUT):
            logger.warning(
                "Exiting before OpenAI published every agent session trace; some turns are not traced. "
                "Traces for turns with background subagents are held by OpenAI until the subagents finish."
            )


def _session_id_of(event: Any) -> Optional[str]:
    session_id = getattr(event, "session_id", None)
    if session_id:
        return session_id
    session = getattr(event, "session", None)
    return getattr(session, "id", None)


def _watch_stream(
    stream: Any, forwarder: _TraceForwarder, started_at: float, sandbox_type: Optional[str] = None
) -> Any:
    """Register the session from the first event that names it, without changing what the user reads."""
    inner = getattr(stream, "_iterator", None)
    if inner is None:
        return stream
    if hasattr(inner, "__anext__"):

        async def aobserve():
            registered = False
            async for event in inner:
                if not registered and (session_id := _session_id_of(event)):
                    forwarder.remember_sandbox(session_id, sandbox_type)
                    forwarder.register(session_id, started_at)
                    registered = True
                yield event

        stream._iterator = aobserve()
    else:

        def observe():
            registered = False
            for event in inner:
                if not registered and (session_id := _session_id_of(event)):
                    forwarder.remember_sandbox(session_id, sandbox_type)
                    forwarder.register(session_id, started_at)
                    registered = True
                yield event

        stream._iterator = observe()
    return stream


def _after_create(result: Any, kwargs: dict, forwarder: _TraceForwarder, started_at: float) -> Any:
    environment = kwargs.get("environment")
    sandbox_type = environment.get("type") if isinstance(environment, dict) else getattr(environment, "type", None)
    if getattr(result, "object", None) == "agent.session":
        forwarder.remember_sandbox(getattr(result, "id", None), sandbox_type)
    if not kwargs.get("input"):
        return result  # no turn starts: a later events.create or sessions.stream registers it
    if getattr(result, "object", None) == "agent.session" and getattr(result, "id", None):
        forwarder.register(result.id, started_at)  # created without a stream: the turn starts a moment later
        return result
    return _watch_stream(result, forwarder, started_at, sandbox_type)


def _warn_beta(starts_turn: bool) -> None:
    """Once per process, before the call like @warn_beta: raising after it would lose the session."""
    if starts_turn and ls_utils.tracing_is_enabled():
        _warn_once("Tracing OpenAI Agents API sessions with wrap_openai is in beta.", stacklevel=5)


def _starts_turn(kwargs: dict) -> bool:
    """Only user messages start a turn; events.create also sends tool results, cancels and approvals."""
    for event in kwargs.get("events") or []:
        event_type = event.get("type") if isinstance(event, dict) else getattr(event, "type", None)
        if event_type == "agent.session.input.message":
            return True
    return False


async def _awaited(value: Any) -> Any:
    return await value


def _sync_twin(client: Any) -> Any:
    """Sync copy of an async client for the worker thread. Its http_client (proxies, mTLS) doesn't carry over."""
    import openai

    if isinstance(client, openai.OpenAI):
        return client
    api_key: Any = client.api_key
    provider = getattr(client, "_api_key_provider", None)
    if provider is not None:

        def api_key() -> str:
            # Also covers `async def __call__` objects; the worker thread has no event loop.
            value = provider()
            return asyncio.run(_awaited(value)) if inspect.isawaitable(value) else value

    return openai.OpenAI(
        api_key=api_key,
        organization=client.organization,
        project=client.project,
        base_url=client.base_url,
        timeout=client.timeout,
        max_retries=client.max_retries,
        default_headers=getattr(client, "_custom_headers", None),
        default_query=getattr(client, "_custom_query", None),
    )


def _is_async_client(client: Any) -> bool:
    # openai's decorated async create fails iscoroutinefunction.
    try:
        import openai

        if isinstance(client, openai.AsyncOpenAI):
            return True
    except ImportError:
        pass
    return inspect.iscoroutinefunction(client.beta.agents.sessions.create)


def wrap_agents_sessions(client: Any, tracing_extra: dict) -> None:
    """Patch `client.beta.agents.sessions` so every turn it starts is traced. No-op on older `openai`."""
    sessions = getattr(getattr(getattr(client, "beta", None), "agents", None), "sessions", None)
    if sessions is None or not hasattr(sessions, "traces"):
        return
    forwarder = _TraceForwarder(client, tracing_extra)  # builds its sync twin lazily, on the worker

    if _is_async_client(client):

        def patch(obj: Any, name: str, before=None, after=None) -> None:
            original = getattr(obj, name)

            @functools.wraps(original)
            async def wrapper(*args: Any, **kwargs: Any) -> Any:
                if before:
                    await asyncio.to_thread(before, args, kwargs)  # may wait: keep the event loop free
                started_at = time.time()
                result = await original(*args, **kwargs)
                return after(result, args, kwargs, started_at) if after else result

            setattr(obj, name, wrapper)

    else:

        def patch(obj: Any, name: str, before=None, after=None) -> None:
            original = getattr(obj, name)

            @functools.wraps(original)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                if before:
                    before(args, kwargs)
                started_at = time.time()
                result = original(*args, **kwargs)
                return after(result, args, kwargs, started_at) if after else result

            setattr(obj, name, wrapper)

    def session_arg(args: tuple, kwargs: dict) -> Optional[str]:
        return args[0] if args else kwargs.get("session_id")

    def after_events_create(result: Any, args: tuple, kwargs: dict, started_at: float) -> Any:
        if _starts_turn(kwargs):
            forwarder.register(session_arg(args, kwargs), started_at)
        return result

    patch(
        sessions,
        "create",
        before=lambda a, k: _warn_beta(bool(k.get("input"))),
        after=lambda result, a, k, started_at: _after_create(result, k, forwarder, started_at),
    )
    # Also covers sessions.stream, which sends its input through events.create.
    patch(sessions.events, "create", before=lambda a, k: _warn_beta(_starts_turn(k)), after=after_events_create)
    # Deleting a session deletes its traces: forward pending ones first.
    patch(
        sessions,
        "delete",
        before=lambda a, k: forwarder.drain(session_arg(a, k), timeout=_DELETE_DRAIN_TIMEOUT),
        after=lambda result, a, k, started_at: (forwarder.forget(session_arg(a, k)), result)[1],
    )
