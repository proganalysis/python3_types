# (generated with --quick)

import contextlib
import kresd
from typing import Any, Callable, Dict, Iterator, Optional, Type, TypeVar

CERTS_DIR: str
ContextDecorator: Type[contextlib.ContextDecorator]
Forward: Type[kresd.`namedtuple-Forward-proto-ip-port-hostname-ca_file`]
HINTS: Dict[str, str]
Kresd: Type[kresd.Kresd]
dns: Any
kresd_tls_client: Callable[..., contextlib._GeneratorContextManager]
make_kresd: Callable[..., contextlib._GeneratorContextManager]
os: module
pytest: Any
subprocess: module
utils: module

_T = TypeVar('_T')
_TProxy = TypeVar('_TProxy', bound=Proxy)

class Proxy(contextlib.ContextDecorator):
    EXECUTABLE: str
    local_ip: Any
    local_port: Any
    proxy: Optional[subprocess.Popen[bytes]]
    upstream_ip: Any
    upstream_port: Any
    def __enter__(self: _TProxy) -> _TProxy: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __init__(self, local_ip = ..., local_port = ..., upstream_ip = ..., upstream_port = ...) -> None: ...
    def get_args(self) -> list: ...

class TLSProxy(Proxy):
    EXECUTABLE: str
    cert_path: Optional[str]
    close: Any
    force_tls13: Any
    key_path: Optional[str]
    local_ip: Any
    local_port: Any
    proxy: None
    rehandshake: Any
    upstream_ip: Any
    upstream_port: Any
    def __init__(self, local_ip = ..., local_port = ..., upstream_ip = ..., upstream_port = ..., certname = ..., close = ..., rehandshake = ..., force_tls13 = ...) -> None: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def make_port(ip = ..., ip6 = ...) -> int: ...
def resolve_hint(sock, qname) -> None: ...
