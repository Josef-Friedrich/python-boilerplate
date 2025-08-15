# https://lukasatkinson.de/2025/just-dont-tox/

set shell := ["uv", "run", "bash", "-euxo", "pipefail", "-c"]
set positional-arguments

@all: test docs format

@test:
	uv run --isolated --python=3.10 pytest
	uv run --isolated --python=3.11 pytest
	uv run --isolated --python=3.12 pytest
	uv run --isolated --python=3.13 pytest

@docs:
	uv run --isolated readme-patcherr
	sphinx-build -W -q docs docs/_build

@format:
	ruff check --select I --fix .
	ruff format
