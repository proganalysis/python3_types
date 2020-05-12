from approxeng.input import Controller
from typing import Any

__all__: Any

class PiHut(Controller):
    def __init__(self, dead_zone: float = ..., hot_zone: float = ...) -> None: ...
    @staticmethod
    def registration_ids(): ...
    def __repr__(self): ...
