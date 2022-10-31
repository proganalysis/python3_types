from gevent.queue import Queue
from typing import Any, Iterable, Optional

def generate_id(size: int=..., chars: str=...) -> str: ...

class ServerSentEvent:
    data: Any = ...
    event: Any = ...
    event_id: Any = ...
    desc_map: Any = ...
    def __init__(self, data: str, event: str) -> None: ...
    def encode(self): ...

class Comment:
    msg: Any = ...
    event_id: Any = ...
    def __init__(self, msg: str) -> None: ...
    def encode(self) -> str: ...

class Channel:
    subscriptions: Any = ...
    history: Any = ...
    def __init__(self, history_size: int=...) -> None: ...
    def notify(self, message: str) -> None: ...
    def event_generator(self, last_id: Optional[str]) -> Iterable[ServerSentEvent]: ...
    def subscribe(self): ...
    def _add_history(self, q: Queue, last_id: Optional[str]) -> None: ...
    def publish(self, event: str, message: dict) -> None: ...
    def comment(self, msg: str=...) -> None: ...
    def get_last_id(self) -> str: ...