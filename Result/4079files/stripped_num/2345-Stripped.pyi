# (generated with --quick)

import asyncio.futures
from typing import Any, Coroutine, List

AsyncTransport: Any
Client: Any
InMemoryCache: Any
asyncio: module
platform: module
signal: module
time: module

def do_call(client, text, number) -> coroutine: ...
def generate_tasks(client) -> List[asyncio.futures.Future]: ...
def main() -> None: ...
def send_messages(client) -> Coroutine[Any, Any, None]: ...
