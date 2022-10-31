# (generated with --quick)

from typing import Any, Dict

Configurator: Any
HTTPBadRequest: Any
MARSHMALLOW_VERSION_INFO: Any
echo_use_args: Any
echo_use_args_validated: Any
echo_use_args_with_path_param: Any
echo_use_kwargs: Any
echo_use_kwargs_with_path_param: Any
fields: Any
hello_args: Dict[str, Any]
hello_many_schema: HelloSchema
hello_multiple: Dict[str, Any]
json: Any
ma: Any
parser: Any
strict_kwargs: Dict[str, bool]
use_args: Any
use_kwargs: Any

class EchoCallable(object):
    __call__: Any
    request: Any
    def __init__(self, request) -> None: ...

class HelloSchema(Any):
    name: Any

def add_route(config, route, view, route_name = ..., renderer = ...) -> None: ...
def always_error(request) -> Any: ...
def create_app() -> Any: ...
def echo(request) -> Any: ...
def echo_cookie(request) -> Any: ...
def echo_file(request) -> Dict[str, Any]: ...
def echo_headers(request) -> Any: ...
def echo_many_schema(request) -> Any: ...
def echo_matchdict(request) -> Any: ...
def echo_multi(request) -> Any: ...
def echo_nested(request) -> Any: ...
def echo_nested_many(request) -> Any: ...
def echo_query(request) -> Any: ...