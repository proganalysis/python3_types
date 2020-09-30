# (generated with --quick)

from typing import Any, Coroutine

plugin_class = Osc

AsyncIOOSCUDPServer: Any
Dispatcher: Any
MYPY: bool
MonitoredSwitchChange: Any
SimpleUDPClient: Any
asyncio: module
logging: module

class Osc:
    __doc__: str
    client: Any
    config: Any
    dispatcher: Any
    log: logging.Logger
    machine: Any
    server: Any
    def __init__(self, machine) -> None: ...
    def __repr__(self) -> str: ...
    def _notify_switch_changes(self, change) -> None: ...
    def _start(self) -> Coroutine[Any, Any, None]: ...
    def handle_switch(self, switch_name, state) -> None: ...
