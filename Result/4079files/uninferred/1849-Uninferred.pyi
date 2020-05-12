from strips import *
from typing import Any

class Locatable(Object): ...
class Dude(Locatable): ...
class Block(Locatable): ...
class Space(Object): ...

class SokobanState(State):
    at: Any = ...
    has_dude: Any = ...
    has_block: Any = ...
    def __init__(self) -> None: ...
    def move(self, dude: Dude, start: Space, end: Space) -> Any: ...
    def move_block(self, dude: Dude, block: Block, dude_start: Space, block_start: Space, block_end: Space) -> Any: ...

player: Any
a: Any
p: Any
is_left: Any
is_above: Any

def adjacent(s1: Any, s2: Any): ...
def inline(s1: Any, s2: Any, s3: Any): ...

s: Any
goal: Any
