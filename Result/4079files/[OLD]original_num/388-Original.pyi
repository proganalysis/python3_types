# (generated with --quick)

import asyncio.locks
from typing import Any, Coroutine, Type

InvalidDsn: Any
Lock: Type[asyncio.locks.Lock]
RedisCollection: Any
SentryClient: Any
checks: Any
commands: Any
commands_errors: Any
discord: Any

class Sentry:
    __doc__: str
    client: Any
    client_lock: asyncio.locks.Lock
    liara: Any
    set_sentry: Any
    settings: Any
    def __init__(self, liara) -> None: ...
    def on_command_error(self, context, exception) -> Coroutine[Any, Any, None]: ...

def setup(liara) -> None: ...
