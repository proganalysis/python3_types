# (generated with --quick)

from typing import Any, TypeVar

Joints: Any
ReturnCommandError: Any
Sensors: Any
SimulationState: Any
v: Any

_TVRepApi = TypeVar('_TVRepApi', bound=VRepApi)

class VRepApi:
    _def_op_mode: Any
    _id: Any
    joint: Any
    sensor: Any
    simulation: Any
    def __enter__(self: _TVRepApi) -> _TVRepApi: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, id) -> None: ...
    def close_connection(self) -> None: ...
    @staticmethod
    def connect(ip, port) -> VRepApi: ...
