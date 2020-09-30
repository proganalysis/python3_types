# (generated with --quick)

import collections
import enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Pattern, Sized, Tuple, Type, TypeVar, Union

BeatmapURLInfo = `namedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`

Enum: Type[enum.Enum]
api_key: Any
api_url: str
beatmap_url_pattern_v1: Pattern[str]
beatmap_url_pattern_v2: Pattern[str]
mode_names: Dict[str, List[str]]
re: module
requests_sent: int
ripple_pattern: Pattern[str]
ripple_url: str
utils: Any

_TMods = TypeVar('_TMods', bound=Mods)
_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode = TypeVar('_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode', bound=`namedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`)

class GameMode(enum.Enum):
    Catch: int
    Mania: int
    Standard: int
    Taiko: int
    __doc__: str
    @classmethod
    def get_mode(cls, mode) -> Optional[enum.Enum]: ...

class Mods(enum.Enum):
    AP: int
    AU: int
    Cinema: int
    DT: int
    EZ: int
    FI: int
    FL: int
    FreeModAllowed: int
    HD: int
    HR: int
    HT: int
    Key1: int
    Key2: int
    Key3: int
    Key4: int
    Key5: int
    Key6: int
    Key7: int
    Key8: int
    Key9: int
    KeyCoop: int
    KeyMod: int
    LastMod: int
    NC: int
    NF: int
    PF: int
    RD: int
    RX: int
    SD: int
    SO: int
    ScoreIncreaseMods: int
    ScoreV2: int
    TD: int
    __doc__: str
    _value_: Any
    def __new__(cls: Type[_TMods], num) -> _TMods: ...
    @classmethod
    def format_mods(cls, mods) -> str: ...
    @classmethod
    def list_mods(cls, bitwise) -> list: ...

class `namedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`(tuple):
    __slots__ = ["beatmap_id", "beatmapset_id", "gamemode"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    beatmap_id: Any
    beatmapset_id: Any
    gamemode: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`], beatmapset_id, beatmap_id, gamemode) -> `_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`: ...
    def _replace(self: `_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`, **kwds) -> `_Tnamedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`: ...

def beatmap_from_url(url, mode = ..., *, return_type = ...) -> coroutine: ...
def beatmapset_from_url(url) -> coroutine: ...
def def_section(api_name, first_element = ...) -> Callable: ...
def get_beatmaps(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_match(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_replay(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_scores(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_user(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_user_best(url = ..., request_tries = ..., **params) -> coroutine: ...
def get_user_recent(url = ..., request_tries = ..., **params) -> coroutine: ...
def lookup_beatmap(beatmaps, **lookup) -> Any: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def parse_beatmap_url(url) -> `namedtuple-BeatmapURLInfo-beatmapset_id-beatmap_id-gamemode`: ...
def rank_from_events(events, beatmap_id) -> Optional[int]: ...
def set_api_key(s) -> None: ...
