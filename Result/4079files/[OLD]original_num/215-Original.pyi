# (generated with --quick)

import asyncio.streams
from typing import Any, Coroutine, Optional, Tuple, Type

FlowControlMixin: Type[asyncio.streams.FlowControlMixin]
StreamWriter: Type[asyncio.streams.StreamWriter]
asyncio: module
os: module
reader: Optional[asyncio.streams.StreamReader]
sys: module
writer: Optional[asyncio.streams.StreamWriter]

def async_input(message) -> coroutine: ...
def stdio(loop = ...) -> Coroutine[Any, Any, Tuple[asyncio.streams.StreamReader, asyncio.streams.StreamWriter]]: ...
