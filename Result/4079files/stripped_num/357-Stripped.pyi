# (generated with --quick)

from typing import Any

MetadataError: Any
Type: Any

class Entity:
    name: Any
    properties: Any
    def __init__(self, name, properties) -> None: ...

class EnumValue:
    desc: Any
    key: Any
    label: Any
    value: Any
    def __init__(self, key, value, label, desc) -> None: ...

class Enumeration:
    name: Any
    values: Any
    def __init__(self, name, values) -> None: ...

class Model:
    __doc__: str
    entities: list
    entity_names: list
    enum_names: list
    enums: list
    def __init__(self) -> None: ...
    def add_entity(self, entity) -> None: ...
    def add_enum(self, enum) -> None: ...
    def entity(self, name) -> Any: ...
    def enum(self, name) -> Any: ...
    def is_entity(self, symbol) -> bool: ...
    def is_enum(self, symbol) -> bool: ...

class Property:
    __doc__: str
    default: Any
    desc: Any
    is_optional: Any
    label: Any
    name: Any
    raw_type: Any
    tag: Any
    type: Any
    def __init__(self, name, tag, raw_type, label, desc, default, is_optional) -> None: ...
