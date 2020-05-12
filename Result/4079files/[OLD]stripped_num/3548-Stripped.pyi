# (generated with --quick)

from typing import Any

Party: Any
exchange_rates: Any

class Expense:
    amount: Any
    currency: Any
    paid_for: Any
    parties_involved: Any
    def __init__(self, paid_for, currency, amount, parties_involved = ...) -> None: ...
    def add_party(self, party) -> None: ...
    def currency_is_supported(self) -> Any: ...
    def remove_party(self, party) -> None: ...
