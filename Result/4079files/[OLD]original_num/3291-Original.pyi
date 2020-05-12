# (generated with --quick)

from typing import Any

ACTION_LEVEL: Any
ACTION_OFF: Any
ACTION_ON: Any
ACTION_TOGGLE: Any
AUTHOR: Any
COMMANDS: list
DEVICE_TYPE: Any
DEVICE_TYPE_SWITCH: Any
HueDevice: Any
LEVEL: Any
REQUESTS: list
STATE: Any
SWITCH: Any
TITLE: str
logging: Any

class HueLight(Any):
    __doc__: str
    def __init__(self, firefly, package, **kwargs) -> None: ...

def Setup(firefly, package, **kwargs) -> Any: ...
