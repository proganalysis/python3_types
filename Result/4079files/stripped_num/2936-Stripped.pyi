# (generated with --quick)

from typing import Any, Dict, NoReturn, Tuple, TypeVar

BaseModel: Any
_generic_types_cache: Dict[Tuple[GenericModel, Any], Any]
create_model: Any
gather_validators: Any

GenericModelT = TypeVar('GenericModelT', bound=GenericModel)

class GenericModel(Any):
    __slots__ = []
    __concrete__: bool
    def __class_getitem__(cls: GenericModel, params) -> Any: ...
    def __new__(cls, *args, **kwargs) -> NoReturn: ...

def check_parameters_count(cls, parameters) -> None: ...
def concrete_name(cls, params) -> str: ...
def resolve_type_hint(type_, typevars_map) -> Any: ...
