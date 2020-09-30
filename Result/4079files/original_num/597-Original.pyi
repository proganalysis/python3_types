# (generated with --quick)

from typing import Any, Dict

BeautifulSoup: Any
bus_api: BusParser
food_api: FoodParser
lib_api: LibParser
parse: module
requests: module
ssubob: Any
subway_api: SubwayParser

class BusParser(metaclass=Singleton):
    __doc__: str
    url: str
    def __init__(self) -> None: ...
    def get_station_stat(self, station_number) -> str: ...

class FoodParser:
    def __init__(self) -> None: ...
    def get_food(self, place) -> Any: ...
    def refresh(self, date = ...) -> None: ...

class LibParser(metaclass=Singleton):
    seat: Dict[str, Dict[str, Any]]
    url: str
    def __init__(self) -> None: ...
    def get_lib_stat(self) -> Dict[str, Dict[str, Any]]: ...

class Singleton(type):
    instance: None
    def __call__(cls: Singleton, *args, **kwargs) -> Any: ...

class SubwayParser(metaclass=Singleton):
    arrival_info_url: str
    station_name_url: str
    def __init__(self) -> None: ...
    def get_station_stat(self, station_name) -> Any: ...
