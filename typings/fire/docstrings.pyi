import enum
from typing import NamedTuple

from _typeshed import Incomplete

class DocstringInfo(
    NamedTuple(
        "DocstringInfo",
        [
            ("summary", Incomplete),
            ("description", Incomplete),
            ("args", Incomplete),
            ("returns", Incomplete),
            ("yields", Incomplete),
            ("raises", Incomplete),
        ],
    )
): ...
class ArgInfo(
    NamedTuple(
        "ArgInfo",
        [("name", Incomplete), ("type", Incomplete), ("description", Incomplete)],
    )
): ...
class KwargInfo(ArgInfo): ...

class Namespace(dict):
    def __getattr__(self, key): ...
    def __setattr__(self, key, value) -> None: ...
    def __delattr__(self, key) -> None: ...

class Sections(enum.Enum):
    ARGS: int
    RETURNS: int
    YIELDS: int
    RAISES: int
    TYPE: int

class Formats(enum.Enum):
    GOOGLE: int
    NUMPY: int
    RST: int

SECTION_TITLES: Incomplete

def parse(docstring): ...
