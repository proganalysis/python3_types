# (generated with --quick)

from typing import Any, Dict, NoReturn, Optional, Tuple, TypeVar

__author__: str
__copyright__: str
common: Any
difflib: module
hashlib: module
time: module
ty: module

_T0 = TypeVar('_T0')
_T2 = TypeVar('_T2')

class AbstractComparator(object):
    __doc__: str
    conf: Any
    name: Optional[str]
    opts: Any
    def __init__(self, conf) -> None: ...
    def compare(self, old, old_date, new, new_date, ctx, meta) -> NoReturn: ...
    def new(self, new: _T0, new_date, ctx, meta) -> Tuple[_T0, Dict[nothing, nothing]]: ...

class Added(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    def compare(self, old, old_date, new, new_date, ctx, meta) -> Tuple[bool, Any, Any]: ...
    def new(self, new: _T0, new_date, ctx, meta) -> Tuple[_T0, Any]: ...

class ContextDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Any
    def compare(self, old, old_date, new, new_date, ctx, meta) -> Tuple[bool, Optional[str], Any]: ...

class Deleted(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    def compare(self, old, old_date, new, new_date, ctx, meta) -> Tuple[bool, Any, Any]: ...

class Last(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    def compare(self, old, old_date, new: _T2, new_date, ctx, meta) -> Tuple[bool, _T2, Any]: ...

class NDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Dict[Any, bool]
    def compare(self, old, old_date, new, new_date, ctx, meta) -> Tuple[bool, Optional[str], Optional[Dict[Any, bool]]]: ...

class UnifiedDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Dict[Any, bool]
    def compare(self, old, old_date, new, new_date, ctx, meta) -> Tuple[bool, Optional[str], Optional[Dict[Any, bool]]]: ...

def _check_changes(ctx, changed_lines, old_lines, changes_th, min_changed) -> bool: ...
def _drop_old_hashes(previous_hash, days) -> dict: ...
def _instr_separator(instr1, instr2) -> Any: ...
def _substract_lists(instr1, instr2) -> Tuple[Any, int, int, int]: ...
def get_comparator(name, conf) -> Any: ...
def hash_item(item) -> str: ...
def hash_strings(inp) -> Dict[Any, int]: ...
