# (generated with --quick)

import asyncio.streams
from typing import Any, Coroutine, Dict, Optional, Union

ARGS_ENCODING: str
asyncio: module
enums: Any
exceptions: Any
ipaddress: module
str_utils: Any

def encode_args(args: Dict[str, str]) -> bytes: ...
def negotiate_socks4_userid(reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter, host: Union[str, ipaddress.IPv4Address, ipaddress.IPv6Address], port: int, args: Optional[Dict[str, str]]) -> Coroutine[Any, Any, None]: ...
def negotiate_socks5_userpass(reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter, host: Union[str, ipaddress.IPv4Address, ipaddress.IPv6Address], port: int, args: Optional[Dict[str, str]]) -> Coroutine[Any, Any, None]: ...
