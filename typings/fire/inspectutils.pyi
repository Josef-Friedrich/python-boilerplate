from _typeshed import Incomplete
from fire import docstrings as docstrings

class FullArgSpec:
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete
    kwonlyargs: Incomplete
    kwonlydefaults: Incomplete
    annotations: Incomplete
    def __init__(
        self,
        args: Incomplete | None = None,
        varargs: Incomplete | None = None,
        varkw: Incomplete | None = None,
        defaults: Incomplete | None = None,
        kwonlyargs: Incomplete | None = None,
        kwonlydefaults: Incomplete | None = None,
        annotations: Incomplete | None = None,
    ) -> None: ...

def Py2GetArgSpec(fn): ...
def Py3GetFullArgSpec(fn): ...
def GetFullArgSpec(fn): ...
def GetFileAndLine(component): ...
def Info(component): ...
def IsNamedTuple(component): ...
def GetClassAttrsDict(component): ...
def IsCoroutineFunction(fn): ...
