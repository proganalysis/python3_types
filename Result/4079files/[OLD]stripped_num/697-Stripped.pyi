# (generated with --quick)

import threading
from typing import Any, Callable, Type, TypeVar

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
    process: subprocess.Popen[bytes]
    socket: Any
    zmq_context: Any
    def __init__(self, listeners = ..., on_finish = ...) -> None: ...
    def kill(self) -> None: ...
    def on_finish(self, _1: int) -> Any: ...
    def register(self, message_listener) -> Callable[[], Any]: ...
    def send(self, message) -> None: ...

class MessageListener:
    input_on_message: Any
    message_predicate: Any
    one_time: Any
    remove_fn: Any
    def __init__(self, on_message, message_predicate = ..., listen_to = ..., one_time = ...) -> None: ...
    def listen_to(self: _TMessageListener, core) -> _TMessageListener: ...
    def on_message(self, msg) -> bool: ...
    def stop_listening(self: _TMessageListener) -> _TMessageListener: ...

def default_datetime_to_utc(message: _T0) -> _T0: ...
