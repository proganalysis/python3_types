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
    def __init__(self, client_session, api_key) -> None: ...
    def async_get_weather(self, location_name) -> Coroutine[Any, Any, WeatherStationInfo]: ...

class WeatherStationInfo(object):
    __doc__: str
    air_temp: Any
    humidity: Any
    precipitationtype: Any
    required_fields: List[str]
    road_temp: Any
    station_id: Any
    station_name: Any
    winddirection: Any
    winddirectiontext: Any
    windforce: Any
    def __init__(self, station_name, station_id, road_temp, air_temp, humidity, precipitationtype, winddirection, winddirectiontext, windforce) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...
