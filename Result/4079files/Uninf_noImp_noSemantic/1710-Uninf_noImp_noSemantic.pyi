from typing import Any

class PatchedStream:
    stream: Any = ...
    patches: Any = ...
    _pos: Any = ...
    def __init__(self, stream: Any, patches: Any) -> None: ...
    def read(self, *args: Any, **kwargs: Any): ...
    def seek(self, *args: Any, **kwargs: Any) -> None: ...
    def tell(self): ...
    def close(self): ...
