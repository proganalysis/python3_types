# (generated with --quick)

import decimal
from typing import Any, Type

Decimal: Type[decimal.Decimal]
RecordDecoder: Any
_decode_date: Any
_decode_datetime: Any
_decode_time: Any
_get_decoder: Any
datetime: Type[datetime.datetime]
decoder: Any
pytest: Any
time: Type[datetime.time]
timedelta: Type[datetime.timedelta]
timezone: Type[datetime.timezone]

def test_decode_date() -> None: ...
def test_decode_datetime() -> None: ...
def test_decode_rows(decoder) -> None: ...
def test_decode_rows_missing_field(decoder) -> None: ...
def test_decode_time() -> None: ...
def test_get_decoder() -> None: ...
