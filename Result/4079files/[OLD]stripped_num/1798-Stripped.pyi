# (generated with --quick)

from typing import Any, Coroutine

asyncio: module
client: MyClient
discord: Any

class MyClient(Any):
    bg_task: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def my_background_task(self) -> Coroutine[Any, Any, None]: ...
    def on_ready(self) -> Coroutine[Any, Any, None]: ...
