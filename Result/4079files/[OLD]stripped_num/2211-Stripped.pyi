# (generated with --quick)

from typing import Any, Generic, TypeVar

ResourceObject: Any
serializers: Any

T = TypeVar('T', bound=Any)

class AutoSchemaDescriptor(Generic[T]):
    __doc__: str
    _cached: Any
    api_type: Any
    id_field: Any
    init_kwargs: Any
    def __get__(self: AutoSchemaDescriptor[nothing], serializer, objtype) -> Any: ...
    def __init__(self: AutoSchemaDescriptor[nothing], api_type, id_field, init_kwargs) -> None: ...

def auto_schema(api_type, *, id_field = ..., **kwargs) -> AutoSchemaDescriptor[nothing]: ...
def from_serializer(serializer, api_type, *, id_field = ..., **kwargs) -> Any: ...
