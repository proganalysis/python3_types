# (generated with --quick)

from typing import Any, Callable

logging: module

class ClientError(Error):
    code: Any
    http_code: Any
    level: Any
    message: Any

class Error(Exception):
    code: Any
    http_code: Any
    level: Any
    message: Any
    def __init__(self, message = ..., *, code = ..., level = ..., http_code = ...) -> None: ...
    def to_dict(self) -> dict: ...

class ServerError(Error):
    code: Any
    http_code: Any
    level: Any
    message: Any

def handle_error(error, exception = ...) -> Callable[[Any], Any]: ...
