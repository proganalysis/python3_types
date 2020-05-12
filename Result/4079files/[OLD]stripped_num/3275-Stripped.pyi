# (generated with --quick)

from typing import Any, Dict, List, Tuple, TypeVar

algorithms: Any
base: Any
creator: Any
futures: Any
georges: Any
h: Helpers
np: module
pyDOE: Any
random: module
toolbox: Any
tools: Any

_T0 = TypeVar('_T0')

class Helpers:
    b: Any
    bl: Any
    context: Dict[str, Any]
    cube: Any
    i: int
    kinematics: Any
    l: Any
    lower_bounds: List[int]
    manzoni_beam: Any
    manzoni_line: Any
    manzoni_variables: Any
    settings_100mm: Dict[str, float]
    upper_bounds: List[int]
    variables: List[Tuple[str, str]]
    def __init__(self) -> None: ...
    def algo(self, seed = ..., NGEN = ..., POP = ..., CXPB = ...) -> Tuple[Any, Any, Any]: ...
    def evaluate(self, vs) -> list: ...
    def initialize(self, cls) -> Any: ...
    def scale(self, cube: _T0, xmin, xmax) -> _T0: ...
