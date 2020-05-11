# (generated with --quick)

from typing import Any, NoReturn, Optional, Type, TypeVar

BaseWindow: Any
Matrix33: Any
Matrix44: Any
Scene: Any
Track: Any
Vector3: Any
camera: Any
matrix44: Any
moderngl: Any
resources: Any

_TEffect = TypeVar('_TEffect', bound=Effect)

class Effect:
    __doc__: str
    _ctx: Any
    _label: str
    _name: str
    _project: Any
    _sys_camera: Any
    _window: Any
    ctx: Any
    label: str
    name: str
    runnable: bool
    sys_camera: Any
    window: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def create_normal_matrix(self, modelview) -> Any: ...
    def create_projection(self, fov: float = ..., near: float = ..., far: float = ..., aspect_ratio: Optional[float] = ...) -> Any: ...
    def create_transformation(self, rotation = ..., translation = ...) -> Any: ...
    def draw(self, time: float, frametime: float, target) -> NoReturn: ...
    def get_data(self, label: str) -> Any: ...
    def get_effect(self: _TEffect, label: str) -> _TEffect: ...
    def get_effect_class(self, effect_name: str, package_name: Optional[str] = ...) -> Type[Effect]: ...
    def get_program(self, label: str) -> Any: ...
    def get_scene(self, label: str) -> Any: ...
    def get_texture(self, label: str) -> Any: ...
    def get_track(self, name: str) -> Any: ...
    def post_load(self) -> None: ...
