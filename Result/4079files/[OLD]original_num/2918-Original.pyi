# (generated with --quick)

import decimal
from typing import Any, Optional, Type, TypeVar

BASE_CURRENCY: Any
Decimal: Type[decimal.Decimal]
Money: Any
MoneyRange: Any
TaxedMoney: Any
TaxedMoneyRange: Any
default_app_config: str
operator: module
settings: Any

T = TypeVar('T', Any, Any, Any, Any)

def exchange_currency(base: T, to_currency: str, *, conversion_rate: Optional[decimal.Decimal] = ...) -> T: ...
def get_conversion_rate(from_currency: str, to_currency: str) -> decimal.Decimal: ...
def get_rate_from_db(currency: str) -> decimal.Decimal: ...
