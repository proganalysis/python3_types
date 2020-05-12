# (generated with --quick)

import queue
from typing import Any, Callable, Type, TypeVar

BasePlugin: Any
Queue: Type[queue.Queue]

_FuncT = TypeVar('_FuncT', bound=Callable)

class ProviderPlugin(Any):
    @abstractmethod
    def ingest(self, queue: queue.Queue) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
