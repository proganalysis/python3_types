# (generated with --quick)

from typing import Any, Tuple

FPS: int
RESOLUTION: Tuple[int, int]
esper: Any
pygame: Any

class MovementProcessor(Any):
    maxx: Any
    maxy: Any
    minx: Any
    miny: Any
    def __init__(self, minx, maxx, miny, maxy) -> None: ...
    def process(self) -> None: ...

class RenderProcessor(Any):
    clear_color: Any
    window: Any
    def __init__(self, window, clear_color = ...) -> None: ...
    def process(self) -> None: ...

class Renderable:
    depth: Any
    h: Any
    image: Any
    w: Any
    x: Any
    y: Any
    def __init__(self, image, posx, posy, depth = ...) -> None: ...

class Velocity:
    x: Any
    y: Any
    def __init__(self, x = ..., y = ...) -> None: ...

def run() -> Any: ...
