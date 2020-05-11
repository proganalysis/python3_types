# (generated with --quick)

from typing import Any, List, Optional, Tuple, TypeVar, Union

EIO: int
cruft: Union[str, List[str]]
os: module
pty: module
selectors: module
subprocess: module
sys: module
time: module
tool: InteractivePTY

_T0 = TypeVar('_T0')

class InteractivePTY(object):
    __doc__: str
    _encoding: Any
    _exit_cmd: Any
    _prompt: Any
    _raw_buffer: Any
    _tool: Any
    _tool_args: Any
    master: int
    proc: subprocess.Popen[bytes]
    proc_rc: Optional[int]
    sel: selectors.SelectSelector
    slave: int
    def __del__(self) -> None: ...
    def __init__(self, tool, prompt, exit_cmd, args = ..., encoding = ...) -> None: ...
    @staticmethod
    def _parse_marker(marker: _T0, data) -> Tuple[Optional[_T0], Any, Any]: ...
    def close(self) -> None: ...
    def cmd(self, cmd, marker = ..., as_string = ..., timeout = ..., trim_cmd = ..., add_crlf = ...) -> Any: ...
    def first_prompt(self) -> Any: ...
    def get_data(self, marker = ..., timeout = ...) -> Tuple[Any, Any]: ...
    def run_script(self, script) -> list: ...
    def send_data(self, data, add_crlf = ...) -> Any: ...
    def sync_prompt(self) -> bool: ...

class PtyTimeoutError(Exception): ...
