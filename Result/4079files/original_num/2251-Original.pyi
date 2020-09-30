# (generated with --quick)

from typing import Any, NoReturn

CommandNotFound: Any
ProcessExecutionError: Any
ProcessTimedOut: Any

class BaseMachine(object):
    Cmd: type
    __doc__: str
    cmd: Any
    encoding: Any
    def __contains__(self, cmd) -> bool: ...
    def daemonic_popen(self, command, cwd = ..., stdout = ..., stderr = ..., append = ...) -> NoReturn: ...
    def get(self, cmd, *othercommands) -> Any: ...

class PopenAddons(object):
    __doc__: str
    def verify(self, retcode, timeout, stdout, stderr) -> None: ...
