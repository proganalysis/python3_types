# (generated with --quick)

import flask.wrappers
from typing import Any, Iterable, Type, TypeVar, Union
import werkzeug.wrappers

app: Any
cache: Any
copy: module
hex2id: Any
init: Any
re: module
request: flask.wrappers.Request
robots: Any
search: Any
search_bad_method: Any
show_block: Any
show_block_old: Any
show_code: Any
show_code_old: Any
sitemap: Any
welcome: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def url_for(endpoint, **values) -> Any: ...
