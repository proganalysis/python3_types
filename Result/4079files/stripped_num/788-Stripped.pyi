# (generated with --quick)

import contextlib
from typing import Any, Callable, IO, Iterator, Optional, TypeVar, Union

lkworkspace: Callable[..., contextlib._GeneratorContextManager]
log: module
make_commandfile: Callable[..., contextlib._GeneratorContextManager]
os: module
run_logged: Any

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def debspawn_run_commandfile(jlog, suite, arch, build_dir, artifacts_dir, command_script, header = ..., allow_dev_access = ...) -> Any: ...
