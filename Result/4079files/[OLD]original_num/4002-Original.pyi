# (generated with --quick)

from typing import Any, List, Tuple, TypeVar

BridgeObject: Any
Variant: Any
bridge: Any
os: module
tempfile: module

AnyStr = TypeVar('AnyStr', str, bytes)

class ThemeUtils(Any):
    _allowed_dirs: Tuple[Any, Any, Any, str]
    _config: Any
    _greeter: Any
    dirlist: Any
    def __init__(self, greeter, config, *args, **kwargs) -> None: ...

def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
