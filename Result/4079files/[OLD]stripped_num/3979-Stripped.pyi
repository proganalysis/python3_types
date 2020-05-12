# (generated with --quick)

import __future__
from typing import Any, Dict, List, Optional, Pattern, TextIO, Tuple, TypeVar, Union

aref2_re: Pattern[str]
aref_re: Pattern[str]
args: List[Optional[str]]
contents: str
doc: str
docs: Dict[str, str]
ih: TextIO
indented_span_re: Pattern[str]
item: str
items: Dict[str, Optional[Tuple[str, int, str]]]
oh: TextIO
os: module
print_function: __future__._Feature
r: str
re: module
replacement: str
replacements: Dict[str, str]
s: str
shutil: module
standardese_path: Optional[str]
subprocess: module
sys: module

_T0 = TypeVar('_T0')

def repair_verbatims(content) -> Any: ...
def section(item) -> str: ...
def strip_arefs(content, item) -> Any: ...
def strip_indent_before_spans(content) -> Any: ...
def title(item) -> str: ...
def weight(item) -> str: ...
def which(program: _T0) -> Optional[Union[str, _T0]]: ...
