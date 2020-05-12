# (generated with --quick)

import asyncio.locks
from typing import Any, Coroutine, Dict, List, Optional, Type

API_BASE: str
BRAND_MAPPINGS: Dict[str, Dict[str, str]]
ClientError: Any
ClientSession: Any
DEFAULT_REQUEST_RETRIES: int
DEFAULT_TIMEOUT: int
DEFAULT_USER_AGENT: str
DEVICE_LIST_ENDPOINT: str
LOGIN_ENDPOINT: str
MIN_TIME_BETWEEN_UPDATES: datetime.timedelta
MyQError: Any
RequestError: Any
SUPPORTED_DEVICE_TYPE_NAMES: List[str]
UnsupportedBrandError: Any
_LOGGER: logging.Logger
asyncio: module
datetime: Type[datetime.datetime]
logging: module
timedelta: Type[datetime.timedelta]

class API:
    __doc__: str
    _brand: str
    _credentials: Optional[Dict[str, str]]
    _devices: List[Dict[str, Any]]
    _last_update: Optional[datetime.datetime]
    _security_token: Any
    _security_token_lock: asyncio.locks.Lock
    _supplied_websession: bool
    _update_lock: asyncio.locks.Lock
    _websession: Any
    online: bool
    def __init__(self, brand: str, websession = ...) -> None: ...
    def _create_websession(self) -> None: ...
    def _get_device_states(self) -> Coroutine[Any, Any, bool]: ...
    def _get_security_token(self) -> Coroutine[Any, Any, None]: ...
    def _request(self, method: str, endpoint: str, *, headers: Optional[dict] = ..., params: Optional[dict] = ..., data: Optional[dict] = ..., json: Optional[dict] = ..., login_request: bool = ..., **kwargs) -> Coroutine[Any, Any, Optional[dict]]: ...
    def _store_device_states(self, devices: dict) -> None: ...
    def _update_device_state(self) -> Coroutine[Any, Any, None]: ...
    def authenticate(self, username: str, password: str) -> Coroutine[Any, Any, None]: ...
    def close_websession(self) -> Coroutine[Any, Any, None]: ...
    def get_devices(self, covers_only: bool = ...) -> Coroutine[Any, Any, list]: ...

def login(username: str, password: str, brand: str, websession = ...) -> Coroutine[Any, Any, API]: ...
