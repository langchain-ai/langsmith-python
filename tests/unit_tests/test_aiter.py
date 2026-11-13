"""Task ownership and cancellation for concurrent asynchronous iteration."""

import asyncio
import functools
import inspect
from unittest.mock import AsyncMock, MagicMock

import pytest

from langsmith._internal._aiter import aiter_with_concurrency, asyncio_accepts_context
from langsmith.evaluation._arunner import AsyncExperimentResults


@pytest.fixture
def recorded_tasks(monkeypatch):
    """Record real tasks without replacing event-loop scheduling."""
    tasks = []
    create_task = asyncio.create_task

    @functools.wraps(create_task)
    def record_task(coro, *args, **kwargs):
        task = create_task(coro, *args, **kwargs)
        tasks.append(task)
        return task

    monkeypatch.setattr(asyncio, "create_task", record_task)
    asyncio_accepts_context.cache_clear()
    try:
        yield tasks
    finally:
        asyncio_accepts_context.cache_clear()


async def _cleanup(tasks, items):
    # Also make failing runs on the original implementation leak-free.
    for task in tasks:
        if not task.done():
            task.cancel()
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    for item in items:
        if inspect.iscoroutine(item) and inspect.getcoroutinestate(item) == inspect.CORO_CREATED:
            item.close()


@pytest.mark.parametrize("eager_timeout", [0, 0.001])
@pytest.mark.parametrize("cleanup_raises", [False, True])
async def test_source_failure_cancels_workers(recorded_tasks, eager_timeout, cleanup_raises):
    """A source error stops owned work and remains the reported exception."""
    started = asyncio.Event()
    cancelled = asyncio.Event()
    items = []

    async def worker():
        started.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            if cleanup_raises:
                raise ValueError("worker cleanup failed")
            raise

    async def source():
        item = worker()
        items.append(item)
        yield item
        await started.wait()
        raise RuntimeError("data source failed")

    iterator = aiter_with_concurrency(2, source(), _eager_consumption_timeout=eager_timeout)
    try:
        with pytest.raises(RuntimeError, match="data source failed"):
            await asyncio.wait_for(anext(iterator), 5)
        assert cancelled.is_set()
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


@pytest.mark.parametrize("concurrency", [2, None])
@pytest.mark.parametrize("eager_timeout", [0, 0.001])
async def test_worker_failure_cancels_siblings(recorded_tasks, concurrency, eager_timeout):
    """An uncaught worker error does not leave siblings running."""
    started = asyncio.Event()
    cancelled = asyncio.Event()
    items = []

    async def blocked():
        started.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            raise

    async def fails():
        await started.wait()
        raise ValueError("worker failed")

    async def source():
        items.extend([blocked(), fails()])
        for item in items:
            yield item

    iterator = aiter_with_concurrency(concurrency, source(), _eager_consumption_timeout=eager_timeout)
    try:
        with pytest.raises(ValueError, match="worker failed"):
            await asyncio.wait_for(anext(iterator), 5)
        assert cancelled.is_set()
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


@pytest.mark.parametrize("concurrency", [2, None])
async def test_closing_iterator_cancels_remaining_workers(recorded_tasks, concurrency):
    """Closing after a yielded result drains the other owned tasks."""
    started = asyncio.Event()
    cancelled = asyncio.Event()
    items = []

    async def first():
        await started.wait()
        return "first"

    async def blocked():
        started.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            raise

    async def source():
        items.extend([first(), blocked()])
        for item in items:
            yield item

    iterator = aiter_with_concurrency(concurrency, source())
    try:
        assert await asyncio.wait_for(anext(iterator), 5) == "first"
        await iterator.aclose()
        assert cancelled.is_set()
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


@pytest.mark.parametrize("concurrency, count", [(2, 1), (None, 3)])
async def test_source_failure_closes_unstarted_items(recorded_tasks, concurrency, count):
    """Cancelling an unstarted wrapper does not leave its item unawaited."""
    started = []

    async def worker(index):
        started.append(index)
        await asyncio.Event().wait()

    items = [worker(index) for index in range(count)]

    async def source():
        for item in items:
            yield item
        raise RuntimeError("source failed before workers start")

    iterator = aiter_with_concurrency(concurrency, source())
    try:
        with pytest.raises(RuntimeError, match="source failed before workers start"):
            await anext(iterator)
        assert not started
        assert all(inspect.getcoroutinestate(item) == inspect.CORO_CLOSED for item in items)
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


def _results_for(source):
    manager = MagicMock()
    manager.experiment_name = "task-cleanup-test"
    manager.aget_results = lambda: aiter_with_concurrency(2, source(), _eager_consumption_timeout=0.001)
    manager.aget_summary_scores = AsyncMock(return_value={"results": []})
    return AsyncExperimentResults(manager)


async def test_cancelling_results_wait_stops_workers(recorded_tasks):
    """Cancelling the blocking waiter stops its producer's worker tasks."""
    started = asyncio.Event()
    cancelled = asyncio.Event()
    items = []

    async def worker():
        started.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            raise

    async def source():
        item = worker()
        items.append(item)
        yield item

    results = _results_for(source)
    waiter = asyncio.create_task(results.wait())
    try:
        await asyncio.wait_for(started.wait(), 5)
        waiter.cancel()
        with pytest.raises(asyncio.CancelledError):
            await waiter
        assert cancelled.is_set()
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


async def test_cancelling_result_consumer_keeps_background_evaluation(recorded_tasks):
    """An individual result consumer does not own the background experiment."""
    started = asyncio.Event()
    release = asyncio.Event()
    items = []

    async def worker():
        started.set()
        await release.wait()
        return "result"

    async def source():
        item = worker()
        items.append(item)
        yield item

    results = _results_for(source)
    consumer = asyncio.create_task(anext(results))
    try:
        await asyncio.wait_for(started.wait(), 5)
        consumer.cancel()
        with pytest.raises(asyncio.CancelledError):
            await consumer
        release.set()
        await asyncio.wait_for(results.wait(), 5)
        assert await anext(results) == "result"
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)


@pytest.mark.parametrize("concurrency", [0, 1, 2, None])
@pytest.mark.parametrize("eager_timeout", [0, 0.001])
@pytest.mark.parametrize("count", [0, 3])
async def test_concurrent_iteration_success_controls(recorded_tasks, concurrency, eager_timeout, count):
    """Normal exhaustion still returns every result, including serial mode."""
    items = []

    async def worker(value):
        await asyncio.sleep(0)
        return value

    async def source():
        for value in range(count):
            item = worker(value)
            items.append(item)
            yield item

    try:
        values = [
            value
            async for value in aiter_with_concurrency(concurrency, source(), _eager_consumption_timeout=eager_timeout)
        ]
        assert sorted(values) == list(range(count))
        assert all(task.done() for task in recorded_tasks)
    finally:
        await _cleanup(recorded_tasks, items)
