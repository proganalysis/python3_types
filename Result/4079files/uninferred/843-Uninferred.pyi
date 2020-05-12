from pyspades.constants import *
from collections import namedtuple
from typing import Any

DIRT_COLOR: Any

StrongBlock = namedtuple('StrongBlock', 'color owner')

def rebuild_block(player: Any, x: Any, y: Any, z: Any, color: Any) -> None: ...
def check_if_buried(protocol: Any, x: Any, y: Any, z: Any) -> None: ...
def bury_adjacent(protocol: Any, x: Any, y: Any, z: Any) -> None: ...
def is_color_dirt(color: Any): ...
def apply_script(protocol: Any, connection: Any, config: Any): ...
