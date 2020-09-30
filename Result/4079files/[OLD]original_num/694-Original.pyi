# (generated with --quick)

import flask.wrappers
from typing import Any, Iterable, NoReturn, Type, TypeVar, Union
import werkzeug.wrappers

Response: Type[flask.wrappers.Response]
__author__: str
add_header: Any
app: Any
datetime: Type[datetime.datetime]
ico: Any
index: Any
metadata: Any
proxyradio: Any
request: flask.wrappers.Request
session: Any
shoutcast: Any
static: Any
stream_factory: Any
streams: Any
wishlist: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def jsonify(*args, **kwargs) -> Any: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def send_from_directory(directory, filename, **options) -> Any: ...
