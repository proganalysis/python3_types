# (generated with --quick)

from typing import Any, Dict, List, Match, Optional, TextIO, Tuple, TypeVar

a: Any
am: list
arg_regex: str
argc: int
args: list
args_file: str
argsdoc: str
binding_file: TextIO
binding_template: str
colours: List[str]
coordinates: List[str]
d: Any
eargs: Any
etree: Any
f: TextIO
func: str
function_template: str
functions_file: TextIO
instruction_file: str
line: str
m: Optional[Match[str]]
opcode: int
output_binding: str
output_functions: str
parameters: List[str]
postfix: str
re: module
res: Any
sa_name: Any
sig: Tuple[str, str]
signame: str
type_names: Dict[str, Dict[str, str]]
var_names: Dict[str, str]
x: int
xpath: str

_T0 = TypeVar('_T0')

def adjust_args(args: _T0) -> _T0: ...
def arg_type(x: _T0, el) -> Tuple[str, str, Any, _T0]: ...
def check_colour(typeName, argName, doc, args, x) -> None: ...
def check_vector(typeName, argName, doc, args, x) -> None: ...
def finalize_args(args: _T0) -> _T0: ...
def impl_sig(opcode, sig) -> Tuple[str, str]: ...
def process_args(args: _T0) -> _T0: ...
