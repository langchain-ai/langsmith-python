"""Cross-process filesystem lock for OAuth token refresh.

Every LangSmith SDK (Python, JS/TS, Go, Java) that shares a profile config uses
the same lock: an exclusive directory created with an atomic ``mkdir`` at
``<config>.oauth.lock.lock``. Its ``created_at`` file holds a UTC timestamp and a
random owner ID. A lock older than ``_LOCK_STALE_AFTER`` is treated as abandoned
(its holder crashed) and taken over. Holders bound their whole refresh to the
refresh timeout, well under that threshold, so a live holder is never evicted.
"""

from __future__ import annotations

import contextlib
import datetime
import os
import secrets
import shutil
import time
from collections.abc import Iterator
from typing import Optional

_LOCK_POLL_INTERVAL = 0.01
_LOCK_STALE_AFTER = 15.0
_LOCK_METADATA_FILE = "created_at"
# On Windows a file cannot be deleted while another process has it open without
# delete sharing (Python and Go open files that way), so removing the lock fails
# if a waiter is reading created_at at that moment. Reads take microseconds; a
# few short retries absorb the overlap.
_LOCK_REMOVE_ATTEMPTS = 10


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def _force_remove(path: str) -> None:
    """Remove the lock directory, retrying briefly if another process has a file open."""
    for attempt in range(_LOCK_REMOVE_ATTEMPTS):
        if attempt:
            time.sleep(_LOCK_POLL_INTERVAL)
        try:
            shutil.rmtree(path)
            return
        except FileNotFoundError:
            return
        except OSError:
            pass


def _write_lock_metadata(lock_dir: str, owner: str) -> None:
    meta = os.path.join(lock_dir, _LOCK_METADATA_FILE)
    fd = os.open(meta, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(_now_iso() + "\n" + owner + "\n")


def _lock_metadata_lines(lock_dir: str) -> Optional[list[str]]:
    try:
        with open(os.path.join(lock_dir, _LOCK_METADATA_FILE), encoding="utf-8") as f:
            return f.read().split("\n")
    except OSError:
        return None


def _parse_lock_timestamp(value: str) -> Optional[float]:
    value = value.strip()
    if not value:
        return None
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    # Other SDKs write between 0 and 9 fractional digits; fromisoformat on
    # Python < 3.11 accepts exactly 3 or 6, so normalize to microseconds.
    date, sep, rest = value.partition(".")
    if sep:
        digits = len(rest) - len(rest.lstrip("0123456789"))
        value = f"{date}.{rest[:digits][:6].ljust(6, '0')}{rest[digits:]}"
    try:
        parsed = datetime.datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=datetime.timezone.utc)
    return parsed.timestamp()


def _lock_created_at(lock_dir: str) -> Optional[float]:
    """Return the lock's timestamp, falling back to the directory's mtime.

    The fallback covers a holder that crashed between ``mkdir`` and writing the
    metadata.
    """
    lines = _lock_metadata_lines(lock_dir)
    if lines:
        parsed = _parse_lock_timestamp(lines[0])
        if parsed is not None:
            return parsed
    try:
        return os.stat(lock_dir).st_mtime
    except OSError:
        return None


def _lock_owner(lock_dir: str) -> Optional[str]:
    lines = _lock_metadata_lines(lock_dir)
    if lines and len(lines) >= 2 and lines[1].strip():
        return lines[1].strip()
    return None


def _remove_stale_lock(lock_dir: str) -> bool:
    created_at = _lock_created_at(lock_dir)
    if created_at is None or time.time() - created_at <= _LOCK_STALE_AFTER:
        return False
    _force_remove(lock_dir)
    return True


def _release_dir_lock(lock_dir: str, owner: str) -> None:
    if _lock_owner(lock_dir) != owner:
        return
    _force_remove(lock_dir)


@contextlib.contextmanager
def _dir_lock(lock_dir: str, deadline: float) -> Iterator[None]:
    owner = secrets.token_hex(16)
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("timed out acquiring OAuth refresh lock")
        try:
            os.mkdir(lock_dir, 0o700)
        except FileExistsError:
            if not _remove_stale_lock(lock_dir):
                time.sleep(min(_LOCK_POLL_INTERVAL, remaining))
            continue
        try:
            _write_lock_metadata(lock_dir, owner)
        except OSError:
            _force_remove(lock_dir)
            raise
        break
    try:
        yield
    finally:
        _release_dir_lock(lock_dir, owner)


def oauth_refresh_lock(config_path, *, deadline: float):
    """Acquire the shared cross-process lock for refreshing OAuth tokens.

    ``config_path`` is the profile config file path; the lock lives beside its
    resolved target. ``deadline`` is a ``time.monotonic()`` value; acquisition
    raises ``TimeoutError`` if the lock cannot be obtained before then.
    """
    config_path = os.path.realpath(os.path.abspath(os.path.expanduser(os.fspath(config_path))))
    parent = os.path.dirname(config_path)
    if parent:
        os.makedirs(parent, mode=0o700, exist_ok=True)
    return _dir_lock(f"{config_path}.oauth.lock.lock", deadline)
