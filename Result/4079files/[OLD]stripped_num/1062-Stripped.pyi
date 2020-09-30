# (generated with --quick)

import click.core
import itertools
from typing import Any, Generator, Tuple, Type, TypeVar, Union

COMMAND: str
FILE_EXT: str
IMG_TYPES: Tuple[str, str, str, str]
STATUS_FAIL: int
STATUS_OK: int
USER_OPTS_STR: Any
WINDOW_OPTIONS: Any
chain: Type[itertools.chain]
click: module
datetime: Type[datetime.datetime]
gen_window_ids: Any
run: click.core.Command

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

class ScreencaptureEx(Exception): ...

def gen_windows(application_name, title, window_selection_options) -> Generator[Any, Any, None]: ...
def get_filename(*args) -> str: ...
def getstatusoutput(cmd: Union[bytes, str]) -> Tuple[int, str]: ...
def screenshot_window(application_name, title = ..., filename: _T2 = ..., window_selection_options = ..., options = ...) -> Union[str, _T2]: ...
def screenshot_windows(application_name, title = ..., window_selection_options = ..., options = ...) -> Generator[str, Any, None]: ...
def take_screenshot(window, filename: _T1, options = ...) -> _T1: ...
