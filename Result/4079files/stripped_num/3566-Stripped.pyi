# (generated with --quick)

from typing import Any

Provider: Any
ProviderException: Any
Status: Any
arrow: Any
get_logger: Any
io: module
json: module
logger: Any
path: module
requests: module

class MeteoSwiss(Any):
    provider_code: str
    provider_name: str
    provider_url: str
    def process_data(self) -> None: ...
