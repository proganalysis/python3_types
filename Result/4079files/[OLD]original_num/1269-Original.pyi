# (generated with --quick)

import collections
import decimal
from typing import Any, Callable, Iterable, List, Sized, Tuple, Type, TypeVar, Union

Installment = `namedtuple-Installment-number-payment-interest-principal-total_interest-balance`

Decimal: Type[decimal.Decimal]

_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance = TypeVar('_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance', bound=`namedtuple-Installment-number-payment-interest-principal-total_interest-balance`)

class Loan(object):
    __doc__: str
    _currency: Any
    _monthly_payment: Any
    _schedule: List[`namedtuple-Installment-number-payment-interest-principal-total_interest-balance`]
    apr: decimal.Decimal
    apy: decimal.Decimal
    compounded: Any
    interest: decimal.Decimal
    interest_to_principle: float
    monthly_payment: Any
    n_periods: int
    principal: decimal.Decimal
    summarize: None
    term: Any
    term_unit: Any
    total_interest: decimal.Decimal
    total_paid: decimal.Decimal
    total_principal: decimal.Decimal
    years_to_pay: float
    def __init__(self, principal, interest, term, term_unit = ..., compounded = ..., currency = ...) -> None: ...
    def _amortize(self) -> List[`namedtuple-Installment-number-payment-interest-principal-total_interest-balance`]: ...
    @staticmethod
    def _quantize(value) -> decimal.Decimal: ...
    def _simple_interest(self, term) -> decimal.Decimal: ...
    def schedule(self, nth_payment = ...) -> Any: ...
    def split_payment(self, number: int, amount: decimal.Decimal) -> Tuple[decimal.Decimal, decimal.Decimal]: ...

class `namedtuple-Installment-number-payment-interest-principal-total_interest-balance`(tuple):
    __slots__ = ["balance", "interest", "number", "payment", "principal", "total_interest"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str]
    balance: Any
    interest: Any
    number: Any
    payment: Any
    principal: Any
    total_interest: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`], number, payment, interest, principal, total_interest, balance) -> `_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`: ...
    def _replace(self: `_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`, **kwds) -> `_Tnamedtuple-Installment-number-payment-interest-principal-total_interest-balance`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
