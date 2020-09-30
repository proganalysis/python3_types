# (generated with --quick)

from typing import Any, List, Optional, Tuple, TypeVar

get_console_width: Any
sys: module
time: module

_TProgressBarIterator = TypeVar('_TProgressBarIterator', bound=ProgressBarIterator)

class Animated:
    _N_PER_CYCLE: int
    _last_state: int
    frames: List[str]
    n_per_cycle: Any
    def __init__(self, total: Optional[int] = ..., frames: List[str] = ..., n_per_cycle: Optional[int] = ...) -> None: ...
    def eval(self, current: Optional[int]) -> str: ...

class Bar:
    after: str
    before: str
    total: int
    width: int
    def __init__(self, total: int, width: int = ..., before: str = ..., after: str = ...) -> None: ...
    def eval(self, current: int) -> str: ...

class Composite:
    __doc__: str
    meters: list
    print_format: str
    def __init__(self, meters: list, print_format: Optional[str] = ...) -> None: ...
    def eval(self, current: Optional[int], message: str = ...) -> str: ...

class Frames:
    pacman: Tuple[str, str, str, str, str, str, str]
    ping: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
    pinwheel: Tuple[str, str, str, str, str, str, str, str]
    sticks: Tuple[str, str, str, str]

class Percentage:
    total: int
    def __init__(self, total: int) -> None: ...
    def eval(self, current: int) -> str: ...

class ProgressBar(Composite):
    _FIRST_MESSAGE_TIME: int
    _METERS_LEN: int
    _SAFE_MARGIN: int
    _SECOND_MESSAGE_TIME: int
    _THIRD_MESSAGE_TIME: int
    __doc__: str
    _is_lying: Any
    _show_default_message: Any
    _start_time: Optional[float]
    _verbose: Any
    _width: Any
    current: Optional[int]
    meters: list
    print_format: Any
    total: Any
    def __init__(self, total = ..., verbose = ..., show_default_message = ..., is_lying = ..., n_per_cycle = ...) -> None: ...
    def eval(self, current: Optional[int] = ..., message: str = ...) -> None: ...
    def finish(self) -> None: ...
    def inc(self, amount: int = ..., message: str = ...) -> None: ...

class ProgressBarIterator:
    __doc__: str
    _iterator: Any
    _progress_bar: ProgressBar
    def __init__(self, iterable, total: Optional[int] = ..., verbose: bool = ..., show_default_message: bool = ..., is_lying: bool = ..., n_per_cycle: Optional[int] = ...) -> None: ...
    def __iter__(self: _TProgressBarIterator) -> _TProgressBarIterator: ...
    def __next__(self) -> Any: ...

class Timing:
    _DEFAULT_FORMAT: str
    __doc__: str
    fmt: str
    print_format: str
    start_time: Optional[float]
    total: Any
    def __init__(self, total: Optional[int] = ..., print_format: str = ...) -> None: ...
    def eval(self, current: Optional[int]) -> str: ...
