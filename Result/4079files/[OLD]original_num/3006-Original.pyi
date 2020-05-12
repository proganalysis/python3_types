# (generated with --quick)

import flask.wrappers
from typing import Any, Iterable, NoReturn, Type, TypeVar, Union
import werkzeug.wrappers

Course: Any
Order: Any
School: Any
User: Any
accept: Any
apply: Any
basic: Any
request: flask.wrappers.Request
required_login: Any
sch: Any
session: Any
set_avatar: Any
show_orders: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def flash(message, category: str = ...) -> None: ...
def jsonify(*args, **kwargs) -> Any: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def url_for(endpoint, **values) -> Any: ...
