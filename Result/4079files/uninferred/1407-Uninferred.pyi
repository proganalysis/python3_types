import asyncio
from typing import Any

__author__: str

@asyncio.coroutine
def handle_msg(reader: Any, writer: Any) -> None: ...

loop: Any
coro: Any
server: Any
