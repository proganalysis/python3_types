# (generated with --quick)

from typing import Any, Dict, Generator, Tuple, TypeVar, Union

WindowInfo = Dict[AnyStr, Union[int, AnyStr]]

CGWindowListCopyWindowInfo: Any
USER_OPTIONS: Any
USER_OPTS_STR: str
WINDOW_OPTIONS: Dict[str, Any]
ex: ImportError
kCGNullWindowID: Any
kCGWindowListExcludeDesktopElements: Any
kCGWindowListOptionAll: Any
kCGWindowListOptionIncludingWindow: Any
kCGWindowListOptionOnScreenAboveWindow: Any
kCGWindowListOptionOnScreenBelowWindow: Any
kCGWindowListOptionOnScreenOnly: Any
kCGWindowName: Any
kCGWindowNumber: Any
kCGWindowOwnerName: Any

AnyStr = TypeVar('AnyStr', str, bytes)

def build_option_bitmask(*opts) -> Any: ...
def gen_ids_from_info(windows) -> Generator[Tuple[Any, Any, Any], Any, None]: ...
def gen_window_ids(parent, title = ..., options = ..., relative_to = ...) -> Generator[Any, Any, None]: ...
def get_window_info(options = ..., relative_to = ...) -> Any: ...
def print_window_ids(windows) -> None: ...
