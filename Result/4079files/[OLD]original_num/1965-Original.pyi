# (generated with --quick)

import numpy
from typing import Any, Tuple

Velocity = Tuple[numpy.ndarray, numpy.ndarray]

Config: Any
Forcing: Any
Grid: Any
State: Any
logging: module
np: module

class Tracker:
    D: Any
    __doc__: str
    advect: Any
    diffusion: Any
    dt: Any
    dx: Any
    dy: Any
    num_particles: int
    xmax: Any
    xmin: Any
    ymax: Any
    ymin: Any
    def EF(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK2(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK2a(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK2b(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK4(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK4a(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def RK4b(self, forcing, state) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def __init__(self, config) -> None: ...
    def diffuse(self) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def move_particles(self, grid, forcing, state) -> None: ...
