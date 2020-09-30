# (generated with --quick)

from typing import Any, List, Optional, Tuple, TypeVar, Union

get_console_width: Any
sys: module
time: module

_TProgressBarIterator = TypeVar('_TProgressBarIterator', bound=ProgressBarIterator)

class Animated:
    _N_PER_CYCLE: int
    _last_state: Any
    frames: Any
    n_per_cycle: Any
    def __init__(self, total = ..., frames = ..., n_per_cycle = ...) -> None: ...
    def eval(self, current) -> Any: ...

class Bar:
    after: Any
    before: Any
    total: Any
    width: Any
    def __init__(self, total, width = ..., before = ..., after = ...) -> None: ...
    def eval(self, current) -> Any: ...

class Composite:
    __doc__: str
    meters: Any
    print_format: Any
    def __init__(self, meters, print_format = ...) -> None: ...
    def eval(self, current, message = ...) -> Any: ...

class Frames:
    pacman: Tuple[str, str, str, str, str, str, str]
    ping: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
    pinwheel: Tuple[str, str, str, str, str, str, str, str]
    sticks: Tuple[str, str, str, str]

class Percentage:
    total: Any
    def __init__(self, total) -> None: ...
    def eval(self, current) -> str: ...

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
    current: Any
    meters: List[Union[Animated, Bar, Percentage, Timing]]
    print_format: str
    total: Any
    def __init__(self, total = ..., verbose = ..., show_default_message = ..., is_lying = ..., n_per_cycle = ...) -> None: ...
    def eval(self, current = ..., message = ...) -> None: ...
    def finish(self) -> None: ...
    def inc(self, amount = ..., message = ...) -> None: ...

class ProgressBarIterator:
    __doc__: str
    _iterator: Any
    _progress_bar: ProgressBar
    def __init__(self, iterable, total = ..., verbose = ..., show_default_message = ..., is_lying = ..., n_per_cycle = ...) -> None: ...
    def __iter__(self: _TProgressBarIterator) -> _TProgressBarIterator: ...
    def __next__(self) -> Any: ...

class Timing:
    _DEFAULT_FORMAT: str
    __doc__: str
    fmt: str
    print_format: Any
    start_time: Optional[float]
    total: Any
    def __init__(self, total = ..., print_format = ...) -> None: ...
    def eval(self, current) -> Any: ...
