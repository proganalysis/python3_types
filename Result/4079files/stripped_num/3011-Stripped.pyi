# (generated with --quick)

import asyncio.events
from typing import Any, Coroutine

AuthToken: Any
RealTimeClient: Any
RestApiClient: Any
argparse: module
asyncio: module
is_streaming: bool
logger: logging.Logger
logging: module
loop: asyncio.events.AbstractEventLoop
models: Any
os: module
signal: module
textwrap: module

def get_parser() -> argparse.ArgumentParser: ...
def main(args, event_loop) -> Coroutine[Any, Any, None]: ...
def stop() -> None: ...
def stream(client) -> Coroutine[Any, Any, None]: ...
