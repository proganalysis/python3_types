# (generated with --quick)

import time
from typing import Any, Coroutine, Optional, Tuple, Union
import urllib.parse

CacheBackend: Any
S3_ACCESS_KEY: Optional[str]
S3_BUCKET: str
S3_REGION: Optional[str]
S3_SECRET_KEY: Optional[str]
S3_SERVER: str
asyncio: module
certifi: module
io: module
minio: Any
os: module
urllib3: module

class S3Cache(Any):
    client: Any
    def __init__(self) -> None: ...
    def _filename(self, url, format) -> str: ...
    def get(self, key, format = ...) -> coroutine: ...
    def modified_since(self, key, format = ...) -> Coroutine[Any, Any, Optional[float]]: ...
    def set(self, key, payload, ttl = ..., format = ...) -> None: ...

def mktime(t: Union[time.struct_time, Tuple[int, int, int, int, int, int, int, int, int]]) -> float: ...
@overload
def quote_plus(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote_plus(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
