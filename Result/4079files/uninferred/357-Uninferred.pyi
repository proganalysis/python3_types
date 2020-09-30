from .types import Type
from typing import List, Optional

class Property:
    name: str
    tag: int
    raw_type: str
    type: Type
    label: str
    desc: str
    default: Optional[str]
    is_optional: bool
    def __init__(self, name: str, tag: int, raw_type: str, label: str, desc: str, default: Optional[str], is_optional: bool) -> None: ...

class Entity:
    name: str
    properties: List[Property]
    def __init__(self, name: str, properties: List[Property]) -> None: ...

class EnumValue:
    key: str
    value: int
    label: str
    desc: str
    def __init__(self, key: str, value: int, label: str, desc: str) -> None: ...

class Enumeration:
    name: str
    values: List[EnumValue]
    def __init__(self, name: str, values: List[EnumValue]) -> None: ...

class Model:
    entities: List[Entity]
    enums: List[Enumeration]
    def __init__(self) -> None: ...
    def add_entity(self, entity: Entity) -> None: ...
    def add_enum(self, enum: Enumeration) -> None: ...
    def entity(self, name: str) -> Entity: ...
    def enum(self, name: str) -> Enumeration: ...
    @property
    def entity_names(self) -> List[str]: ...
    @property
    def enum_names(self) -> List[str]: ...
    def is_entity(self, symbol: str) -> bool: ...
    def is_enum(self, symbol: str) -> bool: ...
