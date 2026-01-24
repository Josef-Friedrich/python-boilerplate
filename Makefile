all: test format docs lint type_check

test:
	uv run --isolated --python=3.10 pytest -m "not (slow or gui)"
	uv run --isolated --python=3.11 pytest -m "not (slow or gui)"
	uv run --isolated --python=3.12 pytest -m "not (slow or gui)"
	uv run --isolated --python=3.13 pytest -m "not (slow or gui)"

test_quick:
	uv run --isolated --python=3.12 pytest

install: update

install_editable: install
	uv pip install --editable .

update:
	uv sync --upgrade

build:
	uv build

publish:
	uv build
	uv publish

format:
	uv run ruff check --select I --fix .
	uv run ruff format

docs:
	uv run --isolated readme-patcher
	uv run sphinx-build -W -q docs docs/_build

pin_docs_requirements:
	rm -rf docs/requirements.txt
	uv run pip-compile --strip-extras --output-file=docs/requirements.txt docs/requirements.in pyproject.toml

lint:
	uv run ruff check

type_check:
	uv run mypy typings python_boilerplate tests

.PHONY: test install install_editable update build publish format docs lint pin_docs_requirements
