test:
	poetry run tox

install:
	poetry install

update:
	poetry lock
	poetry install

doc:
	poetry run tox -e docs

.PHONY: test doc
