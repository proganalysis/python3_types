# (generated with --quick)

from typing import Any

CLRMessage: Any

class CLRObjectRefArray(Any):
    __doc__: str
    value: list
    def __init__(self, v = ...) -> None: ...
    def deserialize(self, sock) -> None: ...
    def serialize(self, sock) -> None: ...

def __getattr__(name) -> Any: ...
