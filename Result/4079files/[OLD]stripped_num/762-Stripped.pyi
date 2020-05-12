# (generated with --quick)

from typing import Any, Coroutine, Dict, Optional, Type

API: Any
DEVICE_ATTRIBUTE_GET_ENDPOINT: str
DEVICE_SET_ENDPOINT: str
RequestError: Any
STATE_CLOSED: str
STATE_CLOSING: str
STATE_MAP: Dict[int, str]
STATE_OPEN: str
STATE_OPENING: str
STATE_STOPPED: str
STATE_TRANSITION: str
STATE_UNKNOWN: str
_LOGGER: logging.Logger
datetime: Type[datetime.datetime]
logging: module
timedelta: Type[datetime.timedelta]

class MyQDevice:
    __doc__: str
    _brand: Any
    _device: Any
    _device_id: Any
    _device_json: Any
    api: Any
    available: Any
    brand: Any
    close_allowed: Any
    device_id: Any
    name: Any
    next_allowed_update: Optional[datetime.datetime]
    open_allowed: Any
    parent_id: Any
    serial: Any
    state: Any
    type: Any
    def __init__(self, device, brand, api) -> None: ...
    @staticmethod
    def _coerce_state_from_string(value) -> str: ...
    def _set_state(self, state) -> Coroutine[Any, Any, bool]: ...
    def _update_state(self, value) -> None: ...
    def close(self) -> Coroutine[Any, Any, bool]: ...
    def close_connection(self) -> Coroutine[Any, Any, None]: ...
    def open(self) -> Coroutine[Any, Any, bool]: ...
    def update(self) -> Coroutine[Any, Any, None]: ...
