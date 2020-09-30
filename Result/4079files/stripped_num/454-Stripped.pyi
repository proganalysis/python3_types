# (generated with --quick)

from typing import Any, Awaitable, Callable, Coroutine, Match

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
    func: Any
    help: Any
    prefix: Any
    regex: Any
    roles: Any
    unsafe: Any
    def __init__(self, name, module, func, regex = ..., unsafe = ..., prefix = ..., commandhelp = ..., roles = ..., bans = ...) -> None: ...
    def try_execute(self, channel, message) -> Coroutine[Any, Any, None]: ...

def always_command(name, **kwargs) -> Callable[[Any], Any]: ...
def command(name, regex, flags = ..., **kwargs) -> Callable[[Any], Any]: ...
