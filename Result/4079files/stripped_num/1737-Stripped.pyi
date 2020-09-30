# (generated with --quick)

import flask.wrappers
from typing import Any, NoReturn, Type, Union
import werkzeug.wrappers

datetime: Type[datetime.datetime]
request: flask.wrappers.Request
session: Any
type_police: Any

class Wishlisht:
    add: Any
    def __init__(self) -> None: ...
    def get(self) -> Any: ...

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
