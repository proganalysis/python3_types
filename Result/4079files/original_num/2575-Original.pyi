# (generated with --quick)

from typing import Any

Body: Any

class BodyState(object):
    bodies: Any
    delta_time: float
    ticks: int
    time: float
    def __init__(self, bodies, ticks: int, time: float, delta_time: float) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict) -> BodyState: ...
    def to_dict(self) -> dict: ...
