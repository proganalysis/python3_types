# (generated with --quick)

from typing import Any

Party: Any
exchange_rates: Any

class Expense:
    amount: float
    currency: str
    paid_for: str
    parties_involved: Any
    def __init__(self, paid_for: str, currency: str, amount: float, parties_involved = ...) -> None: ...
    def add_party(self, party) -> None: ...
    def currency_is_supported(self) -> bool: ...
    def remove_party(self, party) -> None: ...
