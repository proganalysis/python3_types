from itertools import chain
from typing import Dict, Iterable, NewType, Union

from attr import attrib, attrs, evolve

from polygraph.types import (
    DeferredType,
    PolygraphField,
    PolygraphInputValue,
    PolygraphType,
)
from polygraph.utils.strict_dict import StrictDict


TypeName = NewType("TypeName", str)
TypeMap = NewType("TypeMap", Dict[TypeName, PolygraphType])
UnresolvedType = NewType("UnresolvedType", Union[PolygraphType, DeferredType])


@attrs
class Schema:
    query = attrib()
    mutation = attrib()


def visit_types(types: Iterable[UnresolvedType], visited=None):
    """
    Recursively walks over all types in a depth-first manner
    """
    visited = visited or set()

    for type_ in (t for t in types if t not in visited):
        if isinstance(type_, DeferredType):
            continue
        yield type_
        visited.add(type_)
        next_types = (t for t in chain(
            [field.type_ for field in type_.fields],
            [field.type_ for field in type_.input_fields],
            type_.interfaces,
            type_.possible_types,
            [type_.of_type] if type_.of_type else [],
        ) if t not in visited)
        yield from visit_types(next_types, visited)


def collect_type_names(types: Iterable[UnresolvedType]) -> TypeMap:
    """
    Builds a mapping of type names to types
    """
    return StrictDict({
        type_.name: type_ for type_ in visit_types(types)
        if not isinstance(type_, DeferredType)
    })


def undefer_type(type_: UnresolvedType, type_map: TypeMap) -> PolygraphType:
    if isinstance(type_, DeferredType):
        return type_map.get(type_.name)
    else:
        return type_


def undefer_input_value(
    input_value: PolygraphInputValue,
    type_map: TypeMap,
) -> PolygraphInputValue:
    return evolve(
        input_value,
        type_=undefer_type(input_value.type_, type_map),
    )


def undefer_field(field: PolygraphField, type_map: TypeMap) -> PolygraphField:
    return evolve(
        field,
        type_=undefer_type(field.type_, type_map),
        args=tuple(undefer_input_value(v) for v in field.args),
    )


def undefer_subtypes(type_: UnresolvedType, type_map: TypeMap) -> PolygraphType:
    type_ = undefer_type(type_, type_map)
    return evolve(
        type_,
        fields=tuple(undefer_field(f, type_map) for f in type_.fields),
        interfaces=tuple(undefer_subtypes(i, type_map) for i in type_.interfaces),
        possible_types=tuple(undefer_subtypes(p, type_map) for p in type_.possible_types),
        of_type=undefer_type(type_.of_type, type_map),
    )


def build_schema(
    query_type,
    mutation_type: PolygraphType=None,
    additional_types: Iterable[PolygraphType]=None,
) -> Schema:
    types = additional_types or []
    types.append(query_type)
    if mutation_type:
        types.append(mutation_type)
    type_map = collect_type_names(types)
    types = [undefer_subtypes(t, type_map) for t in types]
    return Schema(
        query=undefer_subtypes(query_type),
        mutation=undefer_subtypes(mutation_type),
    )
