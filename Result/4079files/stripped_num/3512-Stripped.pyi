# (generated with --quick)

import collections
from typing import Any, Type

OrderedDict: Type[collections.OrderedDict]
datetime: module
get_brace_style_log_with_null_handler: Any
get_now_utc_pendulum: Any
log: Any
timer: MultiTimer

class MultiTimer(object):
    __doc__: str
    _count: collections.OrderedDict[Any, int]
    _overallstart: Any
    _stack: list
    _starttimes: collections.OrderedDict
    _timing: Any
    _totaldurations: collections.OrderedDict[Any, datetime.timedelta]
    def __init__(self, start = ...) -> None: ...
    def report(self) -> None: ...
    def reset(self) -> None: ...
    def set_timing(self, timing, reset = ...) -> None: ...
    def start(self, name, increment_count = ...) -> None: ...
    def stop(self, name) -> None: ...

class MultiTimerContext(object):
    __doc__: str
    name: Any
    timer: Any
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, multitimer, name) -> None: ...
