# (generated with --quick)

import collections
from typing import Any, Dict, List, Tuple, Type, Union

a: Block
defaultdict: Type[collections.defaultdict]
is_above: collections.defaultdict[Tuple[Any, Any], Any]
is_left: collections.defaultdict[Tuple[Any, Any], Any]
p: List[Space]
player: Dude
s: SokobanState

class Block(Locatable): ...

class Dude(Locatable): ...

class Locatable(Any): ...

class SokobanState(Any):
    at: Dict[Union[Block, Dude], Space]
    has_block: collections.defaultdict[Space, bool]
    has_dude: collections.defaultdict[Space, bool]
    move: Any
    move_block: Any
    def __init__(self) -> None: ...

class Space(Any): ...

def __getattr__(name) -> Any: ...
def adjacent(s1, s2) -> Any: ...
def goal(s) -> Any: ...
def inline(s1, s2, s3) -> Any: ...
