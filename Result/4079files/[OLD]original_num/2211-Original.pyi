# (generated with --quick)

from typing import Any, Dict, Generic, Type, TypeVar

ResourceObject: Any
serializers: Any

T = TypeVar('T', bound=Any)

class AutoSchemaDescriptor(Generic[T]):
    __doc__: str
    _cached: Any
    api_type: str
    id_field: str
    init_kwargs: Dict[str, Any]
    def __get__(self, serializer: T, objtype: Type[T]) -> type: ...
    def __init__(self, api_type: str, id_field: str, init_kwargs: Dict[str, Any]) -> None: ...

def auto_schema(api_type: str, *, id_field: str = ..., **kwargs) -> AutoSchemaDescriptor: ...
def from_serializer(serializer, api_type: str, *, id_field: str = ..., **kwargs) -> type: ...
