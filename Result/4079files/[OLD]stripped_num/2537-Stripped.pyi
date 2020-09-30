# (generated with --quick)

import types
from typing import Any, List, Optional, Tuple

Config: Any
CurseAPI: Any
ErrorDialog: Any
QStandardPaths: Any
Setting: Any
censor_string: Any
path: module

def format_tb(tb: Optional[types.TracebackType], limit: Optional[int] = ...) -> List[str]: ...
def getdefaultlocale(envvars: Tuple[str, ...] = ...) -> Tuple[Optional[str], Optional[str]]: ...
def handle_exception(etype, val, traceback) -> None: ...
def platform(aliased: bool = ..., terse: bool = ...) -> str: ...
def time() -> float: ...
