from _typeshed import Incomplete
from fire import completion as completion
from fire import custom_descriptions as custom_descriptions
from fire import decorators as decorators
from fire import docstrings as docstrings
from fire import formatting as formatting
from fire import inspectutils as inspectutils
from fire import value_types as value_types

LINE_LENGTH: int
SECTION_INDENTATION: int
SUBSECTION_INDENTATION: int

def HelpText(component, trace: Incomplete | None = None, verbose: bool = False): ...
def UsageText(component, trace: Incomplete | None = None, verbose: bool = False): ...

class ActionGroup:
    name: Incomplete
    plural: Incomplete
    names: Incomplete
    members: Incomplete
    def __init__(self, name, plural) -> None: ...
    def Add(self, name, member: Incomplete | None = None) -> None: ...
    def GetItems(self): ...
