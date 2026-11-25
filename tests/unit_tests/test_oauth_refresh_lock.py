"""Tests for the cross-process OAuth refresh lock."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

import pytest

from langsmith._internal import _oauth_refresh_lock as lock_mod
from langsmith._internal import _profiles


def _write_meta(lock_dir: str, created_at: str, owner: str) -> None:
    os.makedirs(lock_dir, exist_ok=True)
    with open(os.path.join(lock_dir, lock_mod._LOCK_METADATA_FILE), "w", encoding="utf-8") as f:
        f.write(created_at + "\n" + owner + "\n")


def _iso_ago(seconds: float) -> str:
    import datetime

    when = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=seconds)
    return when.isoformat().replace("+00:00", "Z")


def test_abandoned_lock_is_taken_over(tmp_path):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    _write_meta(lock_dir, _iso_ago(lock_mod._LOCK_STALE_AFTER + 1), "crashed-owner")
    with lock_mod.oauth_refresh_lock(tmp_path / "config.json", deadline=time.monotonic() + 1):
        assert lock_mod._lock_owner(lock_dir) not in (None, "crashed-owner")
    assert not os.path.exists(lock_dir)


@pytest.mark.parametrize("metadata", [None, "malformed"])
def test_abandoned_lock_without_timestamp_uses_mtime(tmp_path, metadata):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    if metadata is None:
        os.mkdir(lock_dir)
    else:
        _write_meta(lock_dir, metadata, "crashed-owner")
    stale = time.time() - lock_mod._LOCK_STALE_AFTER - 1
    os.utime(lock_dir, (stale, stale))
    with lock_mod.oauth_refresh_lock(tmp_path / "config.json", deadline=time.monotonic() + 1):
        assert lock_mod._lock_owner(lock_dir) not in (None, "crashed-owner")


def test_live_lock_is_not_taken_over(tmp_path):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    _write_meta(lock_dir, _iso_ago(lock_mod._LOCK_STALE_AFTER - 1), "live-owner")
    with pytest.raises(TimeoutError):
        with lock_mod.oauth_refresh_lock(tmp_path / "config.json", deadline=time.monotonic() + 0.05):
            pytest.fail("took over a live lock")
    assert lock_mod._lock_owner(lock_dir) == "live-owner"


def test_stale_threshold_leaves_margin_over_refresh_timeout():
    assert lock_mod._LOCK_STALE_AFTER >= _profiles._TOKEN_REFRESH_TIMEOUT + 5


@pytest.mark.parametrize(
    "stamp",
    [
        "2026-01-01T00:00:00Z",  # Go RFC3339Nano with no fraction
        "2026-01-01T00:00:00.5Z",  # Go trims trailing zeros
        "2026-01-01T00:00:00.123Z",  # JS toISOString
        "2026-01-01T00:00:00.123456789Z",  # Java Instant / Go nanoseconds
    ],
)
def test_lock_timestamps_from_other_sdks_parse(stamp):
    assert lock_mod._parse_lock_timestamp(stamp) is not None


def test_release_dir_lock_keeps_other_owner(tmp_path):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    _write_meta(lock_dir, "2000-01-01T00:00:00Z", "new-owner")

    lock_mod._release_dir_lock(lock_dir, "our-owner")  # owner mismatch
    assert os.path.exists(lock_dir)

    lock_mod._release_dir_lock(lock_dir, "new-owner")  # owner match
    assert not os.path.exists(lock_dir)


def test_release_retries_transient_remove_failure(tmp_path, monkeypatch):
    import shutil

    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    real_rmtree = shutil.rmtree
    failures = {"left": 2}

    def flaky_rmtree(path, *args, **kwargs):
        if failures["left"]:
            failures["left"] -= 1
            raise PermissionError("sharing violation")
        real_rmtree(path, *args, **kwargs)

    with lock_mod._dir_lock(lock_dir, time.monotonic() + 5):
        monkeypatch.setattr(lock_mod.shutil, "rmtree", flaky_rmtree)
    assert failures["left"] == 0
    assert not os.path.exists(lock_dir)


def test_dir_lock_acquires_and_releases(tmp_path):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    with lock_mod._dir_lock(lock_dir, time.monotonic() + 5):
        assert os.path.isdir(lock_dir)
    assert not os.path.exists(lock_dir)


def test_dir_lock_times_out_when_held(tmp_path):
    lock_dir = str(tmp_path / "config.json.oauth.lock.lock")
    with lock_mod._dir_lock(lock_dir, time.monotonic() + 5):
        with pytest.raises(TimeoutError):
            with lock_mod._dir_lock(lock_dir, time.monotonic() + 0.05):
                pass


def test_oauth_refresh_lock_acquires(tmp_path):
    config_path = tmp_path / "sub" / "config.json"
    with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() + 5):
        assert Path(f"{config_path}.oauth.lock.lock").is_dir()
    assert not Path(f"{config_path}.oauth.lock.lock").exists()


def test_oauth_refresh_lock_serializes_same_path(tmp_path):
    config_path = tmp_path / "config.json"
    with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() + 5):
        with pytest.raises((TimeoutError, OSError)):
            with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() + 0.05):
                pass


def _write_config(path: Path, *, access_token: str, expires_at: str) -> None:
    path.write_text(
        json.dumps(
            {
                "current_profile": "default",
                "profiles": {
                    "default": {
                        "api_url": "https://api.smith.langchain.com",
                        "oauth": {
                            "access_token": access_token,
                            "refresh_token": "refresh-abc",
                            "expires_at": expires_at,
                        },
                    }
                },
            }
        ),
        encoding="utf-8",
    )


def test_refresh_skips_network_when_disk_already_fresh(tmp_path, monkeypatch):
    config_path = tmp_path / "config.json"
    past = "2000-01-01T00:00:00Z"  # already expired -> should_refresh == True
    _write_config(config_path, access_token="stale", expires_at=past)
    monkeypatch.setenv("LANGSMITH_CONFIG_FILE", str(config_path))

    calls = {"n": 0}

    def fake_refresh(api_url, refresh_token, timeout=None, deadline=None):
        calls["n"] += 1
        return {
            "access_token": "network-token",
            "refresh_token": "refresh-xyz",
            "expires_in": 3600,
        }

    monkeypatch.setattr(_profiles, "_refresh_profile_oauth_token", fake_refresh)

    # Two independent loads simulate two processes: each gets its own
    # in-memory state, so B does NOT see A's refresh except via disk.
    auth_a = _profiles.ProfileAuth(_profiles.load_profile_client_config(), api_key_header="x-api-key")
    auth_b = _profiles.ProfileAuth(_profiles.load_profile_client_config(), api_key_header="x-api-key")

    headers_a = auth_a.get_auth_headers()
    headers_b = auth_b.get_auth_headers()

    assert calls["n"] == 1
    assert headers_a == {"Authorization": "Bearer network-token"}
    assert headers_b == {"Authorization": "Bearer network-token"}
    on_disk = json.loads(config_path.read_text())
    assert on_disk["profiles"]["default"]["oauth"]["access_token"] == "network-token"


def test_expired_deadline_does_not_create_lock(tmp_path):
    config_path = tmp_path / "config.json"
    with pytest.raises(TimeoutError):
        with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() - 1):
            pytest.fail("acquired after deadline")
    assert not Path(f"{config_path}.oauth.lock.lock").exists()


@pytest.mark.parametrize("contents", [None, "invalid json", '{"profiles": {}}'])
def test_refresh_skips_network_and_save_when_reread_fails(tmp_path, monkeypatch, contents):
    config_path = tmp_path / "config.json"
    _write_config(config_path, access_token="stale", expires_at="2000-01-01T00:00:00Z")
    auth = _profiles.ProfileAuth(
        _profiles.load_profile_client_config(config_path=str(config_path)), api_key_header="x-api-key"
    )
    if contents is None:
        config_path.unlink()
    else:
        config_path.write_text(contents)
    monkeypatch.setattr(
        _profiles, "_refresh_profile_oauth_token", lambda *args, **kwargs: pytest.fail("used cached refresh token")
    )
    assert auth.get_auth_headers() == {"Authorization": "Bearer stale"}
    assert config_path.read_text() == contents if contents is not None else not config_path.exists()


def _iso_in(seconds: float) -> str:
    import datetime

    when = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=seconds)
    return when.isoformat().replace("+00:00", "Z")


@pytest.mark.parametrize(("expires_in", "usable"), [(30, True), (-60, False)])
def test_busy_refresh_lock_uses_unexpired_token_or_raises(tmp_path, monkeypatch, expires_in, usable):
    from langsmith import utils as ls_utils

    config_path = tmp_path / "config.json"
    _write_config(config_path, access_token="cached", expires_at=_iso_in(expires_in))
    auth = _profiles.ProfileAuth(
        _profiles.load_profile_client_config(config_path=str(config_path)), api_key_header="x-api-key"
    )
    monkeypatch.setattr(_profiles, "_TOKEN_REFRESH_TIMEOUT", 0.05)
    monkeypatch.setattr(
        _profiles, "_refresh_profile_oauth_token", lambda *args, **kwargs: pytest.fail("refreshed without the lock")
    )
    with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() + 5):
        if usable:
            assert auth.get_auth_headers() == {"Authorization": "Bearer cached"}
        else:
            with pytest.raises(ls_utils.LangSmithAuthError, match="refresh lock"):
                auth.get_auth_headers()


@pytest.mark.skipif(os.name == "nt" or (hasattr(os, "geteuid") and os.geteuid() == 0), reason="POSIX non-root")
def test_read_only_config_dir_raises_for_expired_token(tmp_path, monkeypatch):
    from langsmith import utils as ls_utils

    config_dir = tmp_path / "ro"
    config_dir.mkdir()
    config_path = config_dir / "config.json"
    _write_config(config_path, access_token="cached", expires_at="2000-01-01T00:00:00Z")
    auth = _profiles.ProfileAuth(
        _profiles.load_profile_client_config(config_path=str(config_path)), api_key_header="x-api-key"
    )
    monkeypatch.setattr(
        _profiles, "_refresh_profile_oauth_token", lambda *args, **kwargs: pytest.fail("refreshed without the lock")
    )
    config_dir.chmod(0o500)
    try:
        with pytest.raises(ls_utils.LangSmithAuthError, match="not be writable"):
            auth.get_auth_headers()
    finally:
        config_dir.chmod(0o700)


def test_config_path_expands_home_and_pins_relative_path(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    assert _profiles._profile_config_path("~/config.json") == tmp_path / "config.json"
    _write_config(tmp_path / "config.json", access_token="stale", expires_at="2000-01-01T00:00:00Z")
    monkeypatch.chdir(tmp_path)
    config = _profiles.load_profile_client_config(config_path="config.json")
    assert config.profile_state is not None
    monkeypatch.chdir(tmp_path.parent)
    assert config.profile_state.path == tmp_path / "config.json"


def test_symlink_config_refresh_preserves_link_and_updates_target(tmp_path, monkeypatch):
    config_path = tmp_path / "config.json"
    _write_config(config_path, access_token="stale", expires_at="2000-01-01T00:00:00Z")
    alias = tmp_path / "alias.json"
    try:
        alias.symlink_to(config_path)
    except OSError:
        pytest.skip("symlinks unavailable")
    monkeypatch.setattr(
        _profiles, "_refresh_profile_oauth_token", lambda *args, **kwargs: {"access_token": "fresh", "expires_in": 3600}
    )
    auth = _profiles.ProfileAuth(
        _profiles.load_profile_client_config(config_path=str(alias)), api_key_header="x-api-key"
    )
    assert auth.get_auth_headers() == {"Authorization": "Bearer fresh"}
    assert alias.is_symlink()
    assert json.loads(config_path.read_text())["profiles"]["default"]["oauth"]["access_token"] == "fresh"
    with lock_mod.oauth_refresh_lock(alias, deadline=time.monotonic() + 5):
        with pytest.raises(TimeoutError):
            with lock_mod.oauth_refresh_lock(config_path, deadline=time.monotonic() + 0.02):
                pytest.fail("alias bypassed lock")


def test_atomic_save_ignores_fixed_temp_and_cleans_up_on_failure(tmp_path, monkeypatch):
    config_path = tmp_path / "config.json"
    config_path.write_text("original")
    fixed_temp = tmp_path / "config.json.tmp"
    fixed_temp.write_text("unrelated")

    def fail_replace(src, dst):
        if os.name != "nt":
            assert Path(src).stat().st_mode & 0o777 == 0o600
        raise OSError("replacement failed")

    monkeypatch.setattr(os, "replace", fail_replace)
    _profiles._save_profile_config(config_path, {"profiles": {}})
    assert config_path.read_text() == "original"
    assert fixed_temp.read_text() == "unrelated"
    assert set(tmp_path.iterdir()) == {config_path, fixed_temp}


def test_slow_refresh_gives_up_at_deadline_and_releases_lock(tmp_path, monkeypatch):
    import threading

    config_path = tmp_path / "config.json"
    _write_config(config_path, access_token="stale", expires_at="2000-01-01T00:00:00Z")
    original = config_path.read_text()
    auth = _profiles.ProfileAuth(
        _profiles.load_profile_client_config(config_path=str(config_path)), api_key_header="x-api-key"
    )
    release = threading.Event()

    def hung_refresh(*args, **kwargs):
        release.wait(5)
        return {"access_token": "too-late", "expires_in": 3600}

    monkeypatch.setattr(_profiles, "_TOKEN_REFRESH_TIMEOUT", 0.1)
    monkeypatch.setattr(_profiles, "_refresh_profile_oauth_token", hung_refresh)
    try:
        started = time.monotonic()
        assert auth.get_auth_headers() == {"Authorization": "Bearer stale"}
        assert time.monotonic() - started < 2
        assert config_path.read_text() == original
        assert not Path(f"{config_path}.oauth.lock.lock").exists()
    finally:
        release.set()


def test_late_discovery_never_posts_refresh_token(monkeypatch):
    import threading

    posted = []
    discovery_done = threading.Event()

    def slow_get(*args, **kwargs):
        time.sleep(0.3)
        discovery_done.set()
        raise _profiles.requests.ConnectionError("slow")

    monkeypatch.setattr(_profiles.requests, "get", slow_get)
    monkeypatch.setattr(_profiles.requests, "post", lambda *a, **k: posted.append(a))

    assert _profiles._refresh_profile_oauth_token_before(time.monotonic() + 0.1, "https://example.com", "rt") is None
    assert discovery_done.wait(2)
    time.sleep(0.1)  # let the abandoned worker reach the POST check
    assert posted == []
