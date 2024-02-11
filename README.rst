.. image:: http://img.shields.io/pypi/v/python-boilerplate.svg
    :target: https://pypi.org/project/python-boilerplate
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/python-boilerplate/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/python-boilerplate/actions/workflows/tests.yml
    :alt: Tests

python_boilerplate
==========================

My other project boilerplates:
------------------------------

* `TeX <https://github.com/Josef-Friedrich/tex-project-boilerplate>`_
* `Python <https://github.com/Josef-Friedrich/python-project-boilerplate>`_

A collection of boilerplate files and templates for my Python projects.

Maybe we should use:
https://github.com/cookiecutter/cookiecutter

Poetry
------

ansible-playbook playbook/all/p/poetry.yml

~/.config/pypoetry/config.toml

.. code-block:: toml

    virtualenvs.in-project = true

Ruff
----

pipx install ruff

https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff

Version
-------

``poetry version <rule>``

https://python-poetry.org/docs/cli/#version

.. code-block:: python

    from importlib import metadata
    __version__ = metadata.version('python_boilerplate')

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

    [bumpversion:file:python_boilerplate/__init__.py]
    search = __version__ = '{current_version}'
    replace = __version__ = '{new_version}'

Test
----

Place the test files in a folder named ``tests``. ``poetry new``
creates a so called folder. Most projects use this named for the
test folder.

pytest
^^^^^^

Convert unittests to pytest using `pytestify <https://github.com/dannysepler/pytestify>`_.

littlefoxteam.vscode-python-test-adapter

nose2
^^^^^

use pytest instead

``tox.ini``

.. code-block:: ini

    [testenv]
    deps =
        nose2
    commands = nose2 {posargs}

pyright
^^^^^^^

.. code-block:: toml

    [tool.pyright]
    reportPrivateUsage = false
    reportPrivateUsage = false
    reportUnusedExpression = false
    reportInvalidStringEscapeSequence = false

pyenv
^^^^^

::

    pyenv-enable.sh
    pyenv update
    pyenv install --list | grep " 3."
    pyenv install 3.8.13
    pyenv install 3.9.13
    pyenv install 3.11.0b4
    pyenv local 3.8.13 3.9.13 3.11.0b4
    pip install tox tox-pyenv
    tox
    pyenv-disable.sh

Run a single test

::

    tox -e quick -- -s test test_job.TestJobWithConfigParser.test_source

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

Link: `Python <https://github.com/Josef-Friedrich/python-project-boilerplate>`_.

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections

1. ``#`` with overline, for parts
2. ``*`` with overline, for chapters
3. ``=`` for sections
4. ``-`` for subsections
5. ``^`` for subsubsections
6. ``"`` for paragraphs

A Literal Block::

    LITERAL BLOCK

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

mypy
^^^^

matangover.mypy

.. code-block:: toml

    [tool.mypy]
    strict = true

To avoid circular imports

.. code-block:: python

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from . import Process

TypedDict
^^^^^^^^^

.. code-block:: python

    from typing_extensions import TypedDict, Required, NotRequired

    class _trending(TypedDict):
        allStores: NotRequired[bool]
        category: str
        date: str
        average: List[int]

Support for typed **kwargs
^^^^^^^^^^^^^^^^^^^^^^^^^^

https://peps.python.org/pep-0589/

https://github.com/microsoft/pyright/issues/3002#issuecomment-1046100462

.. code-block:: python

    from typing_extensions import Unpack, TypedDict

    class MyKwargs(TypedDict, total=False):
      foo: str
      bar: int

    def baz(**kwargs: Unpack[MyKwargs]) -> None:
      pass

    baz(foo="str", bar=3) # Pylance will affirm these types.

Task runner
-----------

https://github.com/illBeRoy/taskipy

https://github.com/nat-n/poethepoet

Docs
----

Docstring formats: https://stackoverflow.com/a/24385103

use reST

https://github.com/Josef-Friedrich/python-project-boilerplate/settings/pages

Source: Deploy from branch
branch: gh-pages

https://gist.github.com/cobyism/4730490

Use subtree push to send it to the gh-pages branch on GitHub.

.. code-block:: shell

    touch docs/_build/.nojekyll

    git subtree push --prefix docs/_build origin gh-pages

Stub packages
-------------

https://peps.python.org/pep-0561/#stub-only-packages

* https://github.com/lxml/lxml-stubs
* https://github.com/tk0miya/docutils-stubs
* https://github.com/Josef-Friedrich/icinga2apic-stubs
* https://github.com/Josef-Friedrich/nagiosplugin-stubs

Add packages section to pyproject.toml

.. code-block:: toml

    [tool.poetry]
    name = "icinga2apic-stubs"
    version = "0.1.0"
    description = "Type stubs for the icinga2apic package."
    authors = ["Josef Friedrich <josef@friedrich.rocks>"]
    readme = "README.rst"
    repository = "https://github.com/Josef-Friedrich/icinga2apic-stubs"
    license = "MIT"
    packages = [
        {include = "icinga2apic-stubs"}
    ]

    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]

    [tool.poetry.dependencies]
    python = "^3.8"

cli
---

* argparse
* click

cli autcompletion
-----------------

* https://pypi.org/project/shtab
* https://pypi.org/project/argcomplete
* https://github.com/dan1994/pyzshcomplete (not update since 3 years)
* click
