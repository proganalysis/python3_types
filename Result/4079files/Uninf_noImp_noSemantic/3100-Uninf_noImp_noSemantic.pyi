from Instanssi.store.models import StoreTransaction
from typing import Any

logger: Any

def handle_cancellation(ta: StoreTransaction) -> Any: ...
def handle_pending(ta: StoreTransaction) -> Any: ...
def handle_payment(ta: StoreTransaction) -> Any: ...
