# (generated with --quick)

from typing import Any

Provider: Any
ProviderException: Any
Status: Any
arrow: Any
html: module
re: module
requests: module
tz: module
user_agents: Any

class ThunerWetter(Any):
    provider_code: str
    provider_name: str
    provider_url: str
    provider_url_temp: str
    def process_data(self) -> None: ...
