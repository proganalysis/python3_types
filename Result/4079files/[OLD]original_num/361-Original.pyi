# (generated with --quick)

from typing import Any, Iterable, List, Tuple

CONJ: int
Group: Any
IDENT: int
NEG: int
Perm: Any
Symbol: Any
_EXPR: int
_FACTOR: int
_SUM: int
_placeholders: _Placeholders
canon_eldag: Any
conjugate: Any
itertools: module
sympy_key: Any
typing: module
warnings: module

class Eldag:
    __doc__: str
    colours: list
    edges: List[int]
    ia: List[int]
    int_colour: list
    symms: list
    def __init__(self) -> None: ...
    def add_node(self, edges: Iterable[int], symm, colour) -> int: ...
    def canon(self) -> Any: ...

class _Placeholders(dict):
    __doc__: str
    def __missing__(self, key) -> Any: ...

def _build_eldag(sums, factors, symms) -> Tuple[Eldag, List[int]]: ...
def _find_perm(orig, dest) -> Any: ...
def _proc_indices(indices, dumms, eldag) -> list: ...
def canon_factors(sums, factors, symms) -> Tuple[list, list, int]: ...
