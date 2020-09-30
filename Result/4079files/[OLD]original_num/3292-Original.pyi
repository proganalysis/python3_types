# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple

__author__: str
__copyright__: str
common: Any
difflib: module
hashlib: module
time: module
ty: module

class AbstractComparator(object):
    __doc__: str
    conf: Any
    name: Optional[str]
    opts: Any
    def __init__(self, conf: Optional[dict]) -> None: ...
    def compare(self, old: str, old_date: str, new: str, new_date: str, ctx, meta: dict) -> Tuple[bool, Optional[str], Optional[dict]]: ...
    def new(self, new: str, new_date: str, ctx, meta: dict) -> Tuple[str, dict]: ...

class Added(AbstractComparator):
    __doc__: str
    conf: Any
    name: str

class ContextDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Any

class Deleted(AbstractComparator):
    __doc__: str
    conf: Any
    name: str

class Last(AbstractComparator):
    __doc__: str
    conf: Any
    name: str

class NDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Dict[Any, bool]

class UnifiedDiff(AbstractComparator):
    __doc__: str
    conf: Any
    name: str
    opts: Dict[Any, bool]

def _check_changes(ctx, changed_lines: int, old_lines: int, changes_th: Optional[float], min_changed: Optional[float]) -> bool: ...
def _drop_old_hashes(previous_hash: Dict[str, int], days: int) -> Dict[str, int]: ...
def _instr_separator(instr1: str, instr2: Optional[str]) -> str: ...
def _substract_lists(instr1: str, instr2: str) -> Tuple[str, int, int, int]: ...
def get_comparator(name: str, conf: Optional[dict]) -> Optional[AbstractComparator]: ...
def hash_item(item: str) -> str: ...
def hash_strings(inp: List[str]) -> Dict[int, int]: ...
