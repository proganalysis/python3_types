# (generated with --quick)

import flask.wrappers
from typing import Any, Callable, Iterable, Optional, Type, Union
import uchan.flask
import uchan.lib.exceptions

ArgumentError: Type[uchan.lib.exceptions.ArgumentError]
BadRequestError: Type[uchan.lib.exceptions.BadRequestError]
app: Optional[uchan.flask.CustomFlaskApp]
check_csrf_referer: Any
request: flask.wrappers.Request
verification_service: module
verify: Callable

def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
