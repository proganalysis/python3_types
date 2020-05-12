# (generated with --quick)

import asyncio.futures
import enum
import musicbot.constructs
import musicbot.exceptions
from typing import Any, Coroutine, Dict, List, Type, Union

Enum: Type[enum.Enum]
ExtractionError: Type[musicbot.exceptions.ExtractionError]
LOG: logging.Logger
Serializable: Type[musicbot.constructs.Serializable]
asyncio: module
logging: module
os: module
re: module
traceback: module

class BasePlaylistEntry(musicbot.constructs.Serializable):
    __doc__: str
    _is_downloading: bool
    _waiting_futures: List[asyncio.futures.Future[nothing]]
    filename: None
    filename_thumbnail: None
    is_downloaded: bool
    def _download(self) -> Coroutine[Any, Any, nothing]: ...
    def _for_each_future(self, callback) -> None: ...
    def get_ready_future(self) -> asyncio.futures.Future[nothing]: ...

class EntryTypes(enum.Enum):
    FILE: int
    STEAM: int
    URL: int
    __doc__: str
    def __str__(self) -> Any: ...

class StreamPlaylistEntry(BasePlaylistEntry):
    __doc__: str
    _is_downloading: bool
    _waiting_futures: List[nothing]
    destination: Any
    duration: int
    filename: Any
    filename_thumbnail: None
    meta: Dict[str, Any]
    playlist: Any
    title: Any
    url: Any
    def __init__(self, playlist, url, title, *, destination = ..., **meta) -> None: ...
    def __json__(self) -> Dict[str, Union[str, Dict[str, Any]]]: ...
    @classmethod
    def _deserialize(cls, data, playlist = ...) -> Any: ...
    def _download(self, *, fallback = ...) -> coroutine: ...

class URLPlaylistEntry(BasePlaylistEntry):
    __doc__: str
    _is_downloading: bool
    _waiting_futures: List[nothing]
    download_folder: Any
    duration: Any
    expected_filename: Any
    filename: Any
    filename_thumbnail: Any
    meta: Dict[str, Any]
    playlist: Any
    start_seconds: Any
    title: Any
    url: Any
    def __init__(self, playlist, url, title, duration = ..., start_seconds = ..., expected_filename = ..., filename_thumbnail = ..., **meta) -> None: ...
    def __json__(self) -> Dict[str, Union[str, Dict[str, Any]]]: ...
    @classmethod
    def _deserialize(cls, data, playlist = ...) -> Any: ...
    def _download(self) -> Coroutine[Any, Any, None]: ...
    def _really_download(self, *, hash = ...) -> Coroutine[Any, Any, None]: ...
    def set_start(self, sec) -> bool: ...

def get_header(session, url, headerfield = ..., *, timeout = ...) -> coroutine: ...
def md5sum(filename, limit = ...) -> str: ...
