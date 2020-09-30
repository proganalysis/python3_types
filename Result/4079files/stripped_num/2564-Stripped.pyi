# (generated with --quick)

from typing import Any, Callable, Union

random: module
time: module

class ExponentialBackoff:
    __doc__: str
    _base: Any
    _exp: int
    _last_invocation: float
    _max: int
    _randfunc: Callable[..., Union[float, int]]
    _reset_time: Any
    def __init__(self, base = ..., *, integral = ...) -> None: ...
    def delay(self) -> Union[float, int]: ...
