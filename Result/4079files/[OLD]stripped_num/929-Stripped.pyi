# (generated with --quick)

import abc
from typing import Any, Callable, Dict, List, Tuple, Type, TypeVar

ABC: Type[abc.ABC]
ABCMeta: Type[abc.ABCMeta]
DIST_LIM: float
ORIGINAL_ROTATION_VEC: Tuple[float, float, float]
ROTATION_VEC: Tuple[float, float, float]
SCALE_FACTOR: float
TARGET_SPEED: float
Vector: Any
bpy: Any
np: module
sys: module

_FuncT = TypeVar('_FuncT', bound=Callable)
_T1 = TypeVar('_T1')

class Cube(Object):
    edges: List[nothing]
    faces: List[Tuple[int, int, int, int]]
    loc: Any
    mesh_data: Any
    name: str
    obj: Any
    radius: Any
    sierpinski_scale: float
    verts: List[Tuple[Any, Any, Any]]
    def __init__(self, radius, location) -> None: ...
    @classmethod
    def replicate_shrink_step(cls, cube, max_depth) -> List[Dict[str, Any]]: ...

class Object(abc.ABC):
    edges: List[nothing]
    faces: List[nothing]
    loc: Any
    mesh_data: Any
    name: Any
    obj: Any
    radius: Any
    sierpinski_scale: None
    verts: List[nothing]
    def __init__(self, radius, location, name) -> None: ...
    def _init_mesh(self) -> None: ...
    def _init_obj(self, link = ...) -> None: ...
    @classmethod
    def obj_replication(cls, obj: _T1, max_depth) -> list: ...
    @classmethod
    @abstractmethod
    def replicate_shrink_step(cls, obj, max_depth) -> Any: ...
    @staticmethod
    def rotate_objects(object, grid_val, rotation_vec = ..., original_rot_vec = ...) -> None: ...
    @staticmethod
    def scale_objects(object, grid_val, scale_factor = ...) -> None: ...

class Pyramid(Object):
    edges: List[nothing]
    faces: List[Tuple[int, ...]]
    loc: Any
    mesh_data: Any
    name: str
    obj: Any
    radius: Any
    sierpinski_scale: float
    verts: List[Tuple[Any, Any, Any]]
    def __init__(self, radius, location) -> None: ...
    @classmethod
    def replicate_shrink_step(cls, pyramid, depth) -> List[Dict[str, Any]]: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def frame_handler(scene, objs, target, num_frames_change) -> None: ...
def main(_) -> None: ...
def move_target(target) -> None: ...
def update_grid(objs, target) -> None: ...
