# (generated with --quick)

import requests.auth
import requests.sessions
from typing import Any, Type

HTTPDigestAuth: Type[requests.auth.HTTPDigestAuth]
URL: str
requests: module

class Configuration(object):
    __doc__: str
    host: Any
    loop: Any
    password: Any
    port: Any
    session: requests.sessions.Session
    url: str
    username: Any
    web_proto: Any
    def __init__(self, *, loop, host, username, password, port = ..., web_proto = ..., verify_ssl = ...) -> None: ...
