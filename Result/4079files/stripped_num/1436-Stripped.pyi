# (generated with --quick)

from typing import Any

Config: Any
DataHandler: Any
ET: module
MsgResource: Any
MsgTemplate: Any
SlackerAdapter: Any
json: module
requests: module
yh: Any

class Bus(object):
    ansan_bus: Any
    ansan_station: Any
    data_handler: Any
    service_key: Any
    slackbot: Any
    def _Bus__request(self, url) -> Any: ...
    def __init__(self, slackbot = ...) -> None: ...
    def arrive_info(self, station_id, real_time = ...) -> None: ...
    def get_bus_number(self, route_id) -> Any: ...
    def get_station_id(self, name) -> None: ...
