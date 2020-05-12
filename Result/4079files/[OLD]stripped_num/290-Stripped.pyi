# (generated with --quick)

import threading
from typing import Any, Type

DEFAULT_LDAP_ALIAS: str
local: Type[threading.local]
sys: module

class ConnectionHandler(object):
    __doc__: str
    _connections: threading.local
    databases: Any
    def __getitem__(self, alias) -> Any: ...
    def __init__(self, databases) -> None: ...
    def __iter__(self) -> Any: ...
    def all(self) -> list: ...

def load_backend(backend_name) -> module: ...
