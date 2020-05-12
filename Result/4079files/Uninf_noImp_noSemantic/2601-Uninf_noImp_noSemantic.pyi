from typing import Any

def dumps(obj: Any): ...
def loads(data: Any): ...

class RemoteCallable:
    callable: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def __init__(self, callable_obj: Any, *args: Any, **kwargs: Any) -> None: ...

class RemoteWorkerMixin:
    def run_remote_callable(self, callable_obj: Any, *args: Any, **kwargs: Any): ...
