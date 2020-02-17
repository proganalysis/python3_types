# (generated with --quick)

import decimal
import fractions
import typing
from typing import Any, Iterable, Optional, Type, TypeVar

ChatLogger: Any
Counter: Type[typing.Counter]
Message: Any
RateLimiter: Any
command: Any
datetime: Type[datetime.datetime]
get_now: Any
get_redis: Any
hualao: Any
plural: Any
r: Any
rlimiter: Any
timedelta: Type[datetime.timedelta]
tz: Any

_Number = TypeVar('_Number', float, decimal.Decimal, fractions.Fraction)

def mean(data: Iterable[_Number]) -> _Number: ...
def stdev(data: Iterable[_Number], xbar: Optional[_Number] = ...) -> _Number: ...
