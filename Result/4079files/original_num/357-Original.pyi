# (generated with --quick)

from typing import Any, List, Optional

MetadataError: Any
Type: Any

class Entity:
    name: str
    properties: List[Property]
    def __init__(self, name: str, properties: List[Property]) -> None: ...

class EnumValue:
    desc: str
    key: str
    label: str
    value: int
    def __init__(self, key: str, value: int, label: str, desc: str) -> None: ...

class Enumeration:
    name: str
    values: List[EnumValue]
    def __init__(self, name: str, values: List[EnumValue]) -> None: ...

class Model:
    __doc__: str
    entities: List[Entity]
    entity_names: List[str]
    enum_names: List[str]
    enums: List[Enumeration]
    def __init__(self) -> None: ...
    def add_entity(self, entity: Entity) -> None: ...
    def add_enum(self, enum: Enumeration) -> None: ...
    def entity(self, name: str) -> Entity: ...
    def enum(self, name: str) -> Enumeration: ...
    def is_entity(self, symbol: str) -> bool: ...
    def is_enum(self, symbol: str) -> bool: ...

class Property:
    __doc__: str
    default: Any
    desc: str
    is_optional: bool
    label: str
    name: str
    raw_type: str
    tag: int
    type: Any
    def __init__(self, name: str, tag: int, raw_type: str, label: str, desc: str, default: Optional[str], is_optional: bool) -> None: ...
