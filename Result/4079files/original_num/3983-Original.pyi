# (generated with --quick)

import requests.adapters
import requests.sessions
from typing import Any, List, Optional, Type, Union

EDBOWebApiHelper: Any
HTTPAdapter: Type[requests.adapters.HTTPAdapter]
config: Any
json: module
requests: module
time: module

class EDBOWebApiConnector(object):
    __doc__: str
    _execution_time: Union[float, int]
    _is_logged_in: bool
    _session: requests.sessions.Session
    _session_start_time: float
    _status: Optional[int]
    default_headers: dict
    execution_time: float
    internal_methods: List[str]
    status: int
    url_prefix: str
    def _EDBOWebApiConnector__login(self, username: str = ..., password: str = ...) -> None: ...
    def _EDBOWebApiConnector__logout(self) -> None: ...
    def __del__(self) -> None: ...
    def __init__(self, username: str = ..., password: str = ...) -> None: ...
    def execute(self, url: str, data: Optional[dict] = ..., headers: Optional[dict] = ..., json_format: bool = ...) -> Any: ...
