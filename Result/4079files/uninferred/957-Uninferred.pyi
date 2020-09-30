from typing import Any, List

class Shipping:
    address_1: str
    address_2: str
    city: str
    state: str
    zip_code: str
    email: str
    mobile: str
    @staticmethod
    def deserialize(data: Any): ...
    def __init__(self, address_1: Any, address_2: Any, city: Any, state: Any, zip_code: Any, email: Any, mobile: Any) -> None: ...

class Order:
    amount: float
    shipping: Shipping
    status: str
    items: List[str]
    id: str = ...
    @staticmethod
    def deserialize(document: Any): ...
    def __init__(self, amount: Any, shipping: Any, status: Any, items: Any, id: Any) -> None: ...
