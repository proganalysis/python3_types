# (generated with --quick)

from typing import Any, TypeVar

Estimator: Any
cat: Any
differential_evolution: Any
irt: Any
numpy: module

_T0 = TypeVar('_T0')

class DifferentialEvolutionEstimator(Any):
    __doc__: str
    _calls: int
    _evaluations: Any
    _lower_bound: Any
    _upper_bound: Any
    avg_evaluations: Any
    calls: Any
    evaluations: Any
    def __init__(self, bounds) -> None: ...
    def __str__(self) -> str: ...
    def estimate(self, index = ..., items = ..., administered_items = ..., response_vector = ..., **kwargs) -> Any: ...

class HillClimbingEstimator(Any):
    __doc__: str
    _calls: int
    _dodd: Any
    _evaluations: int
    _precision: Any
    _verbose: Any
    avg_evaluations: Any
    calls: Any
    dodd: Any
    evaluations: Any
    def __init__(self, precision = ..., dodd = ..., verbose = ...) -> None: ...
    def __str__(self) -> str: ...
    def _getout(self, theta: _T0) -> _T0: ...
    def estimate(self, index = ..., items = ..., administered_items = ..., response_vector = ..., est_theta = ..., **kwargs) -> Any: ...
