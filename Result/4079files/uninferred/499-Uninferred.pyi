from tale import base, driver, pubsub, util
from typing import Any

class Thing:
    x: Any = ...
    def __init__(self) -> None: ...
    def append(self, value: Any, ctx: util.Context) -> None: ...

class FakeDriver(driver.Driver):
    game_clock: Any = ...
    moneyfmt: Any = ...
    def __init__(self) -> None: ...

class Wiretap(pubsub.Listener):
    msgs: Any = ...
    senders: Any = ...
    def __init__(self, target: base.Living) -> None: ...
    def pubsub_event(self, topicname: pubsub.TopicNameType, event: Any) -> None: ...
    def clear(self) -> None: ...

class MsgTraceNPC(base.Living):
    _init_called: bool = ...
    messages: Any = ...
    def init(self) -> None: ...
    def clearmessages(self) -> None: ...
    def tell(self, message: str, *, end: bool=..., format: bool=...) -> base.Living: ...