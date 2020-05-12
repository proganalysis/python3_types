# (generated with --quick)

from typing import Optional

threading: module

class SerialStub:
    _check_read_queue: threading.Event
    _lock: threading.Lock
    _read_canceled: bool
    _read_queue: bytearray
    in_waiting: int
    is_open: bool
    output: list
    def __init__(self) -> None: ...
    def cancel_read(self) -> None: ...
    def close(self) -> None: ...
    def queue_data_for_read(self, data) -> None: ...
    def read(self, size = ...) -> Optional[bytearray]: ...
    def write(self, data) -> None: ...
