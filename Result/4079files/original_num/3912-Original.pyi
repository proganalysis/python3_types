# (generated with --quick)

import asyncio.events
import asyncio.locks
import asyncio.tasks
import multiprocessing.context
from typing import Any, Coroutine, Optional, Tuple, Type

AiohttpDevException: Any
ClientSession: Any
Config: Any
Process: Type[multiprocessing.context.Process]
WS: Any
asyncio: module
awatch: Any
logger: Any
os: module
serve_main_app: Any
signal: module
src_reload: Any
sys: module

class AppTask(WatchTask):
    _app: None
    _awatch: Any
    _config: Any
    _loop: asyncio.events.AbstractEventLoop
    _process: multiprocessing.context.Process
    _reloads: int
    _runner: None
    _session: Any
    _task: None
    stopper: asyncio.locks.Event
    template_files: Tuple[str, str, str]
    def __init__(self, config, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def _run(self, live_checks = ...) -> Coroutine[Any, Any, None]: ...
    def _src_reload_when_live(self, checks = ...) -> Coroutine[Any, Any, None]: ...
    def _start_dev_server(self) -> None: ...
    def _stop_dev_server(self) -> None: ...

class LiveReloadTask(WatchTask):
    _app: None
    _awatch: Any
    _loop: asyncio.events.AbstractEventLoop
    _task: None
    stopper: asyncio.locks.Event
    def _run(self) -> Coroutine[Any, Any, None]: ...

class WatchTask:
    _app: Any
    _awatch: Any
    _loop: asyncio.events.AbstractEventLoop
    _task: Optional[asyncio.tasks.Task[nothing]]
    stopper: asyncio.locks.Event
    def __init__(self, path: str, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def _run(self) -> Coroutine[Any, Any, nothing]: ...
    def close(self, *args) -> Coroutine[Any, Any, None]: ...
    def start(self, app) -> Coroutine[Any, Any, None]: ...
