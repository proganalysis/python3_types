# (generated with --quick)

from typing import Any, Optional

Estimator: Any
cat: Any
differential_evolution: Any
irt: Any
numpy: module

class DifferentialEvolutionEstimator(Any):
    __doc__: str
    _calls: int
    _evaluations: Any
    _lower_bound: Any
    _upper_bound: Any
    avg_evaluations: Any
    calls: Any
    evaluations: Any
    def __init__(self, bounds: tuple) -> None: ...
    def __str__(self) -> str: ...
    def estimate(self, index: Optional[int] = ..., items: Optional[numpy.ndarray] = ..., administered_items: Optional[list] = ..., response_vector: Optional[list] = ..., **kwargs) -> float: ...

class HillClimbingEstimator(Any):
    __doc__: str
    _calls: int
    _dodd: bool
    _evaluations: int
    _precision: int
    _verbose: bool
    avg_evaluations: float
    calls: float
    dodd: bool
    evaluations: float
    def __init__(self, precision: int = ..., dodd: bool = ..., verbose: bool = ...) -> None: ...
    def __str__(self) -> str: ...
    def _getout(self, theta: float) -> float: ...
    def estimate(self, index: Optional[int] = ..., items: Optional[numpy.ndarray] = ..., administered_items: Optional[list] = ..., response_vector: Optional[list] = ..., est_theta: Optional[float] = ..., **kwargs) -> float: ...
