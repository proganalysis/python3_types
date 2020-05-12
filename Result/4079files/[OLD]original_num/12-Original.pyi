# (generated with --quick)

from typing import Any, Coroutine, Dict, Union

error_context: Any
error_middleware: Any
pytest: Any
re: module
test_multiple_handlers: Any
web: Any

class LegalException(Exception):
    data: Dict[str, Union[bool, str]]
    status: int
    def __init__(self) -> None: ...

def api_error(request) -> coroutine: ...
def error(request) -> coroutine: ...
def legal(request) -> Coroutine[Any, Any, nothing]: ...
def no_error_context(request) -> coroutine: ...
def test_single_handler(aiohttp_client) -> Coroutine[Any, Any, None]: ...
