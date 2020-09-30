# (generated with --quick)

import __builtin__
from typing import Any, Callable, Dict, Iterable, Set, Sized, Tuple, Type, TypeVar

Var = `namedtuple-Var-name-type-default-help-flags-filename`

CONFLICTS: collections.defaultdict[str, Any]
VARS: Dict[str, `namedtuple-Var-name-type-default-help-flags-filename`]
VarType: Any
ast: module
collections: module
defaultdict: Type[collections.defaultdict]
glob: module
sys: module
types: Set[nothing]

_Tnamedtuple-Var-name-type-default-help-flags-filename = TypeVar('_Tnamedtuple-Var-name-type-default-help-flags-filename', bound=`namedtuple-Var-name-type-default-help-flags-filename`)

class `namedtuple-Var-name-type-default-help-flags-filename`(tuple):
    __slots__ = ["default", "filename", "flags", "help", "name", "type"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str]
    default: Any
    filename: Any
    flags: Any
    help: Any
    name: Any
    type: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: __builtin__.type[`_Tnamedtuple-Var-name-type-default-help-flags-filename`], name, type, default, help, flags, filename) -> `_Tnamedtuple-Var-name-type-default-help-flags-filename`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: __builtin__.type[`_Tnamedtuple-Var-name-type-default-help-flags-filename`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Var-name-type-default-help-flags-filename`: ...
    def _replace(self: `_Tnamedtuple-Var-name-type-default-help-flags-filename`, **kwds) -> `_Tnamedtuple-Var-name-type-default-help-flags-filename`: ...

def dump(folder) -> None: ...
def main() -> None: ...
def process(filename, args) -> None: ...
