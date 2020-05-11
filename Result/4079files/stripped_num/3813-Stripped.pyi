# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Dict, List, Optional, Tuple, Type, Union

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
    app: Any
    enforce_types: Any
    methods: dict
    def __init__(self, app = ..., register_introspection_methods = ..., allowed_content_types = ..., url = ..., enforce_types = ...) -> None: ...
    def _create_response(self, method_name, args, accept_cts) -> flask.wrappers.Response: ...
    def _get_accepted_content_types(self) -> set: ...
    def _system_list_methods(self) -> List[str]: ...
    def _system_method_help(self, method_name) -> str: ...
    def handle(self) -> Union[flask.wrappers.Response, Tuple[str, int]]: ...
    def register_method(self, method_name, func) -> None: ...
    def stat(self) -> Dict[nothing, nothing]: ...

def _response_autostatus(response) -> None: ...
def format_exc(limit: Optional[int] = ..., chain: bool = ...) -> str: ...
