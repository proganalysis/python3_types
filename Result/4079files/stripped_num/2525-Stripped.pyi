# (generated with --quick)

from typing import Any, Optional

importlib: module
util: Any

class PlayerError(Exception):
    __doc__: str
    long_desc: Any
    short_desc: Any
    def __bytes__(self) -> bytes: ...
    def __init__(self, short_desc, long_desc = ...) -> None: ...
    def __str__(self) -> Any: ...

def init_backend(backend_name) -> Optional[module]: ...
def init_player(backend_name, librarian) -> Any: ...
