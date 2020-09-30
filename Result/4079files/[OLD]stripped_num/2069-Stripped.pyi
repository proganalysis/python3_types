# (generated with --quick)

import http.client
import numpy
from typing import Any, Callable, IO, List, Mapping, Optional, Sequence, Tuple, Union

dataset_url: str
img_to_array: Any
load_img: Any
np: module
os: module

def call(args: Union[bytes, str, Sequence[Union[_PathLike, bytes, str]]], bufsize: int = ..., executable: Union[_PathLike, bytes, str] = ..., stdin: Optional[Union[int, IO]] = ..., stdout: Optional[Union[int, IO]] = ..., stderr: Optional[Union[int, IO]] = ..., preexec_fn: Callable[[], Any] = ..., close_fds: bool = ..., shell: bool = ..., cwd: Optional[Union[_PathLike, bytes, str]] = ..., env: Optional[Mapping[Union[bytes, str], Union[bytes, str]]] = ..., universal_newlines: bool = ..., startupinfo = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds = ..., timeout: Optional[float] = ...) -> int: ...
def download() -> None: ...
def load_data() -> Tuple[Tuple[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray], List[str]]: ...
def urlretrieve(url: str, filename: Optional[Union[_PathLike, str]] = ..., reporthook: Optional[Callable[[int, int, int], None]] = ..., data: Optional[bytes] = ...) -> Tuple[str, http.client.HTTPMessage]: ...
