from typing import Any

class CartItem:
    item_id: str
    modify_time: str
    uid: str
    document_id: str = ...
    @staticmethod
    def deserialize(document: Any): ...
