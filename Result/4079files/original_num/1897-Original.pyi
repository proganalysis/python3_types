# (generated with --quick)

from typing import Any, Coroutine, List

FieldFilter: Any
FilterOperation: Any
NodeHelper: Any
Trafikverket: Any
aiohttp: Any
asyncio: module

class TrafikverketWeather(object):
    __doc__: str
    _api: Any
    def __init__(self, client_session, api_key: str) -> None: ...
    def async_get_weather(self, location_name: str) -> Coroutine[Any, Any, WeatherStationInfo]: ...

class WeatherStationInfo(object):
    __doc__: str
    air_temp: float
    humidity: float
    precipitationtype: str
    required_fields: List[str]
    road_temp: float
    station_id: str
    station_name: str
    winddirection: float
    winddirectiontext: str
    windforce: float
    def __init__(self, station_name: str, station_id: str, road_temp: float, air_temp: float, humidity: float, precipitationtype: str, winddirection: float, winddirectiontext: str, windforce: float) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...
