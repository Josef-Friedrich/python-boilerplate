.. image:: http://img.shields.io/pypi/v/audiorename.svg
    :target: https://pypi.python.org/pypi/audiorename
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/python-project-boilerplate/actions/workflows/test.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/python-project-boilerplate/actions/workflows/test.yml
    :alt: Tests

python_project_boilerplate
==========================

A collection of boilerplate files and templates for my Python projects.

Maybe we should use:
https://github.com/cookiecutter/cookiecutter

Version
-------

``poetry version <rule>``

https://python-poetry.org/docs/cli/#version

.. code-block:: python

    from importlib import metadata
    __version__ = metadata.version('python_project_boilerplate')

bump2version
^^^^^^^^^^^^

``.bumpversion.cfg```

.. code-block:: ini

    [bumpversion]
    commit = True
    tag = True
    current_version = 0.1.0

    [bumpversion:file:pyproject.toml]
    search = version = "{current_version}"
    replace = version = "{new_version}"

    [bumpversion:file:python_project_boilerplate/__init__.py]
    search = __version__ = '{current_version}'
    replace = __version__ = '{new_version}'

Test
----

Place the test files in a folder named ``tests``. ``poetry new``
creates a so called folder. Most projects use this named for the
test folder.

nose2
^^^^^

``tox.ini``

.. code-block:: ini

    [testenv]
    basepython = python3.8
    deps =
        nose2
    commands = nose2 {posargs}


Publish
-------

Publish to PyPI

.. code-block:: shell

    # https://pypi.org/manage/account/token/
    poetry config pypi-token.pypi pypi-waS5vcmcCJ...
    poetry build
    poetry publish

rst
---

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections

1. ``#`` with overline, for parts
2. ``*`` with overline, for chapters
3. ``=`` for sections
4. ``-`` for subsections
5. ``^`` for subsubsections
6. ``"`` for paragraphs

We don’t use parts and chapters in the README files.

.. code-block:: restructuredtext

    section
    =======

    subsection
    ----------

    subsubsection
    ^^^^^^^^^^^^^

    paragraphs
    """"""""""

Type hints
----------

To avoid circular imports

.. code-block:: python

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from . import Process
