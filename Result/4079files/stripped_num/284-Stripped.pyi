# (generated with --quick)

import foomodules.Base
from typing import Any, Callable, Dict, List, Tuple, Type

Base: module
datetime: Type[datetime.datetime]
itertools: module
logging: module
random: module
time: module
timedelta: Type[datetime.timedelta]

class EachDay(RepeatingTimer):
    _at: Tuple[nothing, ...]
    _do: List[nothing]
    _loaded: bool
    _uid: str
    def __init__(self, at = ..., **kwargs) -> None: ...
    def _calc_next_trigger(self) -> datetime.datetime: ...

class EveryInterval(RepeatingTimer):
    _do: List[nothing]
    _loaded: bool
    _uid: str
    seconds: Any
    def __init__(self, interval, **kwargs) -> None: ...
    def _calc_next_trigger(self) -> datetime.datetime: ...

class RateLimitService(EveryInterval):
    _do: List[Callable[[], Any]]
    _loaded: bool
    _uid: str
    cmds_per_minute: Any
    limit_dict: Dict[Tuple[str, Any], Any]
    seconds: int
    warning_message: Any
    warning_messages: Any
    def __init__(self, cmds_per_minute, warning_messages = ..., **kwargs) -> None: ...
    def _decrease(self) -> None: ...
    def check_and_count(self, msg) -> bool: ...

class RepeatingTimer(Timer):
    _do: List[nothing]
    _loaded: bool
    _uid: str
    def __init__(self, **kwargs) -> None: ...
    def _load(self) -> None: ...
    def _on_timer(self) -> None: ...

class Timer(foomodules.Base.XMPPObject):
    _do: Any
    _uid: str
    def __init__(self, do = ..., **kwargs) -> None: ...
