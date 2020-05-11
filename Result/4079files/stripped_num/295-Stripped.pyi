# (generated with --quick)

import asyncio.events
from typing import Any, Callable, Coroutine

BASE_URL: str
EMOJI_ENDPOINT: str
aiohttp: Any
argparse: module
asyncio: module
logger: logging.Logger
logging: module
loop: asyncio.events.AbstractEventLoop
lxml: module
os: module

def _argparse() -> argparse.Namespace: ...
def _async_session(auth_cookie) -> Any: ...
def concurrent_http_get(max_concurrent, session) -> Callable[[Any, Any], Any]: ...
def main() -> Coroutine[Any, Any, None]: ...
def parse_emoji_from_page(text) -> Any: ...
def save_to_file(response, name, url, directory) -> None: ...
