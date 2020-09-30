# (generated with --quick)

import requests.auth
import requests.models
import requests.sessions
from typing import Any, Optional, Type

HTTPBasicAuth: Type[requests.auth.HTTPBasicAuth]
__author__: str
__license__: str
openhab: Any
re: module
requests: module
typing: module
warnings: module

class OpenHAB:
    __doc__: str
    base_url: str
    session: requests.sessions.Session
    timeout: Optional[float]
    def __init__(self, base_url: str, username: Optional[str] = ..., password: Optional[str] = ..., http_auth: Optional[requests.auth.AuthBase] = ..., timeout: Optional[float] = ...) -> None: ...
    @staticmethod
    def _check_req_return(req: requests.models.Response) -> None: ...
    def fetch_all_items(self) -> dict: ...
    def get_item(self, name: str) -> Any: ...
    def get_item_raw(self, name: str) -> Any: ...
    def json_to_item(self, json_data: dict) -> Any: ...
    def req_get(self, uri_path: str) -> Any: ...
    def req_post(self, uri_path: str, data: Optional[dict] = ...) -> None: ...
    def req_put(self, uri_path: str, data: Optional[dict] = ...) -> None: ...

class openHAB(OpenHAB):
    base_url: str
    session: requests.sessions.Session
    timeout: Optional[float]
    def __init__(self, *args, **kwargs) -> None: ...
