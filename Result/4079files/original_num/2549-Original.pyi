# (generated with --quick)

import flask.app
import flask.globals
import flask.wrappers
from typing import Any, Callable, Type, TypeVar
import werkzeug.wrappers

Flask: Type[flask.app.Flask]
Game: Any
app: flask.app.Flask
current_app: flask.globals._FlaskLocalProxy
game: Any
get_cell: Callable
index: Callable
json: module
move_piece: Callable
other_handler: Callable
request: flask.wrappers.Request
some_handler: Callable

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
