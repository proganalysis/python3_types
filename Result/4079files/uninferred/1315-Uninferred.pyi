from typing import Any

def convert(value: Any): ...
def loan_200k(): ...

class TestLoan:
    def test_monthly_payment(self, loan_200k: Any) -> None: ...
    nth_principal: Any = ...
    def test_nth_principal_payment(self, loan_200k: Any, nth_payment: Any, principal: Any) -> None: ...
    nth_interest: Any = ...
    def test_nth_interest_payment(self, loan_200k: Any, nth_payment: Any, interest: Any) -> None: ...
    nth_total_interest: Any = ...
    def test_nth_total_interest_payment(self, loan_200k: Any, nth_payment: Any, total_interest: Any) -> None: ...
    nth_balance: Any = ...
    def test_nth_balance(self, loan_200k: Any, nth_payment: Any, balance: Any) -> None: ...
    def test_original_balance(self, loan_200k: Any) -> None: ...
    def test_interest_rate(self, loan_200k: Any) -> None: ...
    def test_apy(self, loan_200k: Any) -> None: ...
    def test_apr(self, loan_200k: Any) -> None: ...
    def test_term(self, loan_200k: Any) -> None: ...
    def test_total_principal(self, loan_200k: Any) -> None: ...
    def test_total_interest(self, loan_200k: Any) -> None: ...
    def test_total_paid(self, loan_200k: Any) -> None: ...
    def test_interest_to_principle(self, loan_200k: Any) -> None: ...
    def test_years_to_pay(self, loan_200k: Any) -> None: ...
