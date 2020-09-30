# (generated with --quick)

from typing import Any, Callable, Iterable, List, Sized, Tuple, Type, TypeVar

NFA = `namedtuple-NFA-state-groups_count-named_groups`

__all__: List[str]
collections: module
fill_groups: Any
greediness: Any
join_atoms: Any
nfa: Any
parse: Any
rpn: Any

_Tnamedtuple-NFA-state-groups_count-named_groups = TypeVar('_Tnamedtuple-NFA-state-groups_count-named_groups', bound=`namedtuple-NFA-state-groups_count-named_groups`)

class `namedtuple-NFA-state-groups_count-named_groups`(tuple):
    __slots__ = ["groups_count", "named_groups", "state"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    groups_count: Any
    named_groups: Any
    state: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-NFA-state-groups_count-named_groups`], state, groups_count, named_groups) -> `_Tnamedtuple-NFA-state-groups_count-named_groups`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-NFA-state-groups_count-named_groups`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-NFA-state-groups_count-named_groups`: ...
    def _replace(self: `_Tnamedtuple-NFA-state-groups_count-named_groups`, **kwds) -> `_Tnamedtuple-NFA-state-groups_count-named_groups`: ...

def _to_nodes(expression: str) -> Any: ...
def to_atoms(expression: str) -> str: ...
def to_nfa(expression: str) -> `namedtuple-NFA-state-groups_count-named_groups`: ...
def to_rpn(expression: str) -> str: ...
