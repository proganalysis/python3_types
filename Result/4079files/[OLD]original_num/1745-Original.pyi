# (generated with --quick)

import collections
import numpy
from typing import Any, Optional, Tuple, Type

deque: Type[collections.deque]
np: module

class NonStationaryLinearRegression:
    __doc__: str
    _intercept: Any
    _kern: Optional[numpy.ndarray]
    _n_obs: int
    _obs_buffer: collections.deque[float]
    _slope: Any
    _summed_weights: Optional[float]
    _variance: Any
    _weights: Optional[numpy.ndarray]
    _window: int
    _x: Optional[numpy.ndarray]
    def __init__(self, window: int = ...) -> None: ...
    @staticmethod
    def _generate_auxiliary_vars(lam: float, n: int) -> Tuple[numpy.ndarray, float, numpy.ndarray, numpy.ndarray]: ...
    @staticmethod
    def _get_lambda(window: int) -> float: ...
    def _update_regression(self) -> None: ...
    def add_observation(self, y: float) -> None: ...
    def get_intercept(self) -> Optional[float]: ...
    def get_slope(self) -> Optional[float]: ...
    def get_variance(self) -> Optional[float]: ...
