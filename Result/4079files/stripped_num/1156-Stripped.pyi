# (generated with --quick)

from typing import Any, Callable, Dict

EchoUseArgsHook: Any
MARSHMALLOW_VERSION_INFO: Any
falcon: Any
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

class AlwaysError(object):
    def on_get(self, req, resp) -> None: ...
    def on_post(self, req, resp) -> None: ...

class Echo(object):
    def on_get(self, req, resp) -> None: ...
    def on_post(self, req, resp) -> None: ...

class EchoCookie(object):
    def on_get(self, req, resp) -> None: ...

class EchoHeaders(object):
    def on_get(self, req, resp) -> None: ...

class EchoManySchema(object):
    def on_get(self, req, resp) -> None: ...
    def on_post(self, req, resp) -> None: ...

class EchoMulti(object):
    def on_get(self, req, resp) -> None: ...
    def on_post(self, req, resp) -> None: ...

class EchoNested(object):
    def on_post(self, req, resp) -> None: ...

class EchoNestedMany(object):
    def on_post(self, req, resp) -> None: ...

class EchoQuery(object):
    def on_get(self, req, resp) -> None: ...

class EchoUseArgs(object):
    on_get: Any
    on_post: Any

class EchoUseArgsValidated(object):
    on_get: Any
    on_post: Any

class EchoUseArgsWithPathParam(object):
    on_get: Any

class EchoUseKwargs(object):
    on_get: Any
    on_post: Any

class EchoUseKwargsWithPathParam(object):
    on_get: Any

class HelloSchema(Any):
    name: Any

def create_app() -> Any: ...
def use_args_hook(args, context_key = ..., **kwargs) -> Callable[[Any, Any, Any], Any]: ...
