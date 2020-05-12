from constants import *
from typing import Any, Optional

class Manager:
    def personArrived(self, vehicleID: Any, edge: Any, target: Any) -> None: ...
    def cyberCarArrived(self, vehicleID: Any, edge: Any) -> None: ...
    def cyberCarBroken(self, vehicleID: Any, edge: Any) -> None: ...
    def setNewTargets(self) -> None: ...

class Status:
    edge: Any = ...
    pos: Any = ...
    parking: bool = ...
    target: Any = ...
    targetPos: Any = ...
    slot: Any = ...
    delay: Any = ...
    def __init__(self, edge: Any, pos: Any) -> None: ...
    def __repr__(self): ...

class Setting:
    step: int = ...
    manager: Any = ...
    verbose: bool = ...
    cyber: bool = ...

setting: Any
occupancy: Any
vehicleStatus: Any
persons: Any
waiting: Any

def init(manager: Any, forTest: bool = ...) -> None: ...
def getCapacity(): ...
def getStep(): ...
def getPosition(vehicleID: Any): ...
def stopAt(vehicleID: Any, edge: Any, pos: Optional[Any] = ...) -> None: ...
def leaveStop(vehicleID: Any, newTarget: Optional[Any] = ..., delay: float = ...) -> None: ...
def _rerouteCar(vehicleID: Any) -> None: ...
def _reroutePersons(edge: Any) -> None: ...
def _checkInitialPositions(vehicleID: Any, edge: Any, pos: Any) -> None: ...
def doStep() -> None: ...
