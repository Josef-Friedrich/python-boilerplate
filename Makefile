test:
	poetry run tox

install:
	poetry install

update:
	poetry lock
	poetry install

build:
	poetry build

publish:
	poetry build
	poetry publish

doc:
	poetry run tox -e docs

.PHONY: test install update build publish doc
