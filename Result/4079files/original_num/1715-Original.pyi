# (generated with --quick)

from typing import Callable, Optional, Type, TypeVar

_T = TypeVar('_T')

class CartItem:
    __doc__: str
    document_id: str
    item_id: str
    modify_time: str
    uid: str
    def __init__(self, item_id: str, modify_time: str, uid: str, document_id: Optional[str] = ...) -> None: ...
    @staticmethod
    def deserialize(document) -> Optional[CartItem]: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
