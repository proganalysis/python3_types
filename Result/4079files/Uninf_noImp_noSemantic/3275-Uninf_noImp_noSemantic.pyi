from deap import algorithms as algorithms
from typing import Any, Optional

class Helpers:
    i: int = ...
    bl: Any = ...
    kinematics: Any = ...
    b: Any = ...
    settings_100mm: Any = ...
    lower_bounds: Any = ...
    upper_bounds: Any = ...
    variables: Any = ...
    context: Any = ...
    manzoni_line: Any = ...
    l: Any = ...
    manzoni_variables: Any = ...
    manzoni_beam: Any = ...
    cube: Any = ...
    def __init__(self) -> None: ...
    def scale(self, cube: Any, xmin: Any, xmax: Any): ...
    def initialize(self, cls: Any): ...
    def evaluate(self, vs: Any): ...
    def algo(self, seed: Optional[Any] = ..., NGEN: int = ..., POP: int = ..., CXPB: float = ...): ...

h: Any
toolbox: Any
