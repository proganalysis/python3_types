# (generated with --quick)

import numpy
from typing import Any, Callable, Generator, Tuple, Type

BOTTOM_CONST: float
BOTTOM_SCALAR: Any
L_MAX: float
L_MIN: float
M1: Any
M2: Any
M3: Any
M_CONSTS: numpy.ndarray
TOP1_SCALAR: Any
TOP2_L_SCALAR: float
TOP2_SCALAR: Any
_2pi: Any
_to_linear: Callable
constants: Any
ndarray: Type[numpy.ndarray]
ne: Any
np: module
transform: module

def _bounds(l_nd) -> Generator[Tuple[Any, Any], Any, None]: ...
def _dot_product(scalars, rgb_nd) -> numpy.ndarray: ...
def _lch_to_husl(lch_nd) -> Any: ...
def _luv_to_lch(luv_nd) -> Any: ...
def _max_lh_chroma(lch) -> numpy.ndarray: ...
def _ray_length(theta, line) -> Any: ...
def _to_light(y_nd) -> Any: ...
def _xyz_to_luv(xyz_nd) -> Any: ...
