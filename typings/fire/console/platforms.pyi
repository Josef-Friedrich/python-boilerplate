from _typeshed import Incomplete

class Error(Exception): ...

class InvalidEnumValue(Error):
    def __init__(self, given, enum_type, options) -> None: ...

class OperatingSystem:
    class _OS:
        id: Incomplete
        name: Incomplete
        file_name: Incomplete
        def __init__(self, id, name, file_name) -> None: ...
        def __eq__(self, other): ...
        def __hash__(self): ...
        def __ne__(self, other): ...
        def __lt__(self, other): ...
        def __gt__(self, other): ...
        def __le__(self, other): ...
        def __ge__(self, other): ...
    WINDOWS: Incomplete
    MACOSX: Incomplete
    LINUX: Incomplete
    CYGWIN: Incomplete
    MSYS: Incomplete
    @staticmethod
    def AllValues(): ...
    @staticmethod
    def FromId(os_id, error_on_unknown: bool = True): ...
    @staticmethod
    def Current(): ...
    @staticmethod
    def IsWindows(): ...

class Architecture:
    class _ARCH:
        id: Incomplete
        name: Incomplete
        file_name: Incomplete
        def __init__(self, id, name, file_name) -> None: ...
        def __eq__(self, other): ...
        def __hash__(self): ...
        def __ne__(self, other): ...
        def __lt__(self, other): ...
        def __gt__(self, other): ...
        def __le__(self, other): ...
        def __ge__(self, other): ...
    x86: Incomplete
    x86_64: Incomplete
    ppc: Incomplete
    arm: Incomplete
    @staticmethod
    def AllValues(): ...
    @staticmethod
    def FromId(architecture_id, error_on_unknown: bool = True): ...
    @staticmethod
    def Current(): ...

class Platform:
    operating_system: Incomplete
    architecture: Incomplete
    def __init__(self, operating_system, architecture) -> None: ...
    @staticmethod
    def Current(
        os_override: Incomplete | None = None, arch_override: Incomplete | None = None
    ): ...
    def UserAgentFragment(self): ...
    def AsyncPopenArgs(self): ...

class PythonVersion:
    MIN_REQUIRED_PY2_VERSION: Incomplete
    MIN_SUPPORTED_PY2_VERSION: Incomplete
    MIN_SUPPORTED_PY3_VERSION: Incomplete
    ENV_VAR_MESSAGE: str
    version: Incomplete
    def __init__(self, version: Incomplete | None = None) -> None: ...
    def SupportedVersionMessage(self, allow_py3): ...
    def IsCompatible(self, allow_py3: bool = False, raise_exception: bool = False): ...