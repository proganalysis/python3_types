# (generated with --quick)

import requests.models
import requests.sessions
from typing import Any, Dict, Optional, TypeVar, Union

EndableThreadingClass: Any
FileCache: Any
config: Any
log: logging.Logger
logging: module
os: module
requests: module
rsession: requests.sessions.Session
tempfile: module
textextract: Any
time: module

_T1 = TypeVar('_T1')

class LargeDownload(UrlMgr, Any):
    _UrlMgr__data: Optional[str]
    _UrlMgr__request: Optional[requests.models.Response]
    _UrlMgr__size: Optional[int]
    cache: Any
    default_base_cache_dir: Any
    default_cache_class: Any
    downloaded: Any
    hooks: Any
    isResume: bool
    isStream: bool
    kwargs: Dict[str, Any]
    limit: int
    position: Any
    retries: int
    save_path: Any
    uid: int
    uids: int
    url: Any
    def apply_limit(self, elapsed_time, block_size: _T1) -> Union[int, _T1]: ...
    @staticmethod
    def best_block_size(elapsed_time, bytes) -> Any: ...
    def downloadLoop(self, streamFile) -> None: ...
    def finished_error(self) -> None: ...
    def finished_success(self) -> None: ...
    def got_requested_position(self) -> bool: ...
    def response(self) -> None: ...
    def resumeDownload(self) -> Any: ...
    def run(self) -> None: ...
    def set_resume(self) -> None: ...

class UrlMgr(object):
    _UrlMgr__data: Any
    _UrlMgr__request: Optional[requests.models.Response]
    _UrlMgr__size: Optional[int]
    cache: Any
    data: Any
    default_base_cache_dir: Any
    default_cache_class: Any
    isStream: bool
    kwargs: Dict[str, Any]
    position: int
    request: Any
    size: Any
    url: Any
    def __init__(self, url, **kwargs) -> None: ...
    def clearCache(self) -> None: ...
    def clear_connection(self) -> None: ...
    def get_data(self) -> Any: ...
    def get_rawdata(self) -> Any: ...
    def get_request(self) -> Any: ...
    def get_size(self) -> Any: ...
    def initHeader(self) -> dict: ...
    def initRequestArgs(self) -> Dict[str, Any]: ...
    def setCacheReadOnly(self) -> None: ...
    def setCacheWriteOnly(self) -> None: ...

def debug_on_httplevel() -> None: ...
def void(*dummy) -> None: ...
