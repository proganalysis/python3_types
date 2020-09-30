# (generated with --quick)

from typing import Any, Tuple

BGCOLOR: Tuple[int, int, int, int]
FPS: int
RESOLUTION: Tuple[int, int]
esper: Any
key: Any
pyglet: Any
sys: module
texture_enable_group: TextureEnableGroup

class MovementProcessor(Any):
    maxx: Any
    maxy: Any
    minx: Any
    miny: Any
    def __init__(self, minx, miny, maxx, maxy) -> None: ...
    def process(self) -> None: ...

class Renderable:
    _dirty: bool
    _x: Any
    _y: Any
    group: TextureBindGroup
    h: Any
    texture: Any
    vertex_list: None
    w: Any
    x: Any
    y: Any
    def __init__(self, texture, width, height, posx, posy) -> None: ...

class TextureBindGroup(Any):
    blend_dest: Any
    blend_src: Any
    texture: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, texture) -> None: ...
    def set_state(self) -> None: ...
    def unset_state(self) -> None: ...

class TextureEnableGroup(Any):
    def set_state(self) -> None: ...
    def unset_state(self) -> None: ...

class TextureRenderProcessor(Any):
    batch: Any
    def __init__(self, batch) -> None: ...
    def draw_texture(self, renderable) -> None: ...
    def process(self) -> None: ...

class Velocity:
    x: Any
    y: Any
    def __init__(self, x = ..., y = ...) -> None: ...

def __getattr__(name) -> Any: ...
def run(args = ...) -> None: ...
def texture_from_image(image_name) -> Any: ...
