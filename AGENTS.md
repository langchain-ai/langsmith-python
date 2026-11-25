# Instructions for code modifications in the Python SDK

The LangSmith Python SDK source is `sdks/python` in langchainplus: the hand-written client (tracing, run trees, evaluation, sandbox, wrappers, integrations) on top of a Stainless-generated REST client. Both live under `src/langsmith/`. Edit it there. A merge to langchainplus main that changes `sdks/python` is pushed to `langsmith-python` main.

## External contributor PRs

Do not authorize GitHub Actions on external contributors' PRs. To take one over:

1. Review the public PR's diff.
2. From a langchainplus branch off `main`, apply it with its author kept:
   `gh pr diff <number> --repo langchain-ai/langsmith-python --patch | git am -3 --directory=sdks/python`
3. Open the langchainplus PR.
4. Squash-merge it and keep the `Co-authored-by:` trailer GitHub adds for the contributor. The export keeps it, so the `langsmith-python` commit credits them.
5. Close the public PR with a comment that links the exported change.

## Before opening a PR

Run from the repo root:

```
scripts/format
scripts/lint
scripts/test
```

`scripts/test` runs unit tests only. Integration, evaluation and external suites need a live deployment and API keys and run in CI. To run one file or pass pytest args:

```bash
TEST=tests/unit_tests/test_client.py scripts/test
```

Prefer CI over local runs when in doubt: shell or direnv `LANGSMITH_*` variables leak in and cause spurious local failures.

## Generated files

Files whose first line carries `File generated from our OpenAPI spec by Stainless.` are regenerated in langchainplus. Do not edit them by hand. Change the OpenAPI spec or `stainless.yml`, then run `./langdev sdks gen python` from the langchainplus root and commit `sdks/python` with `sdks/tooling/stainless/patches/python.files` and `python.patch`.

Hand-written files are everything not listed in `python.files`. `langdev sdks gen python` keeps edits to generated files in `python.patch`.

## Releasing

Releases are cut by release-please from conventional commits on `langsmith-python` main. Dependency edits in `pyproject.toml` are exported. Do not change the version line in `pyproject.toml`, `src/langsmith/_version.py`, or `.release-please-manifest.json`, and do not push tags.

## Conventions

### Constructing request URLs

Do not hardcode a leading `/v1` (or other `api_url`-dependent prefix) into request
paths. `LANGSMITH_ENDPOINT` may already include `/api/v1`, so a hardcoded
`/v1/...` produces a duplicated `/api/v1/v1/...` path and 404s.

For platform endpoints, build the path with the existing helpers so the `/v1`
prefix is only added when the configured `api_url` does not already end in `/v1`:

- `langsmith._internal._hub.platform_hub_path(api_url)` for hub (agent/skill) repos.
- `_platform_path(api_url, path)` / `_dataset_examples_path(api_url, dataset_id)`
  in `src/langsmith/client.py` for other platform paths.

When adding a new platform endpoint, follow the same pattern instead of inlining
`/v1/platform/...`.
