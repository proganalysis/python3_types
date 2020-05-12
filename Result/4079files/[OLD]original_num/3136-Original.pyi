# (generated with --quick)

import collections
from typing import Any, Callable, Coroutine, Iterable, Optional, Sized, Tuple, Type, TypeVar, Union

CachedBeatmap = `namedtuple-CachedBeatmap-url_or_id-beatmap`
ClosestPPStats = `namedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`
PPStats = `namedtuple-PPStats-pp-stars-artist-title-version`

api: Any
beatmap_path: str
cached_beatmap: `namedtuple-CachedBeatmap-url_or_id-beatmap`
host: str
logging: module
os: module
parse_options: Any
plugin_path: str
pyttanko: Any
utils: Any

_Tnamedtuple-CachedBeatmap-url_or_id-beatmap = TypeVar('_Tnamedtuple-CachedBeatmap-url_or_id-beatmap', bound=`namedtuple-CachedBeatmap-url_or_id-beatmap`)
_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version = TypeVar('_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version', bound=`namedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`)
_Tnamedtuple-PPStats-pp-stars-artist-title-version = TypeVar('_Tnamedtuple-PPStats-pp-stars-artist-title-version', bound=`namedtuple-PPStats-pp-stars-artist-title-version`)

class `namedtuple-CachedBeatmap-url_or_id-beatmap`(tuple):
    __slots__ = ["beatmap", "url_or_id"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    beatmap: Any
    url_or_id: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`], url_or_id, beatmap) -> `_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`: ...
    def _replace(self: `_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`, **kwds) -> `_Tnamedtuple-CachedBeatmap-url_or_id-beatmap`: ...

class `namedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`(tuple):
    __slots__ = ["acc", "artist", "pp", "stars", "title", "version"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str]
    acc: Any
    artist: Any
    pp: Any
    stars: Any
    title: Any
    version: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`], acc, pp, stars, artist, title, version) -> `_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`: ...
    def _replace(self: `_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`, **kwds) -> `_Tnamedtuple-ClosestPPStats-acc-pp-stars-artist-title-version`: ...

class `namedtuple-PPStats-pp-stars-artist-title-version`(tuple):
    __slots__ = ["artist", "pp", "stars", "title", "version"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str]
    artist: Any
    pp: Any
    stars: Any
    title: Any
    version: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-PPStats-pp-stars-artist-title-version`], pp, stars, artist, title, version) -> `_Tnamedtuple-PPStats-pp-stars-artist-title-version`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-PPStats-pp-stars-artist-title-version`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-PPStats-pp-stars-artist-title-version`: ...
    def _replace(self: `_Tnamedtuple-PPStats-pp-stars-artist-title-version`, **kwds) -> `_Tnamedtuple-PPStats-pp-stars-artist-title-version`: ...

def apply_settings(beatmap, args) -> Any: ...
def calculate_pp(beatmap_url_or_id, *options) -> Coroutine[Any, Any, Optional[`namedtuple-PPStats-pp-stars-artist-title-version`]]: ...
def download_beatmap(beatmap_url_or_id) -> Coroutine[Any, Any, None]: ...
def is_osu_file(url: str) -> Coroutine[Any, Any, bool]: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def parse_map(beatmap_url_or_id) -> coroutine: ...
