# (generated with --quick)

import collections
from typing import Any, Optional, Pattern, Type, TypeVar
import urllib.parse

CHANNEL_NAMES: collections.OrderedDict[nothing, nothing]
OrderedDict: Type[collections.OrderedDict]
PLAYLIST_LINK: str
PLAYLIST_TYPE_CHANNEL: str
PLAYLIST_TYPE_EPISODE: str
PORADY_PATH_PATTERN: Pattern[str]
__version__: str
docopt: Any
etree: Any
logging: module
m3u8: Any
re: module
requests: module
shlex: module
subprocess: module
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

def get_ivysilani_playlist(url, quality) -> Any: ...
def get_live_playlist(channel, quality) -> Any: ...
def get_playlist(playlist_id, playlist_type, quality) -> Any: ...
def main() -> None: ...
def parse_quality(value) -> int: ...
def play(options) -> None: ...
def run_player(playlist, player_cmd) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
@overload
def urlsplit(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResult: ...
@overload
def urlsplit(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResultBytes: ...
