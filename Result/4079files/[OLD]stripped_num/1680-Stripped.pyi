# (generated with --quick)

from typing import Any, Coroutine

ARGS_ENCODING: str
asyncio: module
enums: Any
exceptions: Any
ipaddress: module
str_utils: Any

def encode_args(args) -> bytes: ...
def negotiate_socks4_userid(reader, writer, host, port, args) -> Coroutine[Any, Any, None]: ...
def negotiate_socks5_userpass(reader, writer, host, port, args) -> Coroutine[Any, Any, None]: ...
