# (generated with --quick)

from typing import Any, TypeVar, Union

DeviceType: Any
Keypad: Any
Message: Any
RX_315MHZ_GPIO: int
TX_433MHZ_GPIO: int
Transceiver: Any
bs: MyKeypad
mixer: Any
txr: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class MyKeypad(Any):
    def _process_msg(self, msg) -> None: ...
    def _send(self, msg) -> None: ...
    def backlight(self, on: bool) -> None: ...
    def display(self) -> None: ...

def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
