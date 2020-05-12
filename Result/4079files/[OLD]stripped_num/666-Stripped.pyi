# (generated with --quick)

from typing import Any, List, SupportsFloat, Tuple

GeneSpawner: Any
InstructionSet: Any
PushEstimator: Any
PushFloat: Any
PushInterpreter: Any
PushTypeLibrary: Any
SimpleInstruction: Any
X: List[List[Point]]
est: Any
instruction_set: Any
logging: module
np: module
point_distance_insrt: Any
point_from_floats_instr: Any
spawner: Any
sys: module
type_library: Any
y: List[List[Tuple[float]]]

class Point:
    __doc__: str
    x: Any
    y: Any
    def __eq__(self, other) -> Any: ...
    def __init__(self, x, y) -> None: ...
    def __repr__(self) -> str: ...

def point_distance(p1, p2) -> Tuple[float]: ...
def point_from_floats(f1, f2) -> Tuple[Point]: ...
def pow(__x: SupportsFloat, __y: SupportsFloat) -> float: ...
def sqrt(__x: SupportsFloat) -> float: ...
def to_point(thing) -> Point: ...
