from pydantic import BaseModel
from typing import Any, ClassVar, Dict, Tuple, Type, TypeVar, Union

_generic_types_cache: Dict[Tuple[Type[Any], Union[Any, Tuple[Any, ...]]], Type[BaseModel]]
GenericModelT = TypeVar('GenericModelT', bound='GenericModel')

class GenericModel(BaseModel):
    __slots__: Any = ...
    __concrete__: ClassVar[bool] = ...
    def __new__(cls: Any, *args: Any, **kwargs: Any) -> Any: ...
    def __class_getitem__(cls: Type[GenericModelT], params: Union[Type[Any], Tuple[Type[Any], ...]]) -> Type[BaseModel]: ...

def concrete_name(cls: Type[Any], params: Tuple[Type[Any], ...]) -> str: ...
def resolve_type_hint(type_: Any, typevars_map: Dict[Any, Any]) -> Type[Any]: ...
def check_parameters_count(cls: Type[GenericModel], parameters: Tuple[Any, ...]) -> None: ...
