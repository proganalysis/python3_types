from prices import Money, MoneyRange, TaxedMoney, TaxedMoneyRange
from typing import Any, TypeVar

T = TypeVar('T', Money, MoneyRange, TaxedMoney, TaxedMoneyRange)
register: Any

def in_currency(base: T, currency: str) -> T: ...
