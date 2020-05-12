# (generated with --quick)

import threading
from typing import Any, Callable, List, Optional, Type, TypeVar

LOG_MESSAGES: bool
Thread: Type[threading.Thread]
os: module
subprocess: module
sys: module
uuid: module
yaml: module
zmq: Any

_T0 = TypeVar('_T0')
_TMessageListener = TypeVar('_TMessageListener', bound=MessageListener)

class ApartCore(threading.Thread):
    ipc_address: str
    listeners: Any
    on_finish: Callable[[int], None]
    process: subprocess.Popen[bytes]
    socket: Any
    zmq_context: Any
    def __init__(self, listeners: Optional[List[MessageListener]] = ..., on_finish: Callable[[int], None] = ...) -> None: ...
    def kill(self) -> None: ...
    def register(self, message_listener: MessageListener) -> Callable[[], None]: ...
    def send(self, message: str) -> None: ...

class MessageListener:
    input_on_message: Callable[[dict], None]
    message_predicate: Callable[[dict], bool]
    one_time: bool
    remove_fn: Any
    def __init__(self, on_message: Callable[[dict], None], message_predicate: Callable[[dict], bool] = ..., listen_to: Optional[ApartCore] = ..., one_time: bool = ...) -> None: ...
    def listen_to(self: _TMessageListener, core: ApartCore) -> _TMessageListener: ...
    def on_message(self, msg: dict) -> bool: ...
    def stop_listening(self: _TMessageListener) -> _TMessageListener: ...

def default_datetime_to_utc(message: _T0) -> _T0: ...
