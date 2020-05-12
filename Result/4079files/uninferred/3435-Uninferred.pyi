from .utilities import *
from typing import Any

clients: Any

def _start_app(log_level: Any, **ws_options: Any) -> None: ...
def start_app(host: str = ..., port: int = ..., debug: bool = ..., log_level: Any = ..., **ws_options: Any) -> None: ...
