# (generated with --quick)

from typing import Any, Tuple

PaymentMethod: Any
StoreItem: Any
StoreItemVariant: Any
StoreTransaction: Any
TransactionItem: Any
bitpay: Any
logger: logging.Logger
logging: module
no_method: Any
paytrail: Any
timezone: Any
transaction: Any
uuid: module

class TransactionException(Exception): ...

def begin_payment_process(method, ta) -> Any: ...
def create_store_transaction(data: dict) -> Any: ...
def get_item_and_variant(item: dict) -> Tuple[Any, Any]: ...
def validate_item(item: dict) -> None: ...
def validate_payment_method(items: list, method) -> None: ...
