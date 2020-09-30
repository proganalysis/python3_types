# (generated with --quick)

import flask.app
import flask_multisession
from typing import Any, Callable, Type, TypeVar
import werkzeug.wrappers

Flask: Type[flask.app.Flask]
MongoSessionInterface: Type[flask_multisession.MongoSessionInterface]
app: flask.app.Flask
index: Callable
login: Callable
logout: Callable
logout_all_devices: Callable
random: module
session: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def url_for(endpoint, **values) -> Any: ...
