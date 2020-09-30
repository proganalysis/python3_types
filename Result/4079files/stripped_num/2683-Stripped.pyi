# (generated with --quick)

from typing import Any, List, Tuple

Parameter: Any
SwitchView: Any
View: Any

class Exhausted(Exception): ...

class ParameterMaker(object):
    __doc__: str
    channel: Any
    exhausted: bool
    expand: Any
    forbidden: List[int]
    interface: Any
    next_cc: Any
    prefix: Any
    def __init__(self, interface, channel, prefix = ..., first_cc = ..., expand = ...) -> None: ...
    def advance(self) -> None: ...
    def make(self, is_button = ...) -> Any: ...
    def skip(self, n) -> None: ...

class ViewMaker(object):
    interface: Any
    next_index: int
    prefix: Any
    def __init__(self, interface, prefix = ...) -> None: ...
    def make(self, view = ...) -> Tuple[Any, Any]: ...
