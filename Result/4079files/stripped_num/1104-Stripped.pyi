# (generated with --quick)

from typing import Any, TypeVar, Union

BaseCommand: Any
Library: Any
Project: Any
STSIM_LIBRARY_DIRECTORY: Any
STSimConsole: Any
Scenario: Any
contrib: Any
os: module
settings: Any
transaction: Any

_AnyPath = TypeVar('_AnyPath', str, _PathLike[str])

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, name, file, *args, **options) -> None: ...

def copyfile(src: Union[str, _PathLike[str]], dst: _AnyPath, *, follow_symlinks: bool = ...) -> _AnyPath: ...
