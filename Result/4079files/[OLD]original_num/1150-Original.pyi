# (generated with --quick)

import threading
from typing import Any, Tuple, Type, Union

Thread: Type[threading.Thread]

class Messenger(threading.Thread):
    _Messenger__armor: None
    _Messenger__health: None
    _Messenger__kills: None
    _Messenger__money: None
    _Messenger__refresh: bool
    _Messenger__start: bool
    _Messenger__status: str
    __doc__: str
    armor: int
    health: int
    kills: tuple
    money: int
    ser_arduino: Any
    status: str
    def __init__(self, ser_arduino) -> None: ...
    def bomb_timer(self) -> None: ...
    def idle(self) -> None: ...
    def shutdown(self) -> None: ...
    def write_player_stats(self) -> None: ...

def asctime(t: Union[time.struct_time, Tuple[int, int, int, int, int, int, int, int, int]] = ...) -> str: ...
def progress(i: int) -> bytes: ...
def sleep(secs: float) -> None: ...
def time() -> float: ...
