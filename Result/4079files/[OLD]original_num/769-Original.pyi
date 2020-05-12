# (generated with --quick)

import flask.app
import flask.globals
import flask.sessions
from typing import Any, Type

Flask: Type[flask.app.Flask]
SecureCookieSession: Type[flask.sessions.SecureCookieSession]
SecureCookieSessionInterface: Type[flask.sessions.SecureCookieSessionInterface]
auth_bp: Any
cos_bp: Any
current_app: flask.globals._FlaskLocalProxy
main_bp: Any
pay_bp: Any
per_bp: Any
sch_bp: Any
struct: module

class SignedSession(flask.sessions.SecureCookieSession):
    skey: Any
    skey_int: Any
    def __getitem__(self, key) -> str: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> Any: ...
    def decrypt(self, encrypted) -> str: ...
    def encrypt(self, data) -> str: ...
    def parse_key(self) -> Any: ...

def create_app() -> flask.app.Flask: ...
