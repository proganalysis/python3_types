# (generated with --quick)

from typing import Any, List

Colors: Any
fcntl: module
ipaddress: module
socket: module
struct: module
sys: module

class IPV4Network:
    ipList: list
    def __init__(self, CIDR: str) -> None: ...
    def getIPs(self) -> List[str]: ...

def getLocalip(interface: str = ...) -> str: ...
def ip2int(row) -> int: ...
