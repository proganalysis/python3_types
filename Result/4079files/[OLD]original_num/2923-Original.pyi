# (generated with --quick)

import collections
from typing import Any, Callable, Generator, Iterable, Iterator, List, Set, Tuple, Type, TypeVar, Union

EMPTY_PATH: PathItem
TRIM_MARGIN: int
TRIM_MIN: int
defaultdict: Type[collections.defaultdict]
normalize_seq: Any
sys: module

_T = TypeVar('_T')
_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

class Allele:
    __slots__ = []
    __doc__: str

class HetAltAllele(Allele):
    __slots__ = ["index", "locus", "phase", "seq", "start", "stop"]
    __doc__: str
    index: Any
    locus: Any
    phase: Any
    seq: Any
    start: Any
    stop: Any
    def __init__(self, locus, index, start, stop, seq, phase = ...) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

class HomAltAllele(Allele):
    __slots__ = ["index", "locus", "seq", "start", "stop"]
    __doc__: str
    index: Any
    locus: Any
    phase: None
    seq: Any
    start: Any
    stop: Any
    def __init__(self, locus, index, start, stop, seq) -> None: ...
    def __len__(self) -> Any: ...
    def __repr__(self) -> str: ...

class NocallAllele(Allele):
    __slots__ = ["start", "stop"]
    __doc__: str
    index: None
    phase: None
    seq: str
    start: Any
    stop: Any
    def __init__(self, locus, start, stop) -> None: ...
    def __len__(self) -> Any: ...
    def __repr__(self) -> str: ...

class OverlapError(ValueError):
    __doc__: str

class PathItem:
    __doc__: str
    antiphasesets: Set[int]
    nodes: List[Allele]
    phasesets: Set[int]
    seq: str
    def __init__(self, seq: str, nodes: List[Allele], phasesets: Set[int], antiphasesets: Set[int]) -> None: ...

class RefAllele(Allele):
    __slots__ = ["locus", "ref", "start", "stop"]
    __doc__: str
    index: int
    locus: Any
    phase: None
    ref: Any
    seq: Any
    start: Any
    stop: Any
    def __init__(self, locus, start, stop, ref) -> None: ...
    def __len__(self) -> Any: ...
    def __repr__(self) -> str: ...

def _apply_phase_constrants(alleles: _T0, phasesets, antiphasesets) -> Union[list, _T0]: ...
def _make_alleles(ref, locus, zygosity_constraints) -> Generator[Union[HetAltAllele, HomAltAllele, NocallAllele, RefAllele], Any, None]: ...
def _update_antiphasesets(antiphasesets, add_phasesets, phaseset) -> Any: ...
def _update_phasesets(phasesets, phaseset) -> Any: ...
def combinations(iterable: Iterable[_T], r: int) -> Iterator[Tuple[_T, ...]]: ...
def combinations_with_replacement(iterable: Iterable[_T], r: int) -> Iterator[Tuple[_T, ...]]: ...
@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
def extend_paths(inpaths, alleles) -> Generator[PathItem, Any, None]: ...
def generate_genotypes(paths, zygosity_constraints, debug = ...) -> List[Tuple[Any, Any]]: ...
def generate_genotypes_with_paths(paths, zygosity_constraints, ploidy = ...) -> Generator[tuple, Any, None]: ...
def generate_graph(ref, start: _T1, stop: _T2, loci, debug = ...) -> Tuple[Generator[Tuple[Any, Any, list], Any, None], collections.defaultdict[HetAltAllele, int]]: ...
def generate_paths(graph, feasible_paths = ..., debug = ...) -> List[Tuple[str, List[Allele]]]: ...
def intersect_paths(paths1, paths2) -> Tuple[Generator[Any, Any, None], Generator[Any, Any, None]]: ...
def is_valid_geno(zygosity_constraints, path_nodes) -> Any: ...
def prune_paths(paths, feasible_paths) -> Generator[Any, Any, None]: ...
def trim_ref(ref, start, stop) -> Any: ...
def trim_seq(seq: _T0) -> Union[str, _T0]: ...
