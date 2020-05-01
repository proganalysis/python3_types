# (generated with --quick)

from typing import Any, Dict, Optional, Union

ALLE_MEINE_ENTCHEN: Dict[str, Union[int, list]]
HAPPY_BIRTHDAY: Dict[str, Union[int, list]]
TRIAS: Dict[str, Union[int, list]]
datetime: module
ev3: Any
jukebox: Jukebox
now: str
numbers: module
songs: Any
task: Any
time: module

class Jukebox(Any):
    __doc__: str
    _pos_color: None
    _pos_led: Any
    _pos_tone: Optional[int]
    _temperament: int
    _volume: int
    temperament: Any
    verbosity: int
    volume: Any
    def __init__(self, protocol = ..., host = ..., ev3_obj = ...) -> None: ...
    def _init_color(self) -> None: ...
    def _init_tone(self) -> None: ...
    def _next_color(self, song) -> None: ...
    def _next_tone(self, song) -> int: ...
    def change_color(self, led_pattern) -> None: ...
    def play_tone(self, tone, duration = ...) -> None: ...
    def song(self, song) -> Any: ...
    def sound(self, path, duration = ..., repeat = ...) -> Any: ...
    def stop(self) -> None: ...
