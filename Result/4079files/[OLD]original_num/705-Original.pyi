# (generated with --quick)

from typing import Any, NoReturn

EventWatcher: Any
FatalError: Any
Filter: Any
FunctionFilter: Any
OutputThing: Any
Timeout: Any
buffer_with_count: Any
buffer_with_time: Any
buffer_with_time_or_count: Any
datetime: module
filtermethod: Any

class BufferEventUntilTimeoutOrCount(Any):
    __doc__: str
    count: Any
    event_watcher: Any
    interval: Any
    seen: int
    timeout_thing: Any
    def __init__(self, previous_in_chain, event_watcher, scheduler, interval = ..., count = ...) -> None: ...
    def __str__(self) -> str: ...
    def on_completed(self) -> None: ...
    def on_error(self, e) -> None: ...
    def on_next(self, x) -> None: ...
    def on_timeout_completed(self) -> NoReturn: ...
    def on_timeout_error(self, e) -> NoReturn: ...
    def on_timeout_next(self, x) -> None: ...

class BufferEventWatcher(Any):
    q: list
    def __init__(self) -> None: ...
    def on_next(self, x) -> None: ...
    def produce_event_for_timeout(self) -> list: ...
