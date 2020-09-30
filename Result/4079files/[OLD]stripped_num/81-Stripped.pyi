# (generated with --quick)

from typing import Any, Dict, Tuple

BaseHTTPUpdater: Any
logger: logging.Logger
logging: module
requests: module

class DuckDNSUpdater(Any):
    __doc__: str
    _api_url: str
    _domains: None
    _token: None
    info_code: Dict[str, str]
    def __init__(self, domains, token, *args, **kwargs) -> None: ...
    def build_payload(self) -> Any: ...
    def parse_result(self, response) -> Tuple[bool, Any]: ...
