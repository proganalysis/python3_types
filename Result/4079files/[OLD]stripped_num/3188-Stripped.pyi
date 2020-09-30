# (generated with --quick)

from typing import Any

AnaGondaContext: Any
AnaGondaError: Any
PIPE: int
_go_get: str
shlex: module
spawn: Any
sys: module

class GoGetDoc(Any):
    __doc__: str
    binary: Any
    buf: Any
    offset: Any
    path: Any
    def __enter__(self) -> Any: ...
    def __init__(self, path, offset, buf, env_ctx) -> None: ...
    def doc(self) -> Any: ...

class GoGetDocError(Any):
    __doc__: str
