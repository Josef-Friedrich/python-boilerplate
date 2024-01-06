from typing import Any, Callable, Sequence

from _typeshed import Incomplete
from fire import completion as completion
from fire import decorators as decorators
from fire import formatting as formatting
from fire import helptext as helptext
from fire import inspectutils as inspectutils
from fire import interact as interact
from fire import parser as parser
from fire import trace as trace
from fire import value_types as value_types
from fire.console import console_io as console_io

def Fire(
    component: object | None = None,
    command: str | Sequence[str] | None = None,
    name: str | None = None,
    serialize: Callable[[Any], Any] | None = None,
) -> Any: ...
def Display(lines, out) -> None: ...
def CompletionScript(name, component, shell): ...

class FireError(Exception): ...

class FireExit(SystemExit):
    trace: Incomplete
    def __init__(self, code, component_trace) -> None: ...
