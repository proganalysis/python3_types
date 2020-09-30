# (generated with --quick)

import asyncio.events
import asyncio.futures
import collections
from typing import Any, Awaitable, Coroutine, Dict, Generator, Optional, Type, TypeVar, Union

OrderedDict: Type[collections.OrderedDict]
defaultdict: Type[collections.defaultdict]

_T = TypeVar('_T')
_TChannel = TypeVar('_TChannel', bound=Channel)

class Channel(object):
    __doc__: str
    _channels: Dict[Any, Channel]
    _name: Any
    _name_prefix: str
    _subscribers: collections.defaultdict
    active: bool
    name: str
    def __new__(cls: Type[_TChannel], **kwargs) -> _TChannel: ...
    def consume_events(self) -> Coroutine[Any, Any, nothing]: ...
    def kickoff(self) -> None: ...
    def publish(self, key, data = ...) -> Coroutine[Any, Any, nothing]: ...
    def subscribe(self, event, subscriber) -> None: ...
    def unsubscribe(self, event, subscriber) -> None: ...

def ensure_future(coro_or_future: Union[Generator[Any, None, _T], asyncio.futures.Future[_T], Awaitable[_T]], *, loop: Optional[asyncio.events.AbstractEventLoop] = ...) -> asyncio.futures.Future[_T]: ...
