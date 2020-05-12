# (generated with --quick)

import enum
from typing import Any, Dict, List, Type

Enum: Type[enum.Enum]
json: module

class Pokemon:
    __doc__: str
    abilities: Any
    active: Any
    buff: Dict[str, List[int]]
    condition: Any
    item: Any
    level: int
    moves: list
    name: Any
    stats: Any
    status: Any
    types: Any
    def __init__(self, name, condition, active, level) -> None: ...
    def __repr__(self) -> str: ...
    def buff_affect(self, stat) -> int: ...
    def load_known(self, abilities, item, stats, moves) -> None: ...
    def load_unknown(self) -> None: ...

class Status(enum.Enum):
    BRN: int
    FRZ: int
    PAR: int
    PSN: int
    SLP: int
    TOX: int
    UNK: int
    __doc__: str

class Team:
    __doc__: str
    pokemons: list
    def __contains__(self, pkm_name) -> bool: ...
    def __init__(self, *pkms) -> None: ...
    def __repr__(self) -> str: ...
    def active(self) -> Any: ...
    def add(self, pokemon) -> None: ...
    def remove(self, pkm_name) -> None: ...

def infos_for_pokemon(pkm_name) -> Dict[str, Any]: ...
