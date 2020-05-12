# (generated with --quick)

from typing import Any, AsyncGenerator, Callable, Iterable, Optional, Type, TypeVar

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
    def __init__(self, client_factory: Optional[Callable[[], Any]] = ...) -> None: ...
    def get_or_none(self, resource_type: Type[Resource], name: str, namespace: Optional[str] = ...) -> Optional[Resource]: ...
    def watch(self, resource_type: Type[Resource]) -> Iterable: ...

class SnapshotRule(Any):
    endpoint: str
    kind: str
    version: str

def _watch_resources_thread_wrapper(client_factory: Callable[[], Any], resource_type: Type[Resource], allow_missing: bool = ..., *, loop = ...) -> AsyncGenerator[Any, None]: ...
def get_resource_or_none(client_factory: Callable[[], Any], resource_type: Type[Resource], name: str, namespace: Optional[str] = ..., *, loop = ...) -> coroutine: ...
def get_resource_or_none_sync(client_factory: Callable[[], Any], resource_type: Type[Resource], name: str, namespace: Optional[str] = ...) -> Optional[Resource]: ...
def watch_resources(ctx, resource_type: Resource, *, delay: int, allow_missing: bool = ..., loop = ...) -> AsyncGenerator[Any, None]: ...
def watch_resources_sync(client_factory: Callable[[], Any], resource_type) -> Iterable: ...
