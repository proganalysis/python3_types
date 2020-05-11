# (generated with --quick)

import asyncio.futures
import collections
from typing import Any, Coroutine, Dict, List, Optional, Tuple, Type

ALL: str
EVENTS: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
Slacker: Any
__all__: List[str]
asyncio: module
defaultdict: Type[collections.defaultdict]
hashlib: module
importlib: module
itertools: module
json: module
load_plugin: Any
os: module
websockets: Any

class Bot(object):
    _message_id: int
    daemons: Any
    environment: Optional[Dict[str, Any]]
    handlers: collections.defaultdict
    id: Any
    name: Any
    params: Dict[str, Any]
    running: bool
    slack: Any
    uuid: str
    ws: Any
    def __call__(self) -> Coroutine[Any, Any, None]: ...
    def __init__(self, token, daemons = ..., **kwargs) -> None: ...
    def _env_item(self, key, name_or_id, prefix = ...) -> Any: ...
    def get_channel(self, name_or_id) -> Any: ...
    def get_group(self, name_or_id) -> Any: ...
    def get_user(self, name_or_id) -> Any: ...
    def listen(self, coro) -> None: ...
    def ping(self) -> Coroutine[Any, Any, None]: ...
    def post(self, channel_name_or_id, text) -> Coroutine[Any, Any, None]: ...
    def ws_handler(self, url, handler) -> Coroutine[Any, Any, None]: ...
    def ws_keepalive(self) -> Coroutine[Any, Any, None]: ...

class Runner(object):
    registry: dict
    def __init__(self, *bots) -> None: ...
    def add_bot(self, bot) -> None: ...
    def gather(self) -> asyncio.futures.Future[Tuple[Any]]: ...

def run(*bots) -> None: ...
