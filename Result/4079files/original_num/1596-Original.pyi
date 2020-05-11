# (generated with --quick)

import asyncio.streams
from typing import Any, Coroutine

BUF_SIZE: int
_logger: Any
asyncio: module
contexts: Any
log: Any

def _relay_data_side(reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter) -> Coroutine[Any, Any, None]: ...
def relay(dreader: asyncio.streams.StreamReader, dwriter: asyncio.streams.StreamWriter, ureader: asyncio.streams.StreamReader, uwriter: asyncio.streams.StreamWriter) -> Coroutine[Any, Any, None]: ...
