# (generated with --quick)

import asyncio.queues
import channels
from typing import Any, Coroutine, Type, TypeVar

Channel: Type[channels.Channel]
asyncio: module

_T1 = TypeVar('_T1')

class MemoryChannel(channels.Channel):
    __doc__: str
    _queue: asyncio.queues.Queue[nothing]
    def __init__(self, **kwargs) -> None: ...
    def consume_events(self) -> coroutine: ...
    def publish(self, key, data: _T1 = ...) -> Coroutine[Any, Any, _T1]: ...
