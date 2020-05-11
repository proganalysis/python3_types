# (generated with --quick)

import numpy
from typing import Any, Tuple

CenteredGrid: Any
G: Any
T: Any
np: module
theano: Any

class GeoPhysiscs(object):
    __doc__: str
    gravity: None
    magnetics: None
    def create_geophy(self) -> None: ...
    def set_gravity_precomputations(self) -> None: ...

class GeophysicsPreprocessing(Any):
    kernel_centers: Any
    kernel_dxyz_left: Any
    kernel_dxyz_right: Any
    tz: Any
    def __init__(self, centered_grid = ...) -> None: ...
    def set_tz_kernel(self, **kwargs) -> Any: ...

class GravityPreprocessing(object):
    __doc__: str
    ai_extent: numpy.ndarray
    ai_resolution: numpy.ndarray
    airborne_plane: Any
    b_all: Any
    eu: Any
    interp_data: Any
    model_grid: Any
    model_resolution: Any
    range_max: Any
    vox_size: Any
    def __init__(self, interp_data, ai_extent, ai_resolution, ai_z = ..., range_max = ...) -> None: ...
    @staticmethod
    def compile_eu_f() -> Any: ...
    def compute_gravity(self, n_chunck_o = ...) -> Tuple[Any, Any]: ...
    def default_range(self) -> Any: ...
    def set_airborne_plane(self, z, ai_resolution) -> Any: ...
    def set_vox_size(self) -> Any: ...

def precomputations_gravity(interp_data, n_chunck = ..., densities = ...) -> Tuple[Any, Any]: ...
def set_densities(interp_data, densities) -> None: ...
def set_geophysics_obj(interp_data, ai_extent, ai_resolution, ai_z = ..., range_max = ...) -> Any: ...
