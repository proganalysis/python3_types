# (generated with --quick)

from typing import Any

class BinaryActionLinearPolicy(object):
    b: Any
    w: Any
    def __init__(self, theta) -> None: ...
    def act(self, ob) -> int: ...

class ContinuousActionLinearPolicy(object):
    W: Any
    b: Any
    def __init__(self, theta, n_in, n_out) -> None: ...
    def act(self, ob) -> Any: ...
