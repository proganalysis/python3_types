# (generated with --quick)

import decimal
import types
from typing import Any, Callable, List, Optional, Type

BasicContext: decimal.Context
Clamped: Type[decimal.Clamped]
Context: Type[decimal.Context]
ConversionSyntax: Type[decimal.ConversionSyntax]
Decimal: Type[decimal.Decimal]
DecimalException: Type[decimal.DecimalException]
DecimalTuple: Type[decimal.DecimalTuple]
DefaultContext: decimal.Context
DivisionByZero: Type[decimal.DivisionByZero]
DivisionImpossible: Type[decimal.DivisionImpossible]
DivisionUndefined: Type[decimal.DivisionUndefined]
ExtendedContext: decimal.Context
FloatOperation: Type[decimal.FloatOperation]
HAVE_THREADS: bool
Inexact: Type[decimal.Inexact]
InvalidContext: Type[decimal.InvalidContext]
InvalidOperation: Type[decimal.InvalidOperation]
MAX_EMAX: int
MAX_PREC: int
MIN_EMIN: int
MIN_ETINY: int
Overflow: Type[decimal.Overflow]
ROUND_05UP: str
ROUND_CEILING: str
ROUND_DOWN: str
ROUND_FLOOR: str
ROUND_HALF_DOWN: str
ROUND_HALF_EVEN: str
ROUND_HALF_UP: str
ROUND_UP: str
Rounded: Type[decimal.Rounded]
Subnormal: Type[decimal.Subnormal]
TracebackType: Type[types.TracebackType]
Underflow: Type[decimal.Underflow]
ast: module
datetime: module
linecache: module
`namedtuple-DecimalTuple-0`: Type[decimal.`namedtuple-DecimalTuple-0`]
request: module
requests: module
sys: module
time: module

def __getattr__(name) -> Any: ...
def auth(params) -> Any: ...
def formatAnimeDate(data) -> str: ...
def formatAnimeDescription(data) -> Any: ...
def getAnimeGenres(data) -> str: ...
def getAnimeInfo(anime, token, index: int) -> Any: ...
def getAnimes(anime, token) -> List[list]: ...
def getMangaInfo(manga, token, index: int) -> Any: ...
def getMangas(manga, token) -> List[list]: ...
def getcontext() -> decimal.Context: ...
def localcontext(ctx: Optional[decimal.Context] = ...) -> decimal._ContextManager: ...
def setcontext(context: decimal.Context) -> None: ...
def shuffle(x: list, random: Optional[Callable[[], float]] = ...) -> None: ...
