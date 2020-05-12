from . import zsocket as zsocket
from typing import Any

logger: Any

class ZActor:
    ZACTOR_TAG: int = ...
    tag: Any = ...
    ctx: Any = ...
    shim_handler: Any = ...
    shim_args: Any = ...
    shim_kwargs: Any = ...
    is_running: bool = ...
    thread: Any = ...
    def __init__(self, ctx: Any, actor: Any, *args: Any, **kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def destroy(self) -> None: ...
    def send(self, *args: Any, **kwargs: Any): ...
    def send_unicode(self, *args: Any, **kwargs: Any): ...
    def send_multipart(self, *args: Any, **kwargs: Any): ...
    def send_pyobj(self, *args: Any, **kwargs: Any): ...
    def recv(self, *args: Any, **kwargs: Any): ...
    def recv_unicode(self, *args: Any, **kwargs: Any): ...
    def recv_multipart(self, *args: Any, **kwargs: Any): ...
    def recv_pyobj(self, *args: Any, **kwargs: Any): ...
    def is_zactor(self): ...
    def resolve(self): ...

def echo_actor(ctx: Any, pipe: Any, *args: Any) -> None: ...
def zactor_test(verbose: bool = ...) -> None: ...
