# (generated with --quick)

import contextlib
import flask.app
import flask.wrappers
from typing import Any, Callable, Iterator, Optional, Type, TypeVar

CONTENT_TYPE_LATEST: Any
CollectorRegistry: Any
Counter: Any
Flask: Type[flask.app.Flask]
Histogram: Any
Response: Type[flask.wrappers.Response]
g: Any
generate_latest: Any
multiprocess: Any
os: module
request: flask.wrappers.Request
sys: module
time: module

_T = TypeVar('_T')

class DatabaseMonitoring:
    _init: bool
    _instance: Optional[DatabaseMonitoring]
    observe_transaction: Callable[..., contextlib._GeneratorContextManager]
    def __init__(*args, **kwargs) -> Any: ...
    def __new__(cls, *args, **kwargs) -> Any: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def extract_exception_name(exc_info = ...) -> str: ...
def monitor_flask(app) -> None: ...
def once(__init__) -> Callable: ...
