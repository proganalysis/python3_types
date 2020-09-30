# (generated with --quick)

from typing import Any, Generator, Iterable, Iterator, Optional, Tuple, TypeVar

IP: Any
IPAddress: Any
IPv4Address: Any
IPv4Network: Any
IPv6Address: Any
IPv6Network: Any
Subnet: Any
and_: Any
cast: Any
func: Any
session: Any
sys: module

_T = TypeVar('_T')

class MacExistsException(Exception):
    def __init__(self) -> None: ...

class SubnetFullException(Exception):
    def __init__(self) -> None: ...

def get_free_ip(subnets) -> Tuple[Any, Any]: ...
def get_subnet_unused_ips(subnet) -> Generator[Any, Any, None]: ...
def get_subnets_for_room(room) -> list: ...
def get_subnets_with_usage() -> list: ...
def get_unused_ips(subnets) -> dict: ...
@overload
def islice(iterable: Iterable[_T], start: Optional[int], stop: Optional[int], step: Optional[int] = ...) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], stop: Optional[int]) -> Iterator[_T]: ...
def ptr_name(network, ip_address) -> str: ...
