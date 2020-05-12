# (generated with --quick)

import click.core
import click.exceptions
import click.types
from typing import Any, Callable, Optional, Type, TypeVar, Union

Abort: Type[click.exceptions.Abort]
ClickException: Type[click.exceptions.ClickException]
DEFAULT_PATH_KWARGS: dict
LOCAL_REPOSITORY_PATH: str
LOCK_PATH: str
PREVIEW_PATH: str
PUBLISH_PATH: str
Path: Type[click.types.Path]
REPOSITORY_PATH: str
SITE_NAME: str
WIPE_PROMPT: str
WikiRepo: Any
click: module
compile_wiki: Any
get: click.core.Command
git: Any
init: click.core.Command
main: click.core.Group
os: module
pass_config: Callable[[Any], Any]
preview: click.core.Command
publish: click.core.Command
stat: module
subprocess: module
sync: click.core.Command

AnyStr = TypeVar('AnyStr', str, bytes)

class Config:
    author_email: str
    author_name: Optional[str]
    local_repo_path: str
    preview_path: str
    publish_path: str
    repo_path: str
    site_name: str
    def __init__(self) -> None: ...

def _on_create(file_path: str) -> None: ...
def _preview(preview_path, local_repo_path) -> None: ...
def clear_directory(path: str) -> None: ...
def expanduser(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
