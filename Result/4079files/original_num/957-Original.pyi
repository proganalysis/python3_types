# (generated with --quick)

from typing import Callable, List, Optional, Type, TypeVar

_T = TypeVar('_T')

class Order:
    __doc__: str
    amount: float
    id: str
    items: List[str]
    shipping: Shipping
    status: str
    def __init__(self, amount: float, shipping: Shipping, status: str, items: List[str], id: Optional[str] = ...) -> None: ...
    @staticmethod
    def deserialize(document) -> Optional[Order]: ...

class Shipping:
    __doc__: str
    address_1: str
    address_2: str
    city: str
    email: str
    mobile: str
    state: str
    zip_code: str
    def __init__(self, address_1: str, address_2: str, city: str, state: str, zip_code: str, email: str, mobile: str) -> None: ...
    @staticmethod
    def deserialize(data) -> Optional[Shipping]: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
