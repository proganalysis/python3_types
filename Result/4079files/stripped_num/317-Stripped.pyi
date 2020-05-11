# (generated with --quick)

import types
from typing import Any, Callable, NoReturn, Optional, Union

SIGINT: signal.Signals
SIGTERM: signal.Signals
get_text_type: Any
hug: Any
listen_port: int
os: module
rasmify_get: Any
rasmify_post: Any

def rasmify(text) -> Any: ...
def serve() -> None: ...
def sigint_handler(signum, frame) -> NoReturn: ...
def signal(signalnum: int, handler: Optional[Union[Callable[[signal.Signals, types.FrameType], None], int]]) -> Optional[Union[Callable[[signal.Signals, types.FrameType], None], int]]: ...
def sigterm_handler(signum, frame) -> NoReturn: ...
