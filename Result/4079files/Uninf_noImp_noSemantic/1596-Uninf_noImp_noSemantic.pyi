import asyncio
from typing import Any

BUF_SIZE: Any
_logger: Any

async def _relay_data_side(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None: ...
async def relay(dreader: asyncio.StreamReader, dwriter: asyncio.StreamWriter, ureader: asyncio.StreamReader, uwriter: asyncio.StreamWriter) -> None: ...
