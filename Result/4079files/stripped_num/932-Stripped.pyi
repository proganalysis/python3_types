# (generated with --quick)

import pathlib
import subprocess
from typing import Any, List, Match, Optional, TextIO, Type

Path: Type[pathlib.Path]
addr: str
argparse: module
args: argparse.Namespace
codeline: str
dbgline: str
debugdata: List[str]
f: TextIO
filepath: pathlib.Path
info: str
lineno: str
m: Optional[Match[str]]
module_name: Optional[str]
os: module
output: str
p: subprocess.CompletedProcess[bytes]
parser: argparse.ArgumentParser
path: str
prev_output: Optional[str]
projectdir: pathlib.Path
re: module
show_type: str
sp: module
sys: module
text: str

def clamp_len(text, minlen, maxlen) -> Any: ...
def get_funcname(addr) -> Optional[str]: ...
