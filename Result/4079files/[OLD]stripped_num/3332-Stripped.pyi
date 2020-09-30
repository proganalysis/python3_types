# (generated with --quick)

from typing import Any, Coroutine, NoReturn

MYPY: bool
asyncio: module

class BallDeviceEjector:
    __slots__ = ["ball_device", "config", "machine"]
    __doc__: str
    ball_device: Any
    config: Any
    machine: Any
    def __init__(self, config, ball_device, machine) -> None: ...
    def ball_search(self, phase, iteration) -> NoReturn: ...
    def eject_one_ball(self, is_jammed, eject_try) -> Coroutine[Any, Any, nothing]: ...
    def reorder_balls(self) -> Coroutine[Any, Any, nothing]: ...
