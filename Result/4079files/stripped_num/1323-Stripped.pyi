# (generated with --quick)

from typing import Any

ParserError: Any
Pressure: Any
Provider: Any
ProviderException: Any
Status: Any
arrow: Any
requests: module
urllib: module

class Pioupiou(Any):
    provider_code: str
    provider_name: str
    provider_url: str
    def get_status(self, station_id, status, location_date, location_status) -> Any: ...
    def process_data(self) -> None: ...
