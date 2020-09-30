# (generated with --quick)

import __future__
import optparse
from typing import Any, Dict, NoReturn, Type

BREAK_DELAY: int
BUS_CAPACITY: int
CAR_CAPACITY: int
CYBER_CAPACITY: int
CYBER_LENGTH: int
CYBER_SPEED: int
DOUBLE_ROWS: int
INFINITY: float
NETCONVERT: Any
OCCUPATION_PROBABILITY: float
OptionParser: Type[optparse.OptionParser]
PORT: int
PREFIX: str
ROW_DIST: int
SLOTS_PER_ROW: int
SLOT_FOOT_LENGTH: int
SLOT_LENGTH: int
SLOT_WIDTH: int
STOP_POS: int
SUMO: Any
SUMOGUI: Any
SUMO_HOME: str
TOTAL_CAPACITY: int
WAIT_PER_PERSON: int
absolute_import: __future__._Feature
checkBinary: Any
occupancy: dict
os: module
persons: Dict[Any, list]
print_function: __future__._Feature
random: module
setting: Setting
statistics: module
subprocess: module
sys: module
tc: Any
traci: Any
vehicleStatus: Dict[Any, Status]
waiting: Dict[nothing, nothing]

class Manager:
    def cyberCarArrived(self, vehicleID, edge) -> NoReturn: ...
    def cyberCarBroken(self, vehicleID, edge) -> None: ...
    def personArrived(self, vehicleID, edge, target) -> NoReturn: ...
    def setNewTargets(self) -> None: ...

class Setting:
    breakstep: Any
    cyber: Any
    manager: Any
    step: int
    verbose: Any

class Status:
    delay: Any
    edge: Any
    parking: bool
    pos: Any
    slot: Any
    target: Any
    targetPos: Any
    def __init__(self, edge, pos) -> None: ...
    def __repr__(self) -> str: ...

def _checkInitialPositions(vehicleID, edge, pos) -> None: ...
def _rerouteCar(vehicleID) -> None: ...
def _reroutePersons(edge) -> None: ...
def doStep() -> None: ...
def getCapacity() -> int: ...
def getPosition(vehicleID) -> Any: ...
def getStep() -> int: ...
def init(manager, forTest = ...) -> None: ...
def leaveStop(vehicleID, newTarget = ..., delay = ...) -> None: ...
def stopAt(vehicleID, edge, pos = ...) -> None: ...
