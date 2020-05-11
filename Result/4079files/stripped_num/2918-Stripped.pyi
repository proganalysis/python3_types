# (generated with --quick)

import decimal
from typing import Any, Type, TypeVar

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

def exchange_currency(base, to_currency, *, conversion_rate = ...) -> Any: ...
def get_conversion_rate(from_currency, to_currency) -> Any: ...
def get_rate_from_db(currency) -> Any: ...
