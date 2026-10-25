# Contributing

LangSmith SDK changes are developed in internal staging repositories and released from public production repositories.

## Set up the environment

We use [uv](https://docs.astral.sh/uv/) to manage dependencies and the Python version. Run:

```sh
./scripts/bootstrap
```

You can also install uv manually and sync the project:

```sh
uv sync --all-extras
```

Run Python commands with `uv run`, or activate the environment with:

```sh
source .venv/bin/activate
```

## Make changes

Most of the SDK is generated from the LangSmith API definition by Stainless. Do not edit generated files directly. CI rejects changes to files marked `File generated from our OpenAPI spec by Stainless.`

Handwritten client code spans `src/langsmith/`, including `client.py`, `run_trees.py`, `evaluation/`, and `sandbox/`; `langdev sdks gen python` in langchainplus preserves it through regeneration. Check the generated-file marker before editing: marked files should be changed in the API definition or `stainless.yml`, not directly. Handwritten examples belong in `examples/`.

## Add or run an example

Add an executable file under `examples/`, for example `examples/my_example.py`:

```python
#!/usr/bin/env -S uv run python

from langsmith import Client

client = Client()
```

Then run it with:

```sh
chmod +x examples/my_example.py
./examples/my_example.py
```

Examples call the configured LangSmith API, so set the endpoint and credentials for the environment you want to use.

## Use a local build

Build a wheel and install it into the environment you're testing:

```sh
uv build
uv pip install dist/*.whl
```

To install directly from the public production repository, use:

```sh
pip install git+ssh://git@github.com/langchain-ai/langsmith-python.git
```

## Run checks

Run unit tests:

```sh
./scripts/test
```

To run one test file:

```sh
TEST=tests/unit_tests/test_client.py ./scripts/test
```

Format and lint with:

```sh
./scripts/format
./scripts/lint
```

## Open a pull request

External contributors should open issues and pull requests in the public `langsmith-python` repository. Maintainers make the same change in `sdks/python` in langchainplus so the next export does not revert it. An urgent production fix uses the `skip-pr-source-check` label.

Internal changes go in `sdks/python` in langchainplus. After that pull request merges, Copybara opens a pull request on `langsmith-python`. Do not hand-edit the version in `pyproject.toml`, `src/langsmith/_version.py`, or `.release-please-manifest.json`; release-please writes those on `langsmith-python`.
