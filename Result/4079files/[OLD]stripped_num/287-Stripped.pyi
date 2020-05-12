# (generated with --quick)

import asyncio.events
import asyncio.futures
import asyncio.tasks
from typing import Any, Callable, Coroutine, Dict, Iterable, Optional, Sequence, Sized, SupportsFloat, Tuple, Type, TypeVar, Union

Dump1090Resources = `namedtuple-Dump1090Resources-base-receiver-stats-aircraft`
MetricSpecItemType = Tuple[str, str, str]
MetricsSpecGroupType = Sequence[Tuple[str, str, str]]
Position = `namedtuple-Position-latitude-longitude`
PositionType = Tuple[float, float]

AbstractEventLoop: Type[asyncio.events.AbstractEventLoop]
AircraftKeys: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
Gauge: Any
Service: Any
Specs: Any
aiohttp: Any
asyncio: module
collections: module
datetime: module
logger: logging.Logger
logging: module
math: module
warnings: module

_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft = TypeVar('_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft', bound=`namedtuple-Dump1090Resources-base-receiver-stats-aircraft`)
_Tnamedtuple-Position-latitude-longitude = TypeVar('_Tnamedtuple-Position-latitude-longitude', bound=`namedtuple-Position-latitude-longitude`)

class Dump1090Exporter(object):
    __doc__: str
    aircraft_interval: datetime.timedelta
    aircraft_task: Optional[Union[asyncio.tasks.Task, asyncio.futures.Future[nothing]]]
    dump1090urls: `namedtuple-Dump1090Resources-base-receiver-stats-aircraft`
    fetch_timeout: Any
    host: Any
    loop: Any
    metrics: Dict[str, dict]
    origin: Optional[`namedtuple-Position-latitude-longitude`]
    port: Any
    session: Any
    stats_interval: datetime.timedelta
    stats_task: Optional[Union[asyncio.tasks.Task, asyncio.futures.Future[nothing]]]
    stats_time_periods: Any
    svr: Any
    def __init__(self, url, host = ..., port = ..., aircraft_interval = ..., stats_interval = ..., time_periods = ..., origin = ..., fetch_timeout = ..., loop = ...) -> None: ...
    def _create_gauge_metric(self, label, doc) -> Any: ...
    def initialise_metrics(self) -> None: ...
    def process_aircraft(self, aircraft, threshold = ...) -> None: ...
    def process_stats(self, stats, time_periods = ...) -> None: ...
    def start(self) -> Coroutine[Any, Any, None]: ...
    def stop(self) -> Coroutine[Any, Any, None]: ...
    def updater_aircraft(self) -> Coroutine[Any, Any, nothing]: ...
    def updater_stats(self) -> Coroutine[Any, Any, nothing]: ...

class `namedtuple-Dump1090Resources-base-receiver-stats-aircraft`(tuple):
    __slots__ = ["aircraft", "base", "receiver", "stats"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str]
    aircraft: Any
    base: Any
    receiver: Any
    stats: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`], base, receiver, stats, aircraft) -> `_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`: ...
    def _replace(self: `_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`, **kwds) -> `_Tnamedtuple-Dump1090Resources-base-receiver-stats-aircraft`: ...

class `namedtuple-Position-latitude-longitude`(tuple):
    __slots__ = ["latitude", "longitude"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    latitude: Any
    longitude: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Position-latitude-longitude`], latitude, longitude) -> `_Tnamedtuple-Position-latitude-longitude`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Position-latitude-longitude`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Position-latitude-longitude`: ...
    def _replace(self: `_Tnamedtuple-Position-latitude-longitude`, **kwds) -> `_Tnamedtuple-Position-latitude-longitude`: ...

def asin(__x: SupportsFloat) -> float: ...
def build_resources(base_url) -> `namedtuple-Dump1090Resources-base-receiver-stats-aircraft`: ...
def cos(__x: SupportsFloat) -> float: ...
def fetch(url, session, timeout = ..., loop = ...) -> coroutine: ...
def haversine_distance(pos1, pos2, radius = ...) -> Any: ...
def radians(__x: SupportsFloat) -> float: ...
def sin(__x: SupportsFloat) -> float: ...
def sqrt(__x: SupportsFloat) -> float: ...
