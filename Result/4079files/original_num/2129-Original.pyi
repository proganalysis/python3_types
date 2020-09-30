# (generated with --quick)

from typing import Any, Coroutine, Pattern, Set, Type

COLOR_COMPILE_FAIL: Any
COLOR_RUN_FAIL: Any
COLOR_RUN_SUCCESS: Any
Color: Any
FILE_EXTENSION_RE: Pattern[str]
MChannel: Any
MHandler: Any
MRoleType: Any
Message: Any
aiohttp: Any
command: Any
logger: logging.Logger
logging: module
master: Any
re: module
runcode_command: Any
runcode_file_command: Any

class MCodeHandler(Any):
    languages: Set[nothing]
    def __init__(self) -> None: ...
    def execute(self, code: str, channel, message) -> Coroutine[Any, Any, None]: ...

def codehandler(handler: Type[MCodeHandler]) -> Type[MCodeHandler]: ...
def try_execute(code: str, language: str, channel, message) -> Coroutine[Any, Any, bool]: ...
