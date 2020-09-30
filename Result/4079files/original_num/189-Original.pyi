# (generated with --quick)

import asyncio.events
from typing import Any, Coroutine, Dict, List, Tuple, TypeVar

CACHE_CHANGELOG_NAMES: str
CHANGELOG_EMOJIS: Dict[str, str]
LOGGER: logging.Logger
MChannel: Any
asyncio: module
changelog_comm_event: Any
comm_event: Any
logging: module
master: Any

TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

def dicttotuples(d: Dict[TKey, TValue]) -> List[Tuple[TKey, TValue]]: ...
def load(loop: asyncio.events.AbstractEventLoop) -> Coroutine[Any, Any, None]: ...
