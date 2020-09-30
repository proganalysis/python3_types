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

class Order:
    amount: float
    shipping: Shipping
    status: str
    items: List[str]
    id: str = ...
    @staticmethod
    def deserialize(document: Any): ...
