# (generated with --quick)

import subprocess
from typing import Any, Callable, IO, List, Mapping, Optional, Sequence, TextIO, Tuple, Type, Union

PIPE: int
Popen: Type[subprocess.Popen]
QtCore: Any
QtGui: Any
cgi: module
dirstack: List[str]
dummy: None
f: TextIO
file: Any
form: cgi.FieldStorage
hostdir: str
json: module
loc: str
local: str
os: module
picsdir: str
shlex: module
shutil: module
success: bool
sys: module
time: module

def call(args: Union[bytes, str, Sequence[Union[_PathLike, bytes, str]]], bufsize: int = ..., executable: Union[_PathLike, bytes, str] = ..., stdin: Optional[Union[int, IO]] = ..., stdout: Optional[Union[int, IO]] = ..., stderr: Optional[Union[int, IO]] = ..., preexec_fn: Callable[[], Any] = ..., close_fds: bool = ..., shell: bool = ..., cwd: Optional[Union[_PathLike, bytes, str]] = ..., env: Optional[Mapping[Union[bytes, str], Union[bytes, str]]] = ..., universal_newlines: bool = ..., startupinfo = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds = ..., timeout: Optional[float] = ...) -> int: ...
def clean(newdir, maxlen) -> str: ...
def create_html_head() -> None: ...
def create_html_output_dirs() -> None: ...
def create_html_output_pics(pdir) -> None: ...
def create_html_output_rd_fail() -> None: ...
def run_program(rcmd) -> Optional[Union[str, Tuple[bytes, bytes]]]: ...
def save_uploaded_file(tdir) -> Tuple[bool, Any]: ...
def scan_directories() -> None: ...
def upload() -> None: ...
