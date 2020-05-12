from Firefly.components.hue.hue_device import HueDevice
from Firefly.components.virtual_devices import AUTHOR
from Firefly.const import DEVICE_TYPE_SWITCH, STATE as STATE
from typing import Any

TITLE: str
DEVICE_TYPE = DEVICE_TYPE_SWITCH
AUTHOR = AUTHOR
COMMANDS: Any
REQUESTS: Any

def Setup(firefly: Any, package: Any, **kwargs: Any): ...

class HueLight(HueDevice):
    def __init__(self, firefly: Any, package: Any, **kwargs: Any) -> None: ...
