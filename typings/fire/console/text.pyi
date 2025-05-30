import enum

from _typeshed import Incomplete

class TextAttributes:
    def __init__(
        self,
        format_str: Incomplete | None = None,
        color: Incomplete | None = None,
        attrs: Incomplete | None = None,
    ) -> None: ...
    @property
    def format_str(self): ...
    @property
    def color(self): ...
    @property
    def attrs(self): ...

class TypedText:
    texts: Incomplete
    text_type: Incomplete
    def __init__(self, texts, text_type: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __add__(self, other): ...
    def __radd__(self, other): ...

class _TextTypes(enum.Enum):  # type: ignore
    def __call__(self, *args): ...

class TextTypes(_TextTypes):
    """Defines text types that can be used for styling text."""

    RESOURCE_NAME = 1
    URL = 2
    USER_INPUT = 3
    COMMAND = 4
    INFO = 5
    URI = 6
    OUTPUT = 7
    PT_SUCCESS = 8
    PT_FAILURE = 9
