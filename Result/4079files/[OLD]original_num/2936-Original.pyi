# (generated with --quick)

from typing import Any, Dict, Tuple, Type, TypeVar, Union

BaseModel: Any
_generic_types_cache: Dict[Tuple[Any, Any], type]
create_model: Any
gather_validators: Any

GenericModelT = TypeVar('GenericModelT', bound=GenericModel)

class GenericModel(Any):
    __slots__ = []
    __concrete__: bool
    def __class_getitem__(cls: Type[GenericModelT], params: Union[type, Tuple[type, ...]]) -> type: ...
    def __new__(cls, *args, **kwargs) -> Any: ...

def check_parameters_count(cls: Type[GenericModel], parameters: tuple) -> None: ...
def concrete_name(cls: type, params: Tuple[type, ...]) -> str: ...
def resolve_type_hint(type_, typevars_map: dict) -> type: ...
