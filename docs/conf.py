# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

import python_project_boilerplate

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

project = "Python project boilerplate"
copyright = "2022, Josef Friedrich"
author = "Josef Friedrich"

version = python_project_boilerplate.__version__
release = python_project_boilerplate.__version__
language = "en"


templates_path = ["_templates"]

exclude_patterns = ["_build"]

html_theme = "alabaster"

html_static_path = ["_static"]
