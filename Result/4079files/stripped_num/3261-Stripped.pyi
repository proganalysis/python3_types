# (generated with --quick)

from typing import Any, Dict, Optional

LOG: logging.Logger
compute_node_data: Any
compute_vtk_polydata: Any
logging: module
np: module
pi: Any
vtk: Any

class Animation:
    __doc__: str
    _current_frame: int
    _precomputed_polydatas: Dict[Any, Optional[list]]
    actors: list
    fps: Any
    frames_per_loop: int
    def __init__(self, loop_duration, fps = ...) -> None: ...
    def _add_actor(self, mesh, faces_motion = ..., faces_colors = ..., edges = ...) -> Any: ...
    def _callback(self, renderer, event) -> None: ...
    def add_body(self, body, faces_motion = ..., faces_colors = ..., edges = ...) -> Any: ...
    def add_free_surface(self, free_surface, faces_elevation) -> Any: ...
    def run(self, camera_position = ..., resolution = ...) -> None: ...
    def save(self, filepath, nb_loops = ..., camera_position = ..., resolution = ...) -> None: ...
