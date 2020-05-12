# (generated with --quick)

from typing import Any, Dict, Union

Body: Any

class BodyState(object):
    bodies: Any
    delta_time: float
    ticks: int
    time: float
    def __init__(self, bodies, ticks, time, delta_time) -> None: ...
    @staticmethod
    def from_dict(dictionary) -> BodyState: ...
    def to_dict(self) -> Dict[str, Union[float, int, list]]: ...
