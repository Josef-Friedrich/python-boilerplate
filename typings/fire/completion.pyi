from _typeshed import Incomplete
from fire import inspectutils as inspectutils

def Script(
    name, component, default_options: Incomplete | None = None, shell: str = "bash"
): ...
def MemberVisible(
    component,
    name,
    member,
    class_attrs: Incomplete | None = None,
    verbose: bool = False,
): ...
def VisibleMembers(
    component, class_attrs: Incomplete | None = None, verbose: bool = False
): ...
def Completions(component, verbose: bool = False): ...
