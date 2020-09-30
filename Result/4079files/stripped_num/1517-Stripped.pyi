# (generated with --quick)

import requests.models
import requests.sessions
from typing import Any, Dict, Optional, Union

re: module
requests: module

class Retrieve:
    USER_AGENT: str
    __doc__: str
    proxy: Any
    session: requests.sessions.Session
    def __init__(self, proxy) -> None: ...
    def get(self, url, end_cursor = ...) -> Union[bool, requests.models.Response]: ...
    def new_proxy(self) -> Dict[str, str]: ...

def correct_proxy_format(proxy) -> Optional[bool]: ...
