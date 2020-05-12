# (generated with --quick)

import configparser
import flask.app
import flask.wrappers
from typing import Any, Callable, Dict, List, Sequence, TextIO, Type, TypeVar
import werkzeug.exceptions

Bcrypt: Any
ConfigParser: Type[configparser.ConfigParser]
Flask: Type[flask.app.Flask]
HTTPException: Type[werkzeug.exceptions.HTTPException]
Response: Type[flask.wrappers.Response]
app: flask.app.Flask
bcrypt: Any
botnetmgmt: Callable
dbm: module
default_exceptions: Dict[int, Type[werkzeug.exceptions.HTTPException]]
g: Any
json: module
new_torrc: str
os: module
per_request_callbacks: Callable[[flask.wrappers.Response], flask.wrappers.Response]
pip_install: Callable
request: flask.wrappers.Request
reset_to_tag: Callable
restart: Callable
restart_tor: bool
reverse_meterpreter: Callable
shutil: module
socket: module
subprocess: module
time: module
torrc: TextIO
update: Callable
urllib: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

def after_this_request(func: _T0) -> _T0: ...
def authenticate() -> flask.wrappers.Response: ...
def get_eyepi_capture_service() -> str: ...
def get_version() -> None: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def json_response(f) -> Callable: ...
def jsonify(*args, **kwargs) -> Any: ...
def reconfigure_systemd() -> None: ...
def requires_auth(f) -> Callable: ...
def shutdown_server() -> None: ...
def systemctl(options) -> bool: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
