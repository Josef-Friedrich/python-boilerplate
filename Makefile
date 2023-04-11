test:
	poetry run tox

doc:
	poetry run tox -e docs

.PHONY: test doc
