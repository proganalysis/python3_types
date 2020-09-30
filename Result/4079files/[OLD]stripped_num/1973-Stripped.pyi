# (generated with --quick)

import requests.auth
import requests.sessions
from typing import Any, Type

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
    base_url: Any
    session: requests.sessions.Session
    timeout: Any
    def __init__(self, base_url, username = ..., password = ..., http_auth = ..., timeout = ...) -> None: ...
    @staticmethod
    def _check_req_return(req) -> None: ...
    def fetch_all_items(self) -> dict: ...
    def get_item(self, name) -> Any: ...
    def get_item_raw(self, name) -> Any: ...
    def json_to_item(self, json_data) -> Any: ...
    def req_get(self, uri_path) -> Any: ...
    def req_post(self, uri_path, data = ...) -> None: ...
    def req_put(self, uri_path, data = ...) -> None: ...

class openHAB(OpenHAB):
    base_url: Any
    session: requests.sessions.Session
    timeout: None
    def __init__(self, *args, **kwargs) -> None: ...
