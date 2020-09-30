from os.path import dirname as dirname
from pygame import mixer as mixer
from simplisafe import DeviceType as DeviceType
from simplisafe.devices import Keypad
from simplisafe.messages import Message
from typing import Any

RX_315MHZ_GPIO: int
TX_433MHZ_GPIO: int

class MyKeypad(Keypad):
    def _process_msg(self, msg: Message) -> Any: ...
    def _send(self, msg: Message) -> Any: ...
    def backlight(self, on: bool) -> Any: ...
    def display(self) -> None: ...

bs: Any
