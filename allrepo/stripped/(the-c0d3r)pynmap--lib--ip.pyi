# (generated with --quick)

from typing import Any, List, Optional

Colors: Any
fcntl: module
ipaddress: module
socket: module
struct: module
sys: module

class IPV4Network:
    ipList: list
    def __init__(self, CIDR) -> None: ...
    def getIPs(self) -> List[str]: ...

def getLocalip(interface = ...) -> Optional[str]: ...
def ip2int(row) -> int: ...
