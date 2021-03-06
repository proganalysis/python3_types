# (generated with --quick)

from typing import Any, NoReturn, Optional, Set, Tuple

`TypeVar`: Any
_implicit_globals: Set[module]
_tpvar_is_class: bool
datetime: module
force: bool
imp: module
in_file: str
indent: str
inspect: module
os: module
out_file: Optional[str]
pkg_resources: module
py3: bool
pytypes: Any
silent: bool
stub_descr: Tuple[str, str, int]
stub_open_mode: str
sys: module
type_util: Any
typelogger: Any
util: Any

def _class_get_line(clss) -> int: ...
def _func_get_line(func) -> Any: ...
def _print(line) -> None: ...
def _typecomment(_types, argspec, slf_or_clsm = ..., assumed_globals = ...) -> str: ...
def _typestring(_types, argspecs, slf_or_clsm = ..., assumed_globals = ...) -> Any: ...
def _write_TypeVar(tpv, lines, inc = ...) -> None: ...
def _write_class(clss, lines, inc = ..., assumed_globals = ..., implicit_globals = ..., assumed_typevars = ...) -> None: ...
def _write_func(func, lines, inc = ..., decorators = ..., slf_or_clsm = ..., assumed_globals = ...) -> None: ...
def _write_property(prop, lines, inc = ..., decorators = ..., assumed_globals = ...) -> None: ...
def annotated_signature(func, argspec = ..., slf_or_clsm = ..., assumed_globals = ...) -> str: ...
def convert(in_file, out_file = ...) -> None: ...
def err_no_in_file() -> NoReturn: ...
def main() -> None: ...
def print_usage() -> None: ...
def signature(func) -> str: ...
def typecomment(func, argspec = ..., slf_or_clsm = ..., assumed_globals = ...) -> str: ...
