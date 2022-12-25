.. image:: http://img.shields.io/pypi/v/python-project-boilerplate.svg
    :target: https://pypi.org/project/python-project-boilerplate
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/python-project-boilerplate/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/python-project-boilerplate/actions/workflows/tests.yml
    :alt: Tests

python_project_boilerplate
==========================

A collection of boilerplate files and templates for my Python projects.

Maybe we should use:
https://github.com/cookiecutter/cookiecutter

Poetry
------

Poetry hangs:

.. code-block:: ini

    poetry config experimental.new-installer false

Version
-------

``poetry version <rule>``

https://python-poetry.org/docs/cli/#version

``git tag -sa v1.2.3``

https://semver.org/#is-v123-a-semantic-version

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
    deps =
        nose2
    commands = nose2 {posargs}

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

To avoid circular imports

.. code-block:: python

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from . import Process

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

https://github.com/Josef-Friedrich/python-project-boilerplate/settings/pages

Source: Deploy from branch
branch: gh-pages

https://gist.github.com/cobyism/4730490

Use subtree push to send it to the gh-pages branch on GitHub.

.. code-block:: shell

    touch docs/_build/.nojekyll

    git subtree push --prefix docs/_build origin gh-pages
