# (generated with --quick)

from typing import Any, Hashable, Iterator, Mapping, Sequence, Tuple

Client: Any
Locale: Any
MultilingualText: Any
UnknownLocaleError: Any
__all__: Tuple[str, str, str]
collections: module
enum: module
logging: module

class Entity(Mapping, Hashable):
    __doc__: str
    attributes: Mapping[str, Any]
    client: Any
    data: Any
    description: Any
    id: EntityId
    label: Any
    type: EntityType
    def __getitem__(self, key: Entity) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, id: EntityId, client) -> None: ...
    def __iter__(self) -> Iterator[Entity]: ...
    def __len__(self) -> int: ...
    def getlist(self, key: Entity) -> Sequence: ...
    def iterlists(self) -> Iterator[Tuple[Entity, Sequence]]: ...
    def iterlistvalues(self) -> Iterator[Sequence]: ...
    def lists(self) -> Sequence[Tuple[Entity, Sequence]]: ...
    def listvalues(self) -> Sequence[Sequence]: ...
    def load(self) -> None: ...

class EntityId(str):
    def __init__(self, val: str) -> None: ...

class EntityType(enum.Enum):
    __doc__: str
    item: str
    property: str

class multilingual_attribute:
    __doc__: str
    attribute: str
    def __get__(self, obj: Entity, cls = ...) -> Any: ...
    def __init__(self, attribute: str) -> None: ...
