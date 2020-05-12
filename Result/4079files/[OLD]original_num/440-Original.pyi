# (generated with --quick)

from typing import Any, Tuple, Type, TypeVar

c_long: Type[ctypes.c_long]
c_ulong: Type[ctypes.c_ulong]
ctypes: module
fcntl: module
gHandle: Any
os: module
platform: module
struct: module
sys: module
termios: module
time: module

_T0 = TypeVar('_T0')

class TopologyProgressBar(object):
    __doc__: str
    hidden: Any
    rest_client: Any
    term_width: Any
    type: Any
    def __init__(self, rest_client, type, hidden = ...) -> None: ...
    def _report_progress(self, perc_complete, cur_bucket, total_buckets, bucket_name, remaining) -> None: ...
    def show(self) -> Any: ...

def bold(text: _T0) -> _T0: ...
def get_terminal_width() -> Tuple[Any, Any, Any, Any]: ...
def move_cursor_absolute_x(cols) -> None: ...
def move_cursor_relative_y(rows) -> None: ...
