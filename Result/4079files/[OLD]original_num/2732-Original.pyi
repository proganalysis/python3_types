# (generated with --quick)

import flask.wrappers
from typing import Any, Type, TypeVar, Union
import werkzeug.wrappers

app: Any
bad_request: Any
body: Any
cache: Any
config: Any
errors: Any
healthcheck: Any
index: Any
logic: Any
metadata: Any
on_exception: Any
request: flask.wrappers.Request
search: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

def jsonify(*args, **kwargs) -> Any: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
