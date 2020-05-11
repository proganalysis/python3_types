# (generated with --quick)

from typing import Any, Iterable, List, Pattern, Tuple, TypeVar

atexit: module
collections: module
datetime: module
get_home_dir: Any
glob: module
os: module
random: module
re: module
readline: module
shutil: module
string: module
subprocess: module

_TDictProperty = TypeVar('_TDictProperty', bound=DictProperty)

class BoxTable:
    ANSI_REGEX: Pattern[str]
    BOTTOM_LEFT_CHAR: str
    BOTTOM_RIGHT_CHAR: str
    BOTTOM_TEE_CHAR: str
    CROSS_CHAR: str
    HEADER_ANSI: Tuple[str, str]
    HORIZONTAL_CHAR: str
    LEFT_TEE_CHAR: str
    RIGHT_TEE_CHAR: str
    TOP_LEFT_CHAR: str
    TOP_RIGHT_CHAR: str
    TOP_TEE_CHAR: str
    VERTICAL_CHAR: str
    __doc__: str
    _lengths: List[int]
    data: List[Tuple[str, ...]]
    def __init__(self, data: List[Tuple[str, ...]]) -> None: ...
    def _format_bottom_separator(self) -> str: ...
    def _format_inside_separator(self) -> str: ...
    def _format_row(self) -> str: ...
    def _format_top_separator(self) -> str: ...
    def _get_column_lengths(self) -> List[int]: ...
    def _get_separator(self) -> List[str]: ...
    def format(self) -> str: ...

class DictProperty:
    _Proxy: type
    __doc__: Any
    _fdel: Any
    _fget: Any
    _fset: Any
    def __get__(self, obj, objtype = ...) -> Any: ...
    def __init__(self, fget = ..., fset = ..., fdel = ..., doc = ...) -> None: ...
    def deleter(self: _TDictProperty, fdel) -> _TDictProperty: ...
    def getter(self: _TDictProperty, fget) -> _TDictProperty: ...
    def setter(self: _TDictProperty, fset) -> _TDictProperty: ...

class FactoryDict(collections.defaultdict):
    __doc__: str
    def __missing__(self, key) -> Any: ...

class ProgressBar:
    __doc__: str
    coverage: float
    empty_char: Any
    fill_char: Any
    left_char: Any
    message: Any
    r_align: Any
    right_char: Any
    def __init__(self, coverage: float, message = ..., r_align = ..., fill_char = ..., empty_char = ..., left_char = ..., right_char = ...) -> None: ...
    def update(self, fill_amount: float) -> None: ...

def contract_user(path: str) -> str: ...
def get_path_ancestry(paths: Iterable[str]) -> List[str]: ...
def secure_string(length: int) -> str: ...
def set_no_autocomplete() -> None: ...
def set_path_autocomplete() -> None: ...
def shell_cmd(input_cmd: list) -> subprocess.Popen: ...
def timestamp_path(path: str, keyword = ...) -> str: ...
