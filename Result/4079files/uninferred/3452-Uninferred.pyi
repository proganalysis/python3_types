from typing import Any

class BinaryActionLinearPolicy:
    w: Any = ...
    b: Any = ...
    def __init__(self, theta: Any) -> None: ...
    def act(self, ob: Any): ...

class ContinuousActionLinearPolicy:
    W: Any = ...
    b: Any = ...
    def __init__(self, theta: Any, n_in: Any, n_out: Any) -> None: ...
    def act(self, ob: Any): ...
