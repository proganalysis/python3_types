# (generated with --quick)

import requests.sessions
from typing import Any, Dict

random: module
requests: module
time: module

class Session(object):
    URL: Any
    __doc__: str
    accept_language: str
    csrftoken: Any
    logging: Any
    login_post: Dict[str, Any]
    login_status: bool
    session: requests.sessions.Session
    user_agent: str
    user_login: Any
    user_password: Any
    def __del__(self) -> None: ...
    def __init__(self, username, password, logging = ...) -> None: ...
    def log(self, text) -> None: ...
    def login(self) -> None: ...
    def logout(self) -> None: ...
    def post(self, url) -> int: ...
