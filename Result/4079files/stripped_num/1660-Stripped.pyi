# (generated with --quick)

import enum
from typing import Any, Coroutine, List, Type, Union

Enum: Type[enum.Enum]
FieldFilter: Any
FieldSort: Any
FilterOperation: Any
NodeHelper: Any
OrFilter: Any
SortOrder: Any
Trafikverket: Any
aiohttp: Any
asyncio: module
datetime: Type[datetime.datetime]
timedelta: Type[datetime.timedelta]
typing: module

class StationInfo(object):
    __doc__: str
    name: Any
    required_fields: List[str]
    signature: Any
    def __init__(self, signature, name) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...

class TrafikverketTrain(object):
    __doc__: str
    _api: Any
    def __init__(self, client_session, api_key) -> None: ...
    def async_get_next_train_stop(self, from_station, to_station, after_time) -> Coroutine[Any, Any, TrainStop]: ...
    def async_get_train_station(self, location_name) -> Coroutine[Any, Any, StationInfo]: ...
    def async_get_train_stop(self, from_station, to_station, time_at_location) -> Coroutine[Any, Any, TrainStop]: ...
    def async_search_train_stations(self, location_name) -> Coroutine[Any, Any, List[Union[StationInfo, Type[StationInfo]]]]: ...

class TrainStop(object):
    __doc__: str
    advertised_time_at_location: Any
    canceled: Any
    deviations: Any
    estimated_time_at_location: Any
    id: Any
    modified_time: Any
    other_information: Any
    required_fields: List[str]
    time_at_location: Any
    def __init__(self, id, canceled, advertised_time_at_location, estimated_time_at_location, time_at_location, other_information, deviations, modified_time) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...
    def get_delay_time(self) -> Any: ...
    def get_state(self) -> Any: ...

class TrainStopStatus(enum.Enum):
    __doc__: str
    canceled: str
    delayed: str
    on_time: str
