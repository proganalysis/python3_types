# (generated with --quick)

import flask.wrappers
from typing import Any, Iterable, Tuple, Union

app: Any
internal_server_error: Any
page_not_found: Any
request: flask.wrappers.Request

def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def unhandled_exception(error) -> Tuple[str, int]: ...
