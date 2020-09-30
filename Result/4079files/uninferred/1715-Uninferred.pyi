from typing import Any

class CartItem:
    item_id: str
    modify_time: str
    uid: str
    document_id: str = ...
    @staticmethod
    def deserialize(document: Any): ...
    def __init__(self, item_id: Any, modify_time: Any, uid: Any, document_id: Any) -> None: ...
