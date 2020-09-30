# (generated with --quick)

import click.core
import cmus_osx.env
import pathlib
import signal
from typing import Any, Callable, Dict, IO, Mapping, Optional, Sequence, Type, TypeVar, Union

CMUS_OSX_FOLDER_NAME: Any
CONFIG_NAME: Any
COULD_NOT_LOCATED_CMUS_DIRECTORY: Any
ENV: Any
ENV_VAR_PREFIX: Any
Path: Type[pathlib.Path]
RC_ENTRY_REGEX: Any
RC_SCRIPT_NAME: Any
SCRIPTS: Any
SDP_SCRIPT_NAME: Any
SIGTERM: signal.Signals
STATUS_DISPLAY_PROGRAM_REGEX: Any
click: module
config: click.core.Command
entrypoint: click.core.Group
get_cmus_instances: Any
install: click.core.Command
locate_cmus_base_path: Any
locate_editor: Any
uninstall: click.core.Command

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')

class CmusConfig:
    _CmusConfig: type
    def __new__(self: Type[CmusConfig]) -> Any: ...

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def call(args: Union[bytes, str, Sequence[Union[_PathLike, bytes, str]]], bufsize: int = ..., executable: Union[_PathLike, bytes, str] = ..., stdin: Optional[Union[int, IO]] = ..., stdout: Optional[Union[int, IO]] = ..., stderr: Optional[Union[int, IO]] = ..., preexec_fn: Callable[[], Any] = ..., close_fds: bool = ..., shell: bool = ..., cwd: Optional[Union[_PathLike, bytes, str]] = ..., env: Optional[Mapping[Union[bytes, str], Union[bytes, str]]] = ..., universal_newlines: bool = ..., startupinfo = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds = ..., timeout: Optional[float] = ...) -> int: ...
def chmod(path: Union[_PathLike, bytes, int, str], mode: int, *, dir_fd: Optional[int] = ..., follow_symlinks: bool = ...) -> None: ...
@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
def echo(message: object = ..., file: Optional[IO[str]] = ..., nl: bool = ..., err: bool = ..., color: bool = ...) -> None: ...
def kill(pid: int, sig: int) -> None: ...
def remove(path: Union[_PathLike, bytes, str], *, dir_fd: Optional[int] = ...) -> None: ...
def rename(src: Union[_PathLike, bytes, str], dst: Union[_PathLike, bytes, str], *, src_dir_fd: Optional[int] = ..., dst_dir_fd: Optional[int] = ...) -> None: ...
def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
def style(text: str, fg: Optional[str] = ..., bg: Optional[str] = ..., bold: bool = ..., dim: bool = ..., underline: bool = ..., blink: bool = ..., reverse: bool = ..., reset: bool = ...) -> str: ...
def template(env_var_prefix: str, defaults: Dict[str, cmus_osx.env.Default]) -> Optional[str]: ...
