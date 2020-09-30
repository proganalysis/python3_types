# (generated with --quick)

from typing import Any, List

base: Any
datetime: module
driver: Any
pubsub: Any
story: Any
util: Any

class FakeDriver(Any):
    game_clock: Any
    moneyfmt: Any
    def __init__(self) -> None: ...

class MsgTraceNPC(Any):
    _init_called: bool
    messages: List[str]
    def clearmessages(self) -> None: ...
    def init(self) -> None: ...
    def tell(self, message: str, *, end: bool = ..., format: bool = ...) -> Any: ...

class Thing:
    x: list
    def __init__(self) -> None: ...
    def append(self, value, ctx) -> None: ...

class Wiretap(Any):
    msgs: list
    senders: list
    def __init__(self, target) -> None: ...
    def clear(self) -> None: ...
    def pubsub_event(self, topicname, event) -> None: ...
