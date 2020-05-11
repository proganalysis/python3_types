# (generated with --quick)

from typing import Any, Coroutine

HTTPError: Any
MissingArgumentError: Any
RequestHandler: Any
model: Any
util: Any

class BaseHandler(Any):
    def get_template_namespace(self) -> Any: ...

class Index(BaseHandler):
    def get(self) -> None: ...
    def post(self) -> Coroutine[Any, Any, None]: ...

class ShowCode(BaseHandler):
    def get(self, codeid) -> Coroutine[Any, Any, None]: ...
    def put(self, filename) -> Coroutine[Any, Any, None]: ...

def store_code(self, code) -> Coroutine[Any, Any, None]: ...
