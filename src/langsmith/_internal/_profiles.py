"""LangSmith profile configuration and auth helpers."""

from __future__ import annotations

import datetime
import json
import os
import sys
import tempfile
import threading
import time
import urllib.parse
import warnings
from collections.abc import Mapping
from pathlib import Path
from types import FrameType
from typing import Any, NamedTuple, Optional, TypedDict, cast

import requests

from langsmith import utils as ls_utils
from langsmith._internal._oauth_refresh_lock import _LOCK_STALE_AFTER as _OAUTH_REFRESH_LOCK_STALE_AFTER
from langsmith._internal._oauth_refresh_lock import oauth_refresh_lock

DEFAULT_API_URL = "https://api.smith.langchain.com"
_OAUTH_CLIENT_ID = "langsmith-cli"
_TOKEN_REFRESH_LEEWAY = datetime.timedelta(minutes=1)
_TOKEN_REFRESH_TIMEOUT = 10
_OAUTH_DISCOVERY_TIMEOUT = 5
_WELL_KNOWN_OAUTH_PATH = "/.well-known/oauth-authorization-server"
# Trailing separator so a sibling package such as langsmith_helpers is not matched.
_PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep


def _user_stacklevel() -> int:
    """Return the ``stacklevel`` of the first caller outside this package.

    The client is created from user code directly or from deep inside ``@traceable``,
    so a fixed ``stacklevel`` cannot point a warning at the user's line.
    """
    frame: Optional[FrameType] = sys._getframe(2)
    level = 2
    while frame is not None and frame.f_code.co_filename.startswith(_PACKAGE_DIR):
        frame = frame.f_back
        level += 1
    return level


class ProfileOAuth(TypedDict, total=False):
    access_token: str
    refresh_token: str
    expires_at: str


class ProfileConfig(TypedDict, total=False):
    api_key: str
    # Name of an environment variable holding the API key.
    api_key_env: str
    # Shell command that prints the API key. The CLI and Go SDK run it; this
    # SDK reports it as unsupported instead of running unauthenticated.
    api_key_cmd: str
    api_url: str
    workspace_id: str
    oauth: ProfileOAuth


class ProfileConfigFile(TypedDict, total=False):
    current_profile: str
    profiles: dict[str, ProfileConfig]


class ProfileState(NamedTuple):
    path: Path
    config: ProfileConfigFile
    profile_name: str


class ProfileClientConfig(NamedTuple):
    api_url: Optional[str] = None
    api_key: Optional[str] = None
    workspace_id: Optional[str] = None
    oauth_access_token: Optional[str] = None
    oauth_refresh_token: Optional[str] = None
    oauth_expires_at: Optional[str] = None
    profile_state: Optional[ProfileState] = None
    api_key_env: Optional[str] = None
    api_key_cmd: Optional[str] = None

    @property
    def has_oauth(self) -> bool:
        return bool(self.oauth_access_token or self.oauth_refresh_token)

    def resolve_api_key(self) -> Optional[str]:
        """Return the profile's API key, reading ``api_key_env`` when no ``api_key`` is set.

        ``api_key`` wins over ``api_key_env``, which wins over ``api_key_cmd``. A key that
        cannot be resolved warns and returns ``None``, as a missing key does, because
        ``@traceable`` creates the client inside the caller's code and tracing must not
        break it. That covers an unset environment variable and ``api_key_cmd``, which
        this SDK does not run.

        The client calls this once when it is created, so changing the environment
        variable later does not affect an existing client. The JS and Java SDKs read it
        on each request.
        """
        if self.api_key:
            return self.api_key
        profile_name = self.profile_state.profile_name if self.profile_state else ""
        if self.api_key_env:
            key = os.environ.get(self.api_key_env, "").strip()
            if key:
                return key
            warnings.warn(
                f'LangSmith profile "{profile_name}" reads its API key from ${self.api_key_env}, which is not set',
                ls_utils.LangSmithMissingAPIKeyWarning,
                stacklevel=_user_stacklevel(),
            )
        elif self.api_key_cmd:
            warnings.warn(
                f'LangSmith profile "{profile_name}" gets its API key from a command (api_key_cmd), '
                "which the Python SDK does not support yet. Set api_key_env in the profile, "
                "or set LANGSMITH_API_KEY.",
                ls_utils.LangSmithMissingAPIKeyWarning,
                stacklevel=_user_stacklevel(),
            )
        return None


def trim_auth_value(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    trimmed = value.strip().strip('"').strip("'")
    return trimmed or None


def _profile_config_path(config_path: Optional[str] = None) -> Optional[Path]:
    try:
        config_file = config_path or os.environ.get("LANGSMITH_CONFIG_FILE")
        path = Path(config_file) if config_file else Path.home() / ".langsmith" / "config.json"
        return path.expanduser().resolve()
    except (OSError, RuntimeError):
        return None


def _load_profile_state(profile: Optional[str] = None, config_path: Optional[str] = None) -> Optional[ProfileState]:
    path = _profile_config_path(config_path)
    if path is None or not path.exists():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(raw, dict):
        return None
    profiles = raw.get("profiles")
    if not isinstance(profiles, dict):
        return None
    profile_name = profile or os.environ.get("LANGSMITH_PROFILE")
    if not profile_name:
        current_profile = raw.get("current_profile")
        if isinstance(current_profile, str) and current_profile:
            profile_name = current_profile
        elif "default" in profiles:
            profile_name = "default"
    if not profile_name or not isinstance(profiles.get(profile_name), dict):
        return None
    return ProfileState(path, cast(ProfileConfigFile, raw), profile_name)


def _profile_from_state(state: ProfileState) -> Optional[ProfileConfig]:
    profiles = state.config.get("profiles") or {}
    profile = profiles.get(state.profile_name)
    if not isinstance(profile, dict):
        return None
    return cast(ProfileConfig, profile)


def load_profile_client_config(
    *, profile: Optional[str] = None, config_path: Optional[str] = None
) -> ProfileClientConfig:
    state = _load_profile_state(profile, config_path)
    if state is None:
        return ProfileClientConfig()
    selected_profile = _profile_from_state(state)
    if selected_profile is None:
        return ProfileClientConfig()
    oauth = selected_profile.get("oauth") or {}
    return ProfileClientConfig(
        api_url=selected_profile.get("api_url"),
        api_key=trim_auth_value(selected_profile.get("api_key")),
        workspace_id=selected_profile.get("workspace_id"),
        oauth_access_token=trim_auth_value(oauth.get("access_token")),
        oauth_refresh_token=trim_auth_value(oauth.get("refresh_token")),
        oauth_expires_at=oauth.get("expires_at"),
        profile_state=state,
        api_key_env=trim_auth_value(selected_profile.get("api_key_env")),
        api_key_cmd=trim_auth_value(selected_profile.get("api_key_cmd")),
    )


def _normalize_profile_api_url(api_url: str) -> str:
    while api_url.endswith("/"):
        api_url = api_url[:-1]
    suffix = "/api/v1"
    if api_url.endswith(suffix):
        return api_url[: -len(suffix)]
    return api_url


def _oauth_discovery_candidates(api_url: str) -> list[str]:
    """Metadata base URLs to probe, most specific first.

    The configured mount point comes first, then the self-hosted and SaaS
    locations, so both a bare origin and an explicit ``/api`` resolve.
    """
    given = _normalize_profile_api_url(api_url)
    origin = given[: -len("/api")] if given.endswith("/api") else given

    candidates = []
    for candidate in (given, f"{origin}/api", origin):
        if candidate and candidate != "/api" and candidate not in candidates:
            candidates.append(candidate)
    return candidates


def _validate_oauth_metadata(doc: Mapping[str, Any], base: str) -> bool:
    """Check the document describes the deployment we probed.

    RFC 8414 requires the issuer to match the URL the well-known path was built
    from, and every endpoint must share the issuer's origin. Refresh tokens are
    posted to these endpoints, so an unvalidated document could redirect
    credentials to another host.
    """
    issuer = doc.get("issuer")
    if not isinstance(issuer, str) or issuer.rstrip("/") != base.rstrip("/"):
        return False
    issuer_parts = urllib.parse.urlsplit(issuer)
    for key in ("device_authorization_endpoint", "token_endpoint"):
        endpoint = doc.get(key)
        if not isinstance(endpoint, str) or not endpoint:
            return False
        parts = urllib.parse.urlsplit(endpoint)
        if (parts.scheme, parts.netloc) != (issuer_parts.scheme, issuer_parts.netloc):
            return False
    return True


def _oauth_metadata_urls(base: str) -> list[str]:
    """Metadata URLs for an issuer, RFC 8414 form first.

    RFC 8414 inserts the well-known segment between the origin and the issuer
    path, so ``https://host/api`` is described at
    ``https://host/.well-known/oauth-authorization-server/api``. Deployments
    commonly also serve the appended form, and for a path-less issuer the two
    are identical.
    """
    parts = urllib.parse.urlsplit(base)
    inserted = urllib.parse.urlunsplit((parts.scheme, parts.netloc, f"{_WELL_KNOWN_OAUTH_PATH}{parts.path}", "", ""))
    appended = f"{base}{_WELL_KNOWN_OAUTH_PATH}"
    return [inserted] if inserted == appended else [inserted, appended]


def _fetch_oauth_metadata(url: str, base: str, timeout: float) -> Optional[Mapping[str, Any]]:
    try:
        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            timeout=timeout,
        )
    except Exception:
        # Discovery is best effort: any failure falls back to the configured
        # mount point rather than breaking token refresh.
        return None
    if response.status_code < 200 or response.status_code >= 300:
        return None
    try:
        doc = response.json()
    except ValueError:
        # Self-hosted answers unknown paths with an HTML 200 from the SPA.
        return None
    if not isinstance(doc, Mapping) or not _validate_oauth_metadata(doc, base):
        return None
    return doc


def _resolve_token_endpoint(
    api_url: str, timeout: float = _OAUTH_DISCOVERY_TIMEOUT, deadline: Optional[float] = None
) -> str:
    """Resolve the token endpoint, preferring the deployment's metadata.

    Falls back to ``<mount>/oauth/token`` when no usable document is served. The
    fallback keeps a trailing ``/api`` because self-hosted mounts the
    authorization server under it. Stops probing once the monotonic ``deadline``
    passes.
    """
    for base in _oauth_discovery_candidates(api_url):
        for url in _oauth_metadata_urls(base):
            url_timeout = timeout
            if deadline is not None:
                url_timeout = min(timeout, deadline - time.monotonic())
                if url_timeout <= 0:
                    return f"{_normalize_profile_api_url(api_url)}/oauth/token"
            doc = _fetch_oauth_metadata(url, base, url_timeout)
            if doc is not None:
                return cast(str, doc["token_endpoint"])
    return f"{_normalize_profile_api_url(api_url)}/oauth/token"


def _parse_profile_expires_at(expires_at: str) -> Optional[datetime.datetime]:
    try:
        parsed = datetime.datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=datetime.timezone.utc)
    return parsed


def should_refresh_profile_token(profile: ProfileConfig) -> bool:
    if trim_auth_value(profile.get("api_key")):
        return False
    oauth = profile.get("oauth") or {}
    if not oauth.get("refresh_token"):
        return False
    if not oauth.get("access_token"):
        return True
    expires_at = oauth.get("expires_at")
    if not expires_at:
        return False
    parsed = _parse_profile_expires_at(expires_at)
    if parsed is None:
        return False
    return parsed <= datetime.datetime.now(datetime.timezone.utc) + _TOKEN_REFRESH_LEEWAY


def _profile_access_token_usable(profile: ProfileConfig) -> bool:
    """Whether the cached access token can still authenticate a request."""
    oauth = profile.get("oauth") or {}
    if not trim_auth_value(oauth.get("access_token")):
        return False
    expires_at = oauth.get("expires_at")
    parsed = _parse_profile_expires_at(expires_at) if expires_at else None
    return parsed is None or parsed > datetime.datetime.now(datetime.timezone.utc)


def _refresh_profile_oauth_token(
    api_url: Optional[str],
    refresh_token: str,
    timeout: float = _TOKEN_REFRESH_TIMEOUT,
    deadline: Optional[float] = None,
) -> Optional[dict[str, Any]]:
    if deadline is None:
        deadline = time.monotonic() + timeout
    token_endpoint = _resolve_token_endpoint(
        api_url or DEFAULT_API_URL,
        timeout=min(timeout, _OAUTH_DISCOVERY_TIMEOUT),
        deadline=deadline,
    )
    # Never send the single-use refresh token once the caller has stopped
    # waiting: it will have released the lock and would discard the rotated
    # token, so the next refresher would replay a consumed one.
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        return None
    timeout = min(timeout, remaining)
    try:
        response = requests.post(
            token_endpoint,
            data={
                "grant_type": "refresh_token",
                "client_id": _OAUTH_CLIENT_ID,
                "refresh_token": refresh_token,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=timeout,
        )
    except requests.RequestException:
        return None
    if response.status_code < 200 or response.status_code >= 300:
        return None
    try:
        token = response.json()
    except ValueError:
        return None
    if not isinstance(token, dict) or not token.get("access_token"):
        return None
    return token


def _refresh_profile_oauth_token_before(
    deadline: float, api_url: Optional[str], refresh_token: str
) -> Optional[dict[str, Any]]:
    """Run the token refresh, giving up once the monotonic ``deadline`` passes.

    ``requests`` timeouts apply per connect/read, not to the whole exchange, so
    discovery plus the token POST could otherwise hold the cross-process refresh
    lock past the point where other processes treat it as abandoned. The
    request runs on a daemon thread and its result is discarded if it is late;
    the worker shares the deadline so it never starts the token POST after it.
    """
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        return None
    result: list[Optional[dict[str, Any]]] = []
    error: list[BaseException] = []

    def run() -> None:
        try:
            result.append(_refresh_profile_oauth_token(api_url, refresh_token, timeout=remaining, deadline=deadline))
        except BaseException as e:  # re-raised on the calling thread
            error.append(e)

    worker = threading.Thread(target=run, name="langsmith-oauth-refresh", daemon=True)
    worker.start()
    worker.join(max(0.0, deadline - time.monotonic()))
    if worker.is_alive():
        return None
    if error:
        raise error[0]
    return result[0] if result else None


def _apply_profile_token_response(profile: ProfileConfig, token: Mapping[str, Any]) -> None:
    oauth = profile.setdefault("oauth", {})
    access_token = token.get("access_token")
    if isinstance(access_token, str) and access_token:
        oauth["access_token"] = access_token
    refresh_token = token.get("refresh_token")
    if isinstance(refresh_token, str) and refresh_token:
        oauth["refresh_token"] = refresh_token
    expires_in = token.get("expires_in")
    if isinstance(expires_in, (int, float)) and expires_in > 0:
        expires_at = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=expires_in)
        oauth["expires_at"] = expires_at.isoformat().replace("+00:00", "Z")


def _save_profile_config(path: Path, config: ProfileConfigFile) -> None:
    temp_path = None
    try:
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, prefix=f"{path.name}.", delete=False
        ) as f:
            temp_path = Path(f.name)
            f.write(json.dumps(config, indent=2) + "\n")
        os.replace(temp_path, path)
    except OSError:
        return
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass


class ProfileAuth:
    def __init__(
        self,
        config: ProfileClientConfig,
        *,
        api_key_header: str,
    ) -> None:
        self._state = config.profile_state
        self._api_key_header = api_key_header
        self._lock = threading.Lock()
        self._managed_auth_headers: set[tuple[str, str]] = set()
        self._remember_auth_headers(self._auth_headers(refresh=False))

    @property
    def has_auth(self) -> bool:
        profile = self._profile()
        if profile is None:
            return False
        oauth = profile.get("oauth") or {}
        return bool(
            trim_auth_value(oauth.get("access_token"))
            or trim_auth_value(oauth.get("refresh_token"))
            or trim_auth_value(profile.get("api_key"))
        )

    @property
    def oauth_access_token(self) -> Optional[str]:
        profile = self._profile()
        if profile is None:
            return None
        return trim_auth_value((profile.get("oauth") or {}).get("access_token"))

    def needs_refresh(self) -> bool:
        profile = self._profile()
        return profile is not None and should_refresh_profile_token(profile)

    def current_auth_headers(self) -> dict[str, str]:
        headers = self._auth_headers(refresh=False)
        self._remember_auth_headers(headers)
        return headers

    def get_auth_headers(self) -> dict[str, str]:
        headers = self._auth_headers(refresh=True)
        self._remember_auth_headers(headers)
        return headers

    def prepare_request_headers(self, headers: Mapping[str, str]) -> dict[str, str]:
        """Replace stale profile-managed auth while preserving explicit auth."""
        request_headers = dict(headers)
        for key, value in list(request_headers.items()):
            if self._is_profile_auth_header(key, value):
                del request_headers[key]
        if not self._has_auth_header(request_headers):
            request_headers.update(self.current_auth_headers())
        return request_headers

    def _profile(self) -> Optional[ProfileConfig]:
        if self._state is None:
            return None
        return _profile_from_state(self._state)

    def _auth_headers(self, *, refresh: bool) -> dict[str, str]:
        profile = self._profile()
        if profile is None:
            return {}
        if refresh and should_refresh_profile_token(profile):
            with self._lock:
                profile = self._profile()
                if profile is not None and should_refresh_profile_token(profile):
                    profile = self._refresh(profile)
        return self._headers_from_profile(profile)

    def _reload_profile(self) -> Optional[ProfileConfig]:
        if self._state is None:
            return None
        try:
            raw = json.loads(self._state.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        if not isinstance(raw, dict):
            return None
        profiles = raw.get("profiles")
        if not isinstance(profiles, dict):
            return None
        profile = profiles.get(self._state.profile_name)
        if not isinstance(profile, dict):
            return None
        self._state = ProfileState(
            self._state.path,
            cast(ProfileConfigFile, raw),
            self._state.profile_name,
        )
        return cast(ProfileConfig, profile)

    def _refresh(self, profile: ProfileConfig) -> ProfileConfig:
        if self._state is None:
            return profile
        if trim_auth_value((profile.get("oauth") or {}).get("refresh_token")) is None:
            return profile
        deadline = time.monotonic() + _TOKEN_REFRESH_TIMEOUT
        acquired = False
        try:
            with oauth_refresh_lock(self._state.path, deadline=deadline):
                acquired = True
                fresh = self._reload_profile()
                if fresh is None:
                    return profile
                profile = fresh
                if not should_refresh_profile_token(profile):
                    return profile
                refresh_token = trim_auth_value((profile.get("oauth") or {}).get("refresh_token"))
                if refresh_token is None:
                    return profile
                token = _refresh_profile_oauth_token_before(deadline, profile.get("api_url"), refresh_token)
                if token is None:
                    return profile
                _apply_profile_token_response(profile, token)
                profiles = self._state.config.get("profiles") or {}
                profiles[self._state.profile_name] = profile
                self._state.config["profiles"] = profiles
                _save_profile_config(self._state.path, self._state.config)
                return profile
        except OSError as e:
            # Without the lock the cached refresh token must not be used. An
            # unexpired access token still works; an expired one would only
            # produce opaque 401s, so report why the refresh could not run.
            if not acquired and not _profile_access_token_usable(profile):
                raise ls_utils.LangSmithAuthError(
                    f"Could not refresh the expired OAuth token for LangSmith profile "
                    f"{self._state.profile_name!r}: failed to acquire the refresh lock next to "
                    f"{self._state.path} ({e}). Another process may be refreshing it, or the "
                    "config directory may not be writable; OAuth profiles need a writable "
                    "config. Use an API key for read-only configs. A lock left by a crashed "
                    f"process is released automatically after {_OAUTH_REFRESH_LOCK_STALE_AFTER:g} "
                    "seconds."
                ) from e
            return profile

    def _headers_from_profile(self, profile: Optional[ProfileConfig]) -> dict[str, str]:
        if profile is None:
            return {}
        api_key = trim_auth_value(profile.get("api_key"))
        if api_key:
            return {self._api_key_header: api_key}
        oauth_access_token = trim_auth_value((profile.get("oauth") or {}).get("access_token"))
        if oauth_access_token:
            return {"Authorization": f"Bearer {oauth_access_token}"}
        return {}

    def _remember_auth_headers(self, headers: Mapping[str, str]) -> None:
        for name, value in headers.items():
            if self._is_auth_header_name(name) and value:
                self._managed_auth_headers.add((name.lower(), value))

    def _is_profile_auth_header(self, name: str, value: str) -> bool:
        return (name.lower(), value) in self._managed_auth_headers

    def _has_auth_header(self, headers: Mapping[str, str]) -> bool:
        return any(self._is_auth_header_name(name) and bool(value) for name, value in headers.items())

    def _is_auth_header_name(self, name: str) -> bool:
        return name.lower() in {"authorization", self._api_key_header.lower()}
