from collections import namedtuple
from typing import Any

Position = namedtuple('Position', ['x', 'y'])

TileSet = namedtuple('TileSet', ['image', 'positions'])
LEFT: Any
RIGHT: Any
UP: Any
DOWN: Any

def get_tile_rect(position: Any): ...

maze: Any
player: Any
ghost: Any

def draw_sprite(sprite: Any, img: Any, tiles: Any) -> None: ...
def draw(maze: Any, sprites: Any, display: Any, tiles: Any) -> None: ...
def wait_for_key(event: Any) -> None: ...
