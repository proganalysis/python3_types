# (generated with --quick)

import simplisafe
import threading
from typing import Any, NoReturn, TextIO, Type, TypeVar

AbstractTransceiver: Any
BaseStationKeypadMessage: Any
ComponentMessage: Any
DeviceType: Type[simplisafe.DeviceType]
KeypadMessage: Any
Message: Any
SensorMessage: Any
Thread: Type[threading.Thread]
os: module
pigpio: Any
socket: module
stderr: TextIO

_TTransceiver = TypeVar('_TTransceiver', bound=Transceiver)

class DecodeError(Exception): ...

class Transceiver(Any):
    _listener: threading.Thread
    _pi: Any
    _read_fd: int
    _rx_buffer: Any
    _rx_done: bool
    _rx_preamble_high: bool
    _rx_preamble_low: bool
    _rx_start_flag0: bool
    _rx_sync_buffer: Any
    _rx_t: Any
    _write_fd: int
    is_receiver: bool
    is_transmitter: bool
    rx: Any
    tx: Any
    def __enter__(self: _TTransceiver) -> _TTransceiver: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _listen(self) -> NoReturn: ...
    def _listen_cbf(self, gpio, level, tick) -> None: ...
    @staticmethod
    def decode(bits) -> bytes: ...
    def fileno(self) -> int: ...
    def recv(self) -> Any: ...
    def send(self, msg, mode = ...) -> None: ...
    def send_script(self, msg) -> None: ...
    def send_wave(self, msg) -> None: ...

def sleep(secs: float) -> None: ...
