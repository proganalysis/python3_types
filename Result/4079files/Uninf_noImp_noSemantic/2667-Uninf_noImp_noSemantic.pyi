from Instanssi.store.methods import PaymentMethod
from Instanssi.store.models import StoreItem, StoreItemVariant, StoreTransaction
from typing import Any

logger: Any

class TransactionException(Exception): ...

def validate_item(item: dict) -> Any: ...
def get_item_and_variant(item: dict) -> Tuple[StoreItem, StoreItemVariant]: ...
def validate_payment_method(items: list, method: PaymentMethod) -> Any: ...
def create_store_transaction(data: dict) -> StoreTransaction: ...
def begin_payment_process(method: PaymentMethod, ta: StoreTransaction) -> Any: ...