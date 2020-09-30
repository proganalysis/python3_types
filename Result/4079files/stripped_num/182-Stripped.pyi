# (generated with --quick)

from typing import Any, List

pd: Any

class DrawdownHolder(object):
    __doc__: str
    _dd_start: Any
    depth: Any
    end_date: Any
    length: Any
    max_value: Any
    min_value: Any
    recovery: Any
    start_date: Any
    to_trough: Any
    trough_date: Any
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __init__(self, dd_start) -> None: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...

def find_drawdowns(series) -> List[nothing]: ...
