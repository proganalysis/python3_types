# (generated with --quick)

from typing import Any

Bundle: Any
asyncio: module
clients: set
functools: module
logging: module
sys: module
types: module
websockets: Any

def __getattr__(name) -> Any: ...
def _start_app(log_level, **ws_options) -> None: ...
def run_with_reloader(main_func, extra_files = ..., interval: float = ..., reloader_type: str = ...) -> Any: ...
def start_app(host = ..., port = ..., debug = ..., log_level = ..., **ws_options) -> None: ...
