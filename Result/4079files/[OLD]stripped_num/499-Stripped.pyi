# (generated with --quick)

from typing import Any, TypeVar

base: Any
datetime: module
driver: Any
pubsub: Any
story: Any
util: Any

_TMsgTraceNPC = TypeVar('_TMsgTraceNPC', bound=MsgTraceNPC)

class FakeDriver(Any):
    game_clock: Any
    moneyfmt: Any
    def __init__(self) -> None: ...

class MsgTraceNPC(Any):
    _init_called: bool
    messages: list
    def clearmessages(self) -> None: ...
    def init(self) -> None: ...
    def tell(self: _TMsgTraceNPC, message, *, end = ..., format = ...) -> _TMsgTraceNPC: ...

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
