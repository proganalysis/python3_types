# (generated with --quick)

from typing import Any

Object3D: Any
Scene3D: Any
gl: Any
meshtools: Any
platform: Any
primitives: Any
scenegraph: Any
shaders: Any

class CubeDrawable(Any):
    _mesh: Any
    _shader: Any
    color: Any
    def __init__(self, object, drawables, mesh, shader, color) -> None: ...
    def draw(self, transformation_matrix, camera) -> None: ...

class PrimitivesSceneGraphExample(Any):
    _camera: Any
    _cube: Any
    _cube_drawable: CubeDrawable
    _drawables: Any
    _previous_mouse_position: Any
    _scene: Any
    def __init__(self) -> None: ...
    def draw_event(self) -> None: ...
    def mouse_move_event(self, event) -> None: ...
    def mouse_release_event(self, event) -> None: ...

def __getattr__(name) -> Any: ...
