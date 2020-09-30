# (generated with --quick)

import collections
import numpy
from typing import Any, Optional, Tuple, Type

deque: Type[collections.deque]
np: module

class NonStationaryLinearRegression:
    __doc__: str
    _intercept: Any
    _kern: Any
    _n_obs: int
    _obs_buffer: collections.deque
    _slope: Any
    _summed_weights: Any
    _variance: Any
    _weights: Optional[numpy.ndarray]
    _window: Any
    _x: Any
    def __init__(self, window = ...) -> None: ...
    @staticmethod
    def _generate_auxiliary_vars(lam, n) -> Tuple[numpy.ndarray, Any, Any, Any]: ...
    @staticmethod
    def _get_lambda(window) -> Any: ...
    def _update_regression(self) -> None: ...
    def add_observation(self, y) -> None: ...
    def get_intercept(self) -> Any: ...
    def get_slope(self) -> Any: ...
    def get_variance(self) -> Any: ...
