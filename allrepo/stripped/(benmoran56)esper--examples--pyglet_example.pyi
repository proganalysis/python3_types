# (generated with --quick)

from typing import Any, Tuple

FPS: int
RESOLUTION: Tuple[int, int]
batch: Any
enemy: Any
enemy_image: Any
esper: Any
movement_processor: MovementProcessor
on_draw: Any
on_key_press: Any
on_key_release: Any
player: Any
player_image: Any
pyglet: Any
window: Any
world: Any

class MovementProcessor(Any):
    maxx: Any
    maxy: Any
    minx: Any
    miny: Any
    def __init__(self, minx, maxx, miny, maxy) -> None: ...
    def process(self, dt) -> None: ...

class Renderable:
    h: Any
    sprite: Any
    w: Any
    def __init__(self, sprite) -> None: ...

class Velocity:
    x: Any
    y: Any
    def __init__(self, x = ..., y = ...) -> None: ...
