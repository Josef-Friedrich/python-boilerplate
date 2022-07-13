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


Publish to PyPI
---------------

poetry build
poetry publish


rst
---

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections


1. # with overline, for parts
2. * with overline, for chapters
3. = for sections
4. - for subsections
5. ^ for subsubsections
6. " for paragraphs

.. code-block:: rst

    section
    =======

    subsection
    ----------

    subsubsection
    ^^^^^^^^^^^^^

    paragraphs
    """"""""""
