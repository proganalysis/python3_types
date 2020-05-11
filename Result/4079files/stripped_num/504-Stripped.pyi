# (generated with --quick)

import requests.models
from typing import Any, Dict, TypeVar

_HEADERS: Dict[str, str]
requests: module

_T0 = TypeVar('_T0')

class GraknError(Exception):
    __doc__: str

class Graph:
    DEFAULT_URI: str
    __doc__: str
    keyspace: Any
    uri: Any
    def __init__(self, uri = ..., keyspace = ...) -> None: ...
    def _params(self, *, infer: _T0) -> Dict[str, Any]: ...
    def _post(self, query, *, infer) -> requests.models.Response: ...
    def _url(self) -> str: ...
    def execute(self, query, *, infer = ...) -> Any: ...
