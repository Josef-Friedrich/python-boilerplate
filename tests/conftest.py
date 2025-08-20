# https://docs.pytest.org/en/stable/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Any, Callable, Generator, Union

import pytest


def __chdir(dest: Path) -> Generator[Path, Any, None]:
    """https://github.com/ar90n/pytest-chdir"""
    last_cwd = os.getcwd()
    os.chdir(dest)
    try:
        yield dest
    finally:
        os.chdir(last_cwd)


@pytest.fixture
def cwd_tmpdir(tmp_path: Path) -> Generator[Path, Any, None]:
    yield from __chdir(tmp_path)


@pytest.fixture
def cwd_test_path() -> Generator[Path, Any, None]:
    yield from __chdir(Path(__file__).parent)


@pytest.fixture
def files_dir() -> Path:
    """
    Returns the path to the ``tests/files`` directory.

    Returns:
        Path: A Path object pointing to the ``tests/files`` directory.
    """
    return Path(__file__).parent / "files"


@pytest.fixture
def copy_to_tmp(tmp_path: Path, files_dir: Path) -> Callable[[Union[str, Path]], Path]:
    def _copy(src: Union[str, Path]) -> Path:
        """
        Copy a file from the specified source path within the ``tests/files`` to a temporary directory.

        Args:
            src (Union[str, Path]): The source file name or path relative to ``tests/files``.

        Returns:
            Path: The path to the copied file in the temporary directory.
        """
        src = files_dir / src
        dest: Path = tmp_path / src.name
        shutil.copy(files_dir / src, dest)
        return dest

    return _copy
