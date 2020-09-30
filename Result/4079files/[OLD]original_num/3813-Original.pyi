# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, Dict, List, Optional, Set, Type, Union

FRPC_CONTENT_TYPE: str
Flask: Type[flask.app.Flask]
RPC_CONTENT_TYPE: str
Response: Type[flask.wrappers.Response]
fastrpc: Any
inspect: module
logging: module
request: flask.wrappers.Request
stack: Any
typechecked: Any
uwsgi: Any
xmlrpc: module

class FastRPCHandler:
    __doc__: str
    allowed_content_types: set
    app: Optional[flask.app.Flask]
    enforce_types: bool
    methods: Dict[str, Any]
    def __init__(self, app: Optional[flask.app.Flask] = ..., register_introspection_methods: bool = ..., allowed_content_types: Optional[list] = ..., url: str = ..., enforce_types: bool = ...) -> None: ...
    def _create_response(self, method_name: str, args, accept_cts: Set[str]) -> flask.wrappers.Response: ...
    def _get_accepted_content_types(self) -> Set[str]: ...
    def _system_list_methods(self) -> List[str]: ...
    def _system_method_help(self, method_name: str) -> str: ...
    def handle(self) -> Union[tuple, flask.wrappers.Response]: ...
    def register_method(self, method_name: str, func: Callable) -> None: ...
    def stat(self) -> Dict[nothing, nothing]: ...

def _response_autostatus(response) -> None: ...
def format_exc(limit: Optional[int] = ..., chain: bool = ...) -> str: ...
