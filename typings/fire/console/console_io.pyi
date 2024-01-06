from _typeshed import Incomplete
from fire.console import console_attr as console_attr
from fire.console import console_pager as console_pager
from fire.console import encoding as encoding
from fire.console import files as files

def IsInteractive(
    output: bool = False, error: bool = False, heuristic: bool = False
): ...
def More(
    contents, out, prompt: Incomplete | None = None, check_pager: bool = True
) -> None: ...
