# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, Iterable, List, Optional, Type, Union

DATA: List[str]
Flask: Type[flask.app.Flask]
add_data: Callable
app: flask.app.Flask
base64: module
before_request: Callable[[], Any]
get_data: Callable
index: Callable
json: module
request: flask.wrappers.Request
teardown_request: Callable[[Optional[Exception]], Any]

def get_root_path(*args) -> str: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
