# (generated with --quick)

from typing import Any, Coroutine, Dict, Optional, Type, Union

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
    _brand: str
    _device: dict
    _device_id: Any
    _device_json: Any
    api: Any
    available: bool
    brand: str
    close_allowed: bool
    device_id: int
    name: str
    next_allowed_update: Optional[datetime.datetime]
    open_allowed: bool
    parent_id: Optional[int]
    serial: str
    state: str
    type: str
    def __init__(self, device: dict, brand: str, api) -> None: ...
    @staticmethod
    def _coerce_state_from_string(value: Union[int, str]) -> str: ...
    def _set_state(self, state: int) -> Coroutine[Any, Any, bool]: ...
    def _update_state(self, value: str) -> None: ...
    def close(self) -> Coroutine[Any, Any, bool]: ...
    def close_connection(self) -> Coroutine[Any, Any, None]: ...
    def open(self) -> Coroutine[Any, Any, bool]: ...
    def update(self) -> Coroutine[Any, Any, None]: ...
