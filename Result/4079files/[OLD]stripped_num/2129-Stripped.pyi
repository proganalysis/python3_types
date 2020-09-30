# (generated with --quick)

from typing import Any, Coroutine, Pattern, Set, TypeVar

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

_T0 = TypeVar('_T0')

class MCodeHandler(Any):
    languages: Set[nothing]
    def __init__(self) -> None: ...
    def execute(self, code, channel, message) -> Coroutine[Any, Any, nothing]: ...

def codehandler(handler: _T0) -> _T0: ...
def try_execute(code, language, channel, message) -> Coroutine[Any, Any, bool]: ...
