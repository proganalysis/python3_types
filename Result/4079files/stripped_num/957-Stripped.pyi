# (generated with --quick)

from typing import Callable, Optional, Type, TypeVar

_T = TypeVar('_T')

class Order:
    __doc__: str
    id: None
    def __init__(self) -> None: ...
    @staticmethod
    def deserialize(document) -> Optional[Order]: ...

class Shipping:
    __doc__: str
    def __init__(self) -> None: ...
    @staticmethod
    def deserialize(data) -> Optional[Shipping]: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
