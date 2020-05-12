# (generated with --quick)

from typing import Any, Awaitable, Callable, Coroutine, Match, Optional, Pattern, Union

CommandType = Callable[[Any, Match, Any], Awaitable[None]]

MChannel: Any
MHandler: Any
MRoleType: Any
Message: Any
asyncio: module
bantypes: Any
chatlogger: logging.Logger
logger: logging.Logger
logging: module
random: module
re: module

class MCommand(Any):
    func: Callable[[Any, Match[Union[bytes, str]], Any], Awaitable[None]]
    help: Optional[str]
    prefix: bool
    prefix_re: Optional[Pattern]
    regex: Optional[Pattern[Union[bytes, str]]]
    roles: Optional[list]
    unsafe: bool
    def __init__(self, name: str, module: str, func: Callable[[Any, Match, Any], Awaitable[None]], regex: Optional[Pattern] = ..., unsafe: bool = ..., prefix: bool = ..., commandhelp: Optional[str] = ..., roles: Optional[list] = ..., bans: Optional[list] = ...) -> None: ...
    def try_execute(self, channel, message) -> Coroutine[Any, Any, None]: ...

def always_command(name: str, **kwargs) -> Callable[[Callable[[Any, Match, Any], Awaitable[None]]], Callable[[Any, Match, Any], Awaitable[None]]]: ...
def command(name: str, regex: str, flags: int = ..., **kwargs) -> Callable[[Callable[[Any, Match, Any], Awaitable[None]]], Callable[[Any, Match, Any], Awaitable[None]]]: ...
