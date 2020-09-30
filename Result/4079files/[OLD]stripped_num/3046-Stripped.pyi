# (generated with --quick)

import collections
import flask.app
import flask.wrappers
import requests.models
from typing import Any, Callable, Dict, FrozenSet, Optional, Type, TypeVar
import werkzeug.exceptions

Flask: Type[flask.app.Flask]
HTTPException: Type[werkzeug.exceptions.HTTPException]
PROXY_CACHE_AGE: int
PROXY_CACHE_METHODS: FrozenSet[str]
PROXY_CACHE_STATUS_CODES: FrozenSet[int]
PROXY_CHUNK_SIZE: int
PROXY_METHODS: FrozenSet[str]
Response: Type[flask.wrappers.Response]
app: flask.app.Flask
defaultdict: Type[collections.defaultdict]
flask_restful_proxy: Callable
request: flask.wrappers.Request
requests: module

_T = TypeVar('_T')

class APIRequestProxy:
    __doc__: str
    _cache_age: None
    _enable_cache: None
    _proxy_request: None
    cache_age: Any
    chunk_size: Any
    enable_cache: Any
    headers: Any
    method: Any
    payload: Any
    proxy_request: Any
    proxy_request_cache: Optional[collections.defaultdict]
    response: Any
    status_passthrough: bool
    upstream: None
    url: Any
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @classmethod
    def initialize_cache(cls) -> None: ...
    def make_response(self) -> None: ...
    def response_from_cache(self) -> Any: ...
    def response_from_upstream(self) -> flask.wrappers.Response: ...
    def stream_response(self) -> flask.wrappers.Response: ...

class APIRequestProxyError(Exception):
    __doc__: str

class APIRequestProxyUpstream:
    __doc__: str
    _method: None
    headers: Dict[nothing, nothing]
    method: Any
    payload: None
    url: None
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def make_request(self, stream = ...) -> requests.models.Response: ...

class CacheMiss(Exception):
    __doc__: str

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def time() -> float: ...
