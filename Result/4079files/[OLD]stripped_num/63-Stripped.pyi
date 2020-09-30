# (generated with --quick)

import flask.config
import flask.wrappers
from typing import Any, Callable, Dict, List, Type, TypeVar
import werkzeug.local
import werkzeug.wrappers

Binder: Any
Config: Type[flask.config.Config]
FlaskRestfulApi: Any
Injector: Any
Local: Type[werkzeug.local.Local]
LocalManager: Type[werkzeug.local.LocalManager]
LocalProxy: Type[werkzeug.local.LocalProxy]
Module: Any
Provider: Any
Request: Type[flask.wrappers.Request]
Response: Type[werkzeug.wrappers.Response]
Scope: Any
ScopeDecorator: Any
_ModuleT: Any
__all__: List[str]
__author__: str
__version__: str
flask: module
flask_response_unpack: Any
flask_restplus: Any
functools: module
inject: Any
request: Any
singleton: Any

T = TypeVar('T', werkzeug.local.LocalProxy, Callable)

class CachedProviderWrapper(Any):
    _cache: Dict[int, Any]
    _old_provider: Any
    def __init__(self, old_provider) -> None: ...
    def get(self, injector) -> Any: ...

class FlaskInjector:
    app: Any
    injector: Any
    def __init__(self, app, modules = ..., injector = ..., request_scope_class = ...) -> None: ...

class FlaskModule(Any):
    app: Any
    request_scope_class: Any
    def __init__(self, app, request_scope_class = ...) -> None: ...
    def configure(self, binder) -> None: ...

class RequestScope(Any):
    __doc__: str
    _local_manager: werkzeug.local.LocalManager
    _locals: werkzeug.local.Local
    def cleanup(self) -> None: ...
    def configure(self) -> None: ...
    def get(self, key, provider) -> Any: ...
    def prepare(self) -> None: ...

def instance_method_wrapper(im) -> Callable: ...
def ismethod(object: object) -> bool: ...
def process_dict(d, injector) -> None: ...
def process_list(l, injector) -> None: ...
def wrap_class_based_view(fun, injector) -> Any: ...
def wrap_flask_restful_resource(fun, flask_restful_api, injector) -> Callable: ...
def wrap_fun(fun, injector) -> Any: ...
def wrap_function(fun, injector) -> Callable: ...
