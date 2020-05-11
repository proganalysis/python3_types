# (generated with --quick)

import ssl
import subprocess
from typing import Any, List, Optional, Type, Union
import urllib.request

AppHelper: Any
BeautifulSoup: Any
NSApplication: Any
NSEventTrackingRunLoopMode: Any
NSMenu: Any
NSMenuItem: Any
NSRunLoop: Any
NSStatusBar: Any
NSTimer: Any
PIPE: int
Popen: Type[subprocess.Popen]
Request: Type[urllib.request.Request]
logger: logging.Logger
logging: module
random: module
re: module

class Pyet(Any):
    QUIT: Any
    SEPERATOR: Any
    __doc__: str
    curr_track_hash: int
    lyrics: List[str]
    menuBar: Any
    next_track_hash: int
    statusItem: Any
    timer: Any
    def doNothing_(self, sender) -> None: ...
    def finishLaunching(self) -> None: ...
    def update_(self, timer) -> None: ...

def get_current_track() -> dict: ...
def get_lyrics(artist: str, song_title: str) -> str: ...
def main() -> None: ...
def urlopen(url: Union[str, urllib.request.Request], data: Optional[bytes] = ..., timeout: Optional[float] = ..., *, cafile: Optional[str] = ..., capath: Optional[str] = ..., cadefault: bool = ..., context: Optional[ssl.SSLContext] = ...) -> Any: ...
