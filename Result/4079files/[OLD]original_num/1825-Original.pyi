# (generated with --quick)

from typing import Any, Dict, Set, Tuple, Type, Union

bl_info: Dict[str, Union[str, Tuple[int, int, int]]]
bpy: Any
classes: Tuple[Type[SpriteRenderOperator], Type[SpriteRenderPanel], Type[SpriteRenderSettings]]
math: module
signal: module
sys: module
time: module

class SpriteRenderOperator(Any):
    abort: bool
    bl_idname: str
    bl_label: str
    bl_options: Set[str]
    def execute(self, context) -> Set[str]: ...
    def render(self, scene, obj_name, filepath, steps, framenames, anglenames, startframe = ..., endframe = ...) -> None: ...

class SpriteRenderPanel(Any):
    bl_context: str
    bl_idname: str
    bl_label: str
    bl_region_type: str
    bl_space_type: str
    def draw(self, context) -> None: ...

class SpriteRenderSettings(Any):
    anglenames: Any
    framenames: Any
    path: Any
    steps: Any
    target: Any

def __getattr__(name) -> Any: ...
def register() -> None: ...
def unregister() -> None: ...
