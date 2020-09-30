import asyncio
import logging
from typing import Any

logger: Any

async def aclosing_multiple_writers(*writers: asyncio.StreamWriter) -> Any: ...
async def log_unhandled_exc(logger: logging.Logger) -> Any: ...
