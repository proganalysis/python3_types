# (generated with --quick)

import click.core
import itertools
from typing import Any, Iterator, List, Optional, Tuple, Type, Union

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

class ScreencaptureEx(Exception): ...

def gen_windows(application_name: str, title: str, window_selection_options: str) -> Iterator[int]: ...
def get_filename(*args) -> str: ...
def getstatusoutput(cmd: Union[bytes, str]) -> Tuple[int, str]: ...
def screenshot_window(application_name: str, title: str = ..., filename: str = ..., window_selection_options: str = ..., options: Optional[List[str]] = ...) -> str: ...
def screenshot_windows(application_name: str, title: str = ..., window_selection_options: str = ..., options: Optional[List[str]] = ...) -> Iterator[str]: ...
def take_screenshot(window: int, filename: str, options: Optional[List[str]] = ...) -> str: ...
