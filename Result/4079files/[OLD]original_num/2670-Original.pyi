# (generated with --quick)

from typing import Any, List

currency_types: List[str]
expense: Any
expense_types: List[str]
group: Any
group_names: List[str]
party: Any
party_names: List[str]
payment: Any
pytest: Any
random: module

class TestGroup:
    @classmethod
    def setup_class(cls) -> None: ...
    def test_add_expense_to_group_also_adds_parties(self) -> None: ...
    def test_assertion_error_if_add_not_expense(self) -> None: ...
    def test_assertion_error_if_add_not_party(self) -> None: ...
    def test_assertion_error_if_add_not_payment(self) -> None: ...
    def test_no_error_if_add_expense(self) -> None: ...
    def test_no_error_if_add_party(self) -> None: ...
    def test_no_error_if_add_payment(self) -> None: ...
    def test_standardize_group_expenses(self) -> None: ...
    def test_standardize_group_expenses_and_payments(self) -> None: ...

def rand_expense() -> Any: ...
def rand_group() -> Any: ...
def rand_party() -> Any: ...
def rand_payment(e) -> Any: ...
