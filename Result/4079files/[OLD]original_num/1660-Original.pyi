# (generated with --quick)

import enum
from typing import Any, Coroutine, List, Type

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
    name: str
    required_fields: List[str]
    signature: str
    def __init__(self, signature: str, name: str) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...

class TrafikverketTrain(object):
    __doc__: str
    _api: Any
    def __init__(self, client_session, api_key: str) -> None: ...
    def async_get_next_train_stop(self, from_station: StationInfo, to_station: StationInfo, after_time: datetime.datetime) -> Coroutine[Any, Any, TrainStop]: ...
    def async_get_train_station(self, location_name: str) -> Coroutine[Any, Any, StationInfo]: ...
    def async_get_train_stop(self, from_station: StationInfo, to_station: StationInfo, time_at_location: datetime.datetime) -> Coroutine[Any, Any, TrainStop]: ...
    def async_search_train_stations(self, location_name: str) -> Coroutine[Any, Any, List[StationInfo]]: ...

class TrainStop(object):
    __doc__: str
    advertised_time_at_location: datetime.datetime
    canceled: bool
    deviations: List[str]
    estimated_time_at_location: datetime.datetime
    id: Any
    modified_time: datetime.datetime
    other_information: List[str]
    required_fields: List[str]
    time_at_location: datetime.datetime
    def __init__(self, id, canceled: bool, advertised_time_at_location: datetime.datetime, estimated_time_at_location: datetime.datetime, time_at_location: datetime.datetime, other_information: List[str], deviations: List[str], modified_time: datetime.datetime) -> None: ...
    @classmethod
    def from_xml_node(cls, node) -> Any: ...
    def get_delay_time(self) -> datetime.timedelta: ...
    def get_state(self) -> TrainStopStatus: ...

class TrainStopStatus(enum.Enum):
    __doc__: str
    canceled: str
    delayed: str
    on_time: str
