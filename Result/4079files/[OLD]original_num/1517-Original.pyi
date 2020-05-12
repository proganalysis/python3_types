# (generated with --quick)

import requests.models
import requests.sessions
from typing import Dict, Optional, Union

re: module
requests: module

class Retrieve:
    USER_AGENT: str
    __doc__: str
    proxy: Optional[dict]
    session: requests.sessions.Session
    def __init__(self, proxy: dict) -> None: ...
    def get(self, url, end_cursor = ...) -> Union[bool, requests.models.Response]: ...
    def new_proxy(self) -> Dict[str, str]: ...

def correct_proxy_format(proxy) -> Optional[bool]: ...
