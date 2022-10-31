from .tlib import *
from typing import Any, Optional

is_exe: Any

class Tiles:
    path: Any = ...
    w: Any = ...
    pos: Any = ...
    endpos: Any = ...
    h: Any = ...
    def __init__(self, path: Any, pos: Any, w: Any, h: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...

class Chests:
    path: Any = ...
    pos: Any = ...
    endpos: Any = ...
    def __init__(self, path: Any, pos: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...

class Signs:
    path: Any = ...
    pos: Any = ...
    endpos: Any = ...
    def __init__(self, path: Any, pos: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...

class NPCs:
    path: Any = ...
    pos: Any = ...
    endpos: Any = ...
    def __init__(self, path: Any, pos: Any) -> None: ...
    def __len__(self): ...
    len: Any = ...
    def __iter__(self) -> Any: ...

class Trail:
    path: Any = ...
    pos: Any = ...
    def __init__(self, path: Any, pos: Any) -> None: ...
    def get(self): ...

class World:
    path: Any = ...
    header: Any = ...
    tilepos: Any = ...
    tiles: Any = ...
    def __init__(self, path: Any) -> None: ...
    chestpos: Any = ...
    chests: Any = ...
    def ready_chests(self) -> None: ...
    signpos: Any = ...
    signs: Any = ...
    def ready_signs(self) -> None: ...
    npcpos: Any = ...
    npcs: Any = ...
    def ready_npcs(self) -> None: ...
    def make_split(self) -> None: ...

def get_content(f: Any, layers: int = ...): ...
def get_multis(): ...
def get_myterraria(): ...
def get_steamdir(): ...

cloud_warning_flag: int

def get_remote_terraria_dirs(sub_dir: str = ...) -> None: ...
def get_worlds(source: str = ...) -> None: ...
def get_players() -> None: ...
def get_next_world(name: Optional[Any] = ...): ...
def write_tiles(surface: Any, header: Any, walls: Any = ..., report: bool = ..., overwrite_no_mt: Any = ..., callback: Optional[Any] = ...): ...