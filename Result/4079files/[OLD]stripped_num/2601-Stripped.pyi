# (generated with --quick)

from typing import Any, Dict

RemoteWorkerNotRunning: Any
Setting: Any
cloudpickle: Any
pickle: module
socket: module
struct: module

class RemoteCallable:
    args: tuple
    callable: Any
    kwargs: Dict[str, Any]
    def __init__(self, callable_obj, *args, **kwargs) -> None: ...

class RemoteWorkerMixin:
    def run_remote_callable(self, callable_obj, *args, **kwargs) -> Any: ...

def dumps(obj) -> Any: ...
def loads(data) -> Any: ...
