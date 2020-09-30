# (generated with --quick)

from typing import Any, List, Tuple, Type
import window.base

Example: Type[window.base.Example]
FRAGMENT_SHADER: str
VERTEX_SHADER: str
np: module
struct: module

class Raymarching(window.base.Example):
    aspect_ratio: float
    gl_version: Tuple[int, int]
    u_time: Any
    vao: Any
    vaos: List[nothing]
    window_size: Tuple[int, int]
    def __init__(self, **kwargs) -> None: ...
    def render(self, time: float, frame_time: float) -> None: ...

def run_example(example_cls: window.base.Example, args = ...) -> None: ...
