# (generated with --quick)

import flask.wrappers
from typing import Any, Callable

flask: module
functools: module
settings: Any

def check_credentials(username, pw) -> Any: ...
def not_authorized() -> flask.wrappers.Response: ...
def requires_auth(func) -> Callable: ...
