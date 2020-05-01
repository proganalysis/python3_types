# (generated with --quick)

import itertools
from typing import Any, Dict, Generator, Iterable, Optional, Type

DeferredType: Any
PolygraphField: Any
PolygraphInputValue: Any
PolygraphType: Any
Schema: Any
StrictDict: Any
attrib: Any
attrs: Any
chain: Type[itertools.chain]
evolve: Any

class TypeMap(Dict[TypeName, Any]):
    def __init__(self, val: Dict[TypeName, Any]) -> None: ...

class TypeName(str):
    def __init__(self, val: str) -> None: ...

class UnresolvedType(Any):
    def __init__(self, val) -> None: ...

def build_schema(query_type, mutation_type = ..., additional_types: Optional[Iterable] = ...) -> Any: ...
def collect_type_names(types: Iterable[UnresolvedType]) -> TypeMap: ...
def undefer_field(field, type_map: TypeMap) -> Any: ...
def undefer_input_value(input_value, type_map: TypeMap) -> Any: ...
def undefer_subtypes(type_: UnresolvedType, type_map: TypeMap) -> Any: ...
def undefer_type(type_: UnresolvedType, type_map: TypeMap) -> Any: ...
def visit_types(types: Iterable[UnresolvedType], visited = ...) -> Generator[UnresolvedType, Any, None]: ...