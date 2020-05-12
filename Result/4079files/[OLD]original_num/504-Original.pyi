# (generated with --quick)

import requests.models
from typing import Any, Dict

_HEADERS: Dict[str, str]
requests: module

class GraknError(Exception):
    __doc__: str

class Graph:
    DEFAULT_URI: str
    __doc__: str
    keyspace: str
    uri: str
    def __init__(self, uri: str = ..., keyspace: str = ...) -> None: ...
    def _params(self, *, infer: bool) -> Dict[str, Any]: ...
    def _post(self, query: str, *, infer: bool) -> requests.models.Response: ...
    def _url(self) -> str: ...
    def execute(self, query: str, *, infer: bool = ...) -> Any: ...
