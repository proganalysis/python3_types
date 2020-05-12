# (generated with --quick)

from typing import Any, Callable, TypeVar

ClientFactory = Callable[[], Any]

Channel: Any
Context: Any
_WatchEvent: Any
_logger: Any
asyncio: module
pykube: Any
structlog: Any
threading: module

Resource = TypeVar('Resource', bound=Any)

class Kubernetes:
    __doc__: str
    client_factory: Any
    def __init__(self, client_factory = ...) -> None: ...
    def get_or_none(self, resource_type, name, namespace = ...) -> Any: ...
    def watch(self, resource_type) -> Any: ...

class SnapshotRule(Any):
    endpoint: str
    kind: str
    version: str

def _watch_resources_thread_wrapper(client_factory, resource_type, allow_missing = ..., *, loop = ...) -> asyncgenerator: ...
def get_resource_or_none(client_factory, resource_type, name, namespace = ..., *, loop = ...) -> coroutine: ...
def get_resource_or_none_sync(client_factory, resource_type, name, namespace = ...) -> Any: ...
def watch_resources(ctx, resource_type, *, delay, allow_missing = ..., loop = ...) -> asyncgenerator: ...
def watch_resources_sync(client_factory, resource_type) -> Any: ...
