# (generated with --quick)

from typing import Any, Dict, Iterable, Iterator, List, Tuple, TypeVar, Union

WindowInfo = Dict[AnyStr, Union[int, AnyStr]]

CGWindowListCopyWindowInfo: Any
USER_OPTIONS: int
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

def build_option_bitmask(*opts: Iterable[str]) -> int: ...
def gen_ids_from_info(windows: Iterable[Dict[AnyStr, Union[int, AnyStr]]]) -> Iterator[Tuple[int, str, str]]: ...
def gen_window_ids(parent: str, title: str = ..., options: str = ..., relative_to: bool = ...) -> Iterator[int]: ...
def get_window_info(options: int = ..., relative_to: int = ...) -> List[Dict[AnyStr, Union[int, AnyStr]]]: ...
def print_window_ids(windows) -> None: ...
