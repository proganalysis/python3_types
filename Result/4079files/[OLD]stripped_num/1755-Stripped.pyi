# (generated with --quick)

import requests.cookies
from typing import Any, Optional

json: module
requests: module

class TaralloSession:
    cookie: Optional[requests.cookies.RequestsCookieJar]
    last_status: Optional[int]
    url: Any
    def __init__(self, url) -> None: ...
    def get_history(self, item, limit) -> Any: ...
    def login(self, username, password) -> bool: ...
