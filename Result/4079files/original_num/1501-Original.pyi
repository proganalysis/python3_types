# (generated with --quick)

import base_station
from typing import Any, Callable, Sequence, SupportsFloat, Type

BaseStation: Type[base_station.BaseStation]
csv: module
datetime: Type[datetime.datetime]
logging: module
os: module
pickle: module
random: module

class DataUtils(object):
    base_station_locations: Any
    base_station_reader: Callable
    base_stations: Any
    distance_between_stations: Callable
    distances: Any
    user_info_reader: Callable
    def __init__(self, location_file, user_info_file) -> None: ...
    @staticmethod
    def _shuffle(l: list) -> None: ...
    @staticmethod
    def calc_distance(lat_a, lng_a, lat_b, lng_b) -> float: ...

def asin(__x: SupportsFloat) -> float: ...
def cos(__x: SupportsFloat) -> float: ...
def memorize(filename) -> Callable[[Any], Any]: ...
def sqrt(__x: SupportsFloat) -> float: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
