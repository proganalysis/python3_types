# (generated with --quick)

import api.common
import requests.exceptions
import threading
from typing import Any, Callable, Match, Optional, Type, Union

ConnectionError: Type[requests.exceptions.ConnectionError]
Lock: Type[threading.Lock]
OK_CODES: list
ReadTimeoutError: Any
RequestError: Type[api.common.RequestError]
RequestException: Type[requests.exceptions.RequestException]
local: Type[threading.local]
logger: logging.Logger
logging: module
random: module
re: module
requests: module
time: module

class BackOffRequest(object):
    _BackOffRequest__lock: threading.Lock
    _BackOffRequest__next_req: float
    _BackOffRequest__retries: int
    _BackOffRequest__session: Any
    _BackOffRequest__thr_local: threading.local
    __doc__: str
    _request: Callable
    auth_callback: Any
    proxies: Any
    timeout: Any
    def _BackOffRequest__calc_next(self) -> None: ...
    def __init__(self, auth_callback, timeout, proxies = ...) -> None: ...
    def _failed(self) -> None: ...
    def _succeeded(self) -> None: ...
    def _wait(self) -> None: ...
    def delete(self, url, acc_codes = ..., **kwargs) -> Any: ...
    def get(self, url, acc_codes = ..., **kwargs) -> Any: ...
    def paginated_get(self, url, params = ...) -> list: ...
    def patch(self, url, acc_codes = ..., **kwargs) -> Any: ...
    def post(self, url, acc_codes = ..., **kwargs) -> Any: ...
    def put(self, url, acc_codes = ..., **kwargs) -> Any: ...

def catch_conn_exception(func) -> Callable: ...
def is_valid_id(id) -> Optional[Union[bool, Match[str]]]: ...
def sleep(secs: float) -> None: ...
