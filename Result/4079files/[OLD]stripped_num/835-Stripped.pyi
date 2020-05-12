# (generated with --quick)

from typing import Any, List, Optional, Tuple

ipaddress: module
os: module

class GoogleDns:
    networks: List[Tuple[Any, Any]]
    def __init__(self) -> None: ...
    def add_network(self, ip_network, location_id) -> None: ...
    def get_server(self, ip_address) -> Optional[Server]: ...

class Server:
    ip_address: Any
    location_id: Any
    def __init__(self, ip_address, location_id) -> None: ...

def create_default_google_dns() -> GoogleDns: ...
def create_google_dns_from_filename(filename) -> GoogleDns: ...
