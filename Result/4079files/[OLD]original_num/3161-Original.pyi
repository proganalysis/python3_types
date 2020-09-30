# (generated with --quick)

from typing import Any, Callable, Dict, Tuple, Type, Union

CommonFieldMap: Dict[str, Tuple[Union[Callable[[Any], Any], Type[Union[int, str]]], Tuple[Union[int, str], ...]]]
CondFieldMap: Dict[str, Tuple[Any, Tuple[Union[int, str], ...]]]
EmptyIcon: Any
FcstFieldMap: Dict[str, Union[str, Tuple[Any, Tuple[str, ...]]]]
TreeDict: Any
TryShorten: Any
WeathProvs: Any
WeatherIconCache: dict
config: Any
controlevents: Any
datetime: Type[datetime.datetime]
functools: module
historybuffer: Any
icondir: Any
interval_str: Any
logsupport: Any
pygame: Any
requests: module
time: module

class APIXUWeatherSource(object):
    apikey: Any
    args: Dict[str, Any]
    baseurl: str
    json: Dict[nothing, nothing]
    location: Any
    thisStore: Any
    thisStoreName: Any
    def ConnectStore(self, store) -> None: ...
    def FetchWeather(self) -> None: ...
    def MapItem(self, src, item) -> Any: ...
    def __init__(self, storename, location, api) -> None: ...

def doage(basetime) -> Any: ...
def fcstlength(param) -> int: ...
def getdayname(param) -> str: ...
def geticon(url) -> Any: ...
def setAge(param) -> functools.partial[nothing]: ...
