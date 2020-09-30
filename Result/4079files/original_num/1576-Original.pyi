# (generated with --quick)

import collections
from typing import Any, Callable, Generator, Iterable, Sized, Tuple, Type, TypeVar, Union

DATATUPLE = `namedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`

JSONDecodeError: Type[ValueError]
TPEX_BASE_URL: str
TWSE_BASE_URL: str
analytics: Any
codes: Any
datetime: module
e: ImportError
get_proxies: Any
requests: module
urllib: module

_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction = TypeVar('_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction', bound=`namedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`)

class BaseFetcher(object):
    def _convert_date(self, date) -> str: ...
    def _make_datatuple(self, data) -> None: ...
    def fetch(self, year, month, sid, retry) -> None: ...
    def purify(self, original_data) -> None: ...

class Stock(Any):
    capacity: list
    change: list
    close: list
    data: Any
    date: list
    fetcher: Union[TPEXFetcher, TWSEFetcher]
    high: list
    low: list
    open: list
    price: list
    raw_data: list
    sid: str
    transaction: list
    turnover: list
    def __init__(self, sid: str, initial_fetch: bool = ...) -> None: ...
    def _month_year_iter(self, start_month, start_year, end_month, end_year) -> Generator[Tuple[int, int], Any, None]: ...
    def fetch(self, year: int, month: int) -> Any: ...
    def fetch_31(self) -> list: ...
    def fetch_from(self, year: int, month: int) -> list: ...

class TPEXFetcher(BaseFetcher):
    REPORT_URL: str
    def _make_datatuple(self, data) -> `namedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`: ...
    def fetch(self, year: int, month: int, sid: str, retry: int = ...) -> Any: ...
    def purify(self, original_data) -> list: ...

class TWSEFetcher(BaseFetcher):
    REPORT_URL: str
    def _make_datatuple(self, data) -> `namedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`: ...
    def fetch(self, year: int, month: int, sid: str, retry: int = ...) -> Any: ...
    def purify(self, original_data) -> list: ...

class `namedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`(tuple):
    __slots__ = ["capacity", "change", "close", "date", "high", "low", "open", "transaction", "turnover"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str, str, str, str]
    capacity: Any
    change: Any
    close: Any
    date: Any
    high: Any
    low: Any
    open: Any
    transaction: Any
    turnover: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`], date, capacity, turnover, open, high, low, close, change, transaction) -> `_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`: ...
    def _replace(self: `_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`, **kwds) -> `_Tnamedtuple-Data-date-capacity-turnover-open-high-low-close-change-transaction`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
