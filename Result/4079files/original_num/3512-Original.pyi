# (generated with --quick)

import collections
from typing import Any, List, Type

OrderedDict: Type[collections.OrderedDict]
datetime: module
get_brace_style_log_with_null_handler: Any
get_now_utc_pendulum: Any
log: Any
timer: MultiTimer

class MultiTimer(object):
    __doc__: str
    _count: collections.OrderedDict[str, int]
    _overallstart: Any
    _stack: List[str]
    _starttimes: collections.OrderedDict[str, Any]
    _timing: bool
    _totaldurations: collections.OrderedDict[str, datetime.timedelta]
    def __init__(self, start: bool = ...) -> None: ...
    def report(self) -> None: ...
    def reset(self) -> None: ...
    def set_timing(self, timing: bool, reset: bool = ...) -> None: ...
    def start(self, name: str, increment_count: bool = ...) -> None: ...
    def stop(self, name: str) -> None: ...

class MultiTimerContext(object):
    __doc__: str
    name: str
    timer: MultiTimer
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, multitimer: MultiTimer, name: str) -> None: ...
