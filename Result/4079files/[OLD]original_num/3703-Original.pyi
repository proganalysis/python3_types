# (generated with --quick)

from typing import Any, Callable, Coroutine, List, Match, Pattern, TypeVar, Union

AsyncIOScheduler: Any
BunkBot: Any
BunkException: Any
BunkUser: Any
Channel: Any
Duel: Any
Embed: Any
ProgressBar: Any
USER_NAME_REGEX: Any
asyncio: module
calc_req_xp: Any
command: Any
database: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class BunkRPG:
    accept: Any
    bot: Any
    cancel: Any
    duel: Any
    duels: List[nothing]
    leader: Any
    level: Any
    reject: Any
    def __init__(self, bot) -> None: ...
    def check_decayed_xp(self) -> Coroutine[Any, Any, None]: ...
    def ding(self, member, value, channel = ...) -> Coroutine[Any, Any, None]: ...
    def wire_decay_check(self) -> Coroutine[Any, Any, None]: ...

def setup(bot) -> None: ...
def sub(pattern: Union[Pattern[AnyStr], AnyStr], repl: Union[Callable[[Match[AnyStr]], AnyStr], AnyStr], string: AnyStr, count: int = ..., flags: int = ...) -> AnyStr: ...
