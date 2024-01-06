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

class _TextTypes(enum.Enum):
    def __call__(self, *args): ...

class TextTypes(_TextTypes):
    RESOURCE_NAME: int
    URL: int
    USER_INPUT: int
    COMMAND: int
    INFO: int
    URI: int
    OUTPUT: int
    PT_SUCCESS: int
    PT_FAILURE: int
