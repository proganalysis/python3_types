from typing import Any
from window import Example

class Raymarching(Example):
    gl_version: Any = ...
    window_size: Any = ...
    aspect_ratio: float = ...
    vaos: Any = ...
    vao: Any = ...
    u_time: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def render(self, time: float, frame_time: float) -> Any: ...

VERTEX_SHADER: str
FRAGMENT_SHADER: str