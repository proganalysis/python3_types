# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, Dict, List, Type, TypeVar, Union

Flask: Type[flask.app.Flask]
app: flask.app.Flask
internal_error: Callable
json: module
jwt: module
login: Callable
logins: Dict[str, str]
not_found: Callable
packages: Callable
request: flask.wrappers.Request
requests: Callable
signature: Callable
time: module
traceback: module

_T0 = TypeVar('_T0')

def jsonify(*args, **kwargs) -> Any: ...
def main() -> None: ...
def make_response(*args) -> Any: ...
def payload(username: _T0) -> Dict[str, Union[float, str, Dict[str, _T0], List[str]]]: ...
def token(data) -> str: ...
