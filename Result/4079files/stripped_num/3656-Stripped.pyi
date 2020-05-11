# (generated with --quick)

from typing import Any

SlidingWindowFeature: Any
np: module
pd: Any

class GlobalStandardization(object):
    __doc__: str
    def __call__(self, features, sliding_window = ...) -> Any: ...
    def get_context_duration(self) -> float: ...

class ShortTermStandardization(object):
    __doc__: str
    duration: Any
    def __call__(self, features, sliding_window = ...) -> Any: ...
    def __init__(self, duration = ...) -> None: ...
    def get_context_duration(self) -> Any: ...
