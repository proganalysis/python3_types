# (generated with --quick)

import flask.wrappers
from typing import Any, Iterable, NoReturn, Type, TypeVar, Union
import werkzeug.wrappers

Course: Any
Message: Any
Order: Any
Paper: Any
School: Any
User: Any
basic: Any
bind_gmail: Any
bind_parent: Any
get_message: Any
info_page: Any
like: Any
message: Any
new_message: Any
per: Any
request: flask.wrappers.Request
required_login: Any
session: Any
set_avatar: Any
show_child: Any
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
