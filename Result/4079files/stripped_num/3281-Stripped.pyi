# (generated with --quick)

from typing import Any, Dict, List, Tuple, Type, TypeVar
import werkzeug.exceptions
import werkzeug.routing
import werkzeug.wrappers

HTTPException: Type[werkzeug.exceptions.HTTPException]
Response: Type[werkzeug.wrappers.Response]
Rule: Type[werkzeug.routing.Rule]
Submount: Type[werkzeug.routing.Submount]
collections: module
inspect: module
types: module
typing: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_T3 = TypeVar('_T3')
_TRoute = TypeVar('_TRoute', bound=Route)

class Route(object):
    __doc__: str
    bp: Any
    callable_repr: str
    do_argument_checking: Any
    endpoint: Any
    hooks: Dict[Any, list]
    reverse_hooks: Any
    routes: List[Tuple[Any, Any]]
    should_invoke_hooks: Any
    def __init__(self, function, *, reverse_hooks = ..., should_invoke_hooks = ..., do_argument_checking = ..., endpoint = ...) -> None: ...
    def _callable(self) -> Any: ...
    def add_hook(self, type_, hook: _T1) -> _T1: ...
    def add_path(self: _TRoute, url, methods = ...) -> _TRoute: ...
    def after_request(self, func: _T0) -> _T0: ...
    def before_request(self, func: _T0) -> _T0: ...
    def check_route_args(self, params = ...) -> None: ...
    def get_endpoint_name(self, bp = ...) -> Any: ...
    def get_hooks(self, type_) -> list: ...
    def get_submount(self) -> werkzeug.routing.Submount: ...
    def invoke(self, ctx, args = ..., params = ...) -> coroutine: ...
    def invoke_function(self, ctx, pre_hooks, post_hooks, params) -> coroutine: ...

def wrap_response(args, response_class = ...) -> Any: ...
