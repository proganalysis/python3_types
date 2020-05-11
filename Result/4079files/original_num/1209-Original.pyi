# (generated with --quick)

import abc
import functools
import mixins
import pathlib
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
DataFileMixin: Type[mixins.DataFileMixin]
LevelMixin: Type[mixins.LevelMixin]
Path: Type[pathlib.Path]
ReprMixin: Type[mixins.ReprMixin]
SpritesMixin: Type[mixins.SpritesMixin]
char: Character
cont: Container
inv: Inventory
item: Item
json: module
math: module
player: Player
toml: module

_FuncT = TypeVar('_FuncT', bound=Callable)
_T = TypeVar('_T')

class Character(mixins.ReprMixin, mixins.LevelMixin, mixins.SpritesMixin):
    __doc__: str
    inventory: Inventory
    name: Any
    def __init__(self, name, inventory: Optional[Inventory] = ..., **kwargs) -> None: ...

class Container(mixins.ReprMixin):
    __doc__: str
    items: list
    max_capacity: int
    name: Any
    def __init__(self, items: Optional[list] = ..., max_capacity: int = ..., **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def append(self, item: Item) -> str: ...
    def remove(self, item: Item, count: int = ...) -> str: ...

class Inventory(Container):
    GEAR_SLOTS: Any
    __doc__: str
    gear: Any
    items: Any
    max_capacity: int
    name: Any
    def __init__(self, gear: Optional[dict] = ..., items: Optional[list] = ..., **kwargs) -> None: ...
    def better_combine_item(self, base_item: Item, combination: int, *materials) -> str: ...
    def combine_item(self, *items) -> str: ...
    def equip(self, item: Item) -> str: ...
    def equip_from_index(self, item_index: int) -> str: ...
    def unequip(self, slot: str) -> str: ...

class Item(mixins.ReprMixin, mixins.DataFileMixin):
    EQUIPMENT: Tuple[str, str, str, str, str]
    ID: int
    __doc__: str
    _count: Any
    attack: Any
    combinations: Any
    combinations2: Any
    defence: Any
    description: Any
    descriptions: Any
    metadata: Any
    name: Any
    slot: Any
    specialAttack: Any
    stackable: Any
    def __eq__(self, item: object) -> bool: ...
    def __gt__(self, item: object) -> bool: ...
    def __init__(self, id_num: int, **kwargs) -> None: ...
    def __lt__(self, item: object) -> bool: ...

class Player(Character):
    __doc__: str
    inventory: Any
    name: Any

def __getattr__(name) -> Any: ...
def abstractmethod(callable: _FuncT) -> _FuncT: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
