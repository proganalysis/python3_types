# (generated with --quick)

import concurrent.futures.thread
import functools
from typing import Any, Optional, Type

ThreadPoolExecutor: Type[concurrent.futures.thread.ThreadPoolExecutor]
asyncio: module
partial: Type[functools.partial]

class ThreadedWorkerPool:
    executor: Optional[concurrent.futures.thread.ThreadPoolExecutor]
    loop: Any
    def __init__(self, max_workers, loop = ...) -> None: ...
    def run(self, func, *args, **kwargs) -> coroutine: ...
    def run_sync(self, coro, *args, wait = ..., **kwargs) -> Any: ...
    def shutdown(self, wait = ...) -> None: ...
