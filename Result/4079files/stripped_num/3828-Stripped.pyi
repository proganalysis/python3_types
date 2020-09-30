# (generated with --quick)

import jinja2.environment
import jinja2.loaders
import pathlib
from typing import Callable, Iterable, Iterator, List, Optional, TextIO, Tuple, Type

Environment: Type[jinja2.environment.Environment]
FileSystemLoader: Type[jinja2.loaders.FileSystemLoader]
Path: Type[pathlib.Path]
TARGET: str
env: jinja2.environment.Environment
f: TextIO
rendered: str
sys: module
template: jinja2.environment.Template

def make_breadcrumb(target) -> Iterator[Tuple[Optional[str], str]]: ...
def make_children(target) -> List[pathlib.Path]: ...
def select_autoescape(enabled_extensions: Iterable[str] = ..., disabled_extensions: Iterable[str] = ..., default_for_string: bool = ..., default: bool = ...) -> Callable[[str], bool]: ...
