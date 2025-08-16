from pathlib import Path
from typing import Callable


def test_tmp_path(tmp_path: Path) -> None:
    assert tmp_path.exists()
    assert tmp_path.is_dir()
    assert "pytest-of-" in str(tmp_path)


def test_copy_to_tmp(copy_to_tmp: Callable[[str | Path], Path]) -> None:
    dest = copy_to_tmp("test.txt")
    assert dest.exists()
    assert dest.is_file()
    assert "/tmp/pytest-of-" in str(dest)
    assert dest.read_text() == "test\n"
