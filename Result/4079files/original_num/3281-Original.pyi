# (generated with --quick)

from typing import Any, Container, Coroutine, Dict, Iterable, List, Optional, Sequence, Tuple, Type, TypeVar
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
_T2 = TypeVar('_T2')
_TRoute = TypeVar('_TRoute', bound=Route)

class Route(object):
    __doc__: str
    bp: Any
    callable_repr: str
    do_argument_checking: bool
    endpoint: Optional[str]
    hooks: Dict[str, list]
    reverse_hooks: bool
    routes: List[Tuple[str, Sequence[str]]]
    should_invoke_hooks: bool
    def __init__(self, function, *, reverse_hooks: bool = ..., should_invoke_hooks: bool = ..., do_argument_checking: bool = ..., endpoint: Optional[str] = ...) -> None: ...
    def _callable(self) -> Any: ...
    def add_hook(self, type_: str, hook: _T0) -> _T0: ...
    def add_path(self: _TRoute, url: str, methods: Sequence[str] = ...) -> _TRoute: ...
    def after_request(self, func: _T0) -> _T0: ...
    def before_request(self, func: _T0) -> _T0: ...
    def check_route_args(self, params: Optional[dict] = ...) -> None: ...
    def get_endpoint_name(self, bp = ...) -> str: ...
    def get_hooks(self, type_: str) -> list: ...
    def get_submount(self) -> werkzeug.routing.Submount: ...
    def invoke(self, ctx, args: Iterable = ..., params: Optional[Container] = ...) -> Coroutine[Any, Any, werkzeug.wrappers.Response]: ...
    def invoke_function(self, ctx, pre_hooks: list, post_hooks: list, params) -> coroutine: ...

def wrap_response(args, response_class: werkzeug.wrappers.Response = ...) -> werkzeug.wrappers.Response: ...
