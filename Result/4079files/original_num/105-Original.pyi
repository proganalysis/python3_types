# (generated with --quick)

import io
from typing import Any, Dict, List, Tuple, Type, TypeVar

StringIO: Type[io.StringIO]
defines: Dict[str, str]
log: logging.Logger
logging: module
os: module
re: module
subprocess: module
tempfile: module

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')

def perl_preproc(data) -> Tuple[str, List[int]]: ...
def preproc(filename, perl_pp_enabled) -> Tuple[str, list]: ...
def verilog_preproc(data, line_infos: _T1, perl_pp_enabled) -> Tuple[str, _T1]: ...
def verilog_preproc_line(i, line, ifs: _T2, line_info: _T3, perl_pp_enabled) -> Tuple[Any, Any, Any]: ...
