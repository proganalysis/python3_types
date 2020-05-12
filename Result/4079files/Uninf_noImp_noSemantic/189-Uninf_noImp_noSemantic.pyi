import asyncio
import logging
from MoMMI import MChannel
from typing import Any, Dict, List, Tuple, TypeVar

LOGGER: logging.Logger
CHANGELOG_EMOJIS: Any
CACHE_CHANGELOG_NAMES: str

async def load(loop: asyncio.AbstractEventLoop) -> None: ...
async def changelog_comm_event(channel: MChannel, message: Any, meta: str) -> None: ...
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

def dicttotuples(d: Dict[TKey, TValue]) -> List[Tuple[TKey, TValue]]: ...
