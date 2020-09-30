# (generated with --quick)

import flask.app
import flask.wrappers
import threading
from typing import Any, Callable, Optional, Sequence, Type, TypeVar
import werkzeug.routing

BaseConverter: Type[werkzeug.routing.BaseConverter]
Flask: Type[flask.app.Flask]
JWT_SECRET: str
PASSWORD: str
PROJECTS: Any
SECRET: bytes
Timer: Type[threading.Timer]
ValidationError: Type[werkzeug.routing.ValidationError]
app: flask.app.Flask
channel: flask_sse.Channel
compile: module
datetime: module
flask_sse: module
get_build_details: Callable
get_build_log: Callable
get_build_pdf: Callable
get_build_svg: Callable
get_build_zip: Callable
get_builds: Callable
get_diff: Callable
get_latest_svg: Callable
git: module
github_build: Callable
hashlib: module
hmac: module
json: module
jwt: module
list_projects: Callable
login: Callable
os: module
p: Any
request: flask.wrappers.Request
start_build: Callable
subscribe: Callable
useNginx: Optional[str]

_T0 = TypeVar('_T0')

class StringConverter(werkzeug.routing.BaseConverter):
    exc: list
    def __init__(self, url_map, exc = ...) -> None: ...
    def to_python(self, value: _T0) -> _T0: ...
    def to_url(self, value) -> str: ...

def SSEPing() -> None: ...
def check_auth(func) -> Callable: ...
def error_handler(func) -> Callable: ...
def getBuildPath(proj, ref = ...) -> str: ...
def getConfig(proj, ref = ...) -> Any: ...
def getProjPath(proj) -> str: ...
def make_response(*args) -> Any: ...
def mySendFile(path, mimetype, content_disposition = ...) -> Any: ...
def nocache(view) -> Callable: ...
def parseRef(proj, ref) -> Any: ...
def send_file(filename_or_fp, mimetype = ..., as_attachment: bool = ..., attachment_filename = ..., add_etags: bool = ..., cache_timeout = ..., conditional: bool = ..., last_modified = ...) -> Any: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
