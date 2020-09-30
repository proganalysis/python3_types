# (generated with --quick)

import enum
from typing import Any, Generator, Sequence, SupportsFloat, Tuple, Type, TypeVar

Enum: Type[enum.Enum]
random: module
time: module

_T = TypeVar('_T')

class Chromosome:
    Strategy: Any
    __doc__: str
    age: int
    fitness: Any
    genes: Any
    def __init__(self, genes, fitness, Strategy) -> None: ...

class Strategies(enum.Enum):
    __doc__: str
    create: Tuple[int]
    crossover: int
    mutate: Tuple[int]

def _crossover(parent_genes, index, parents, get_fitness, crossover, mutate, generate_parent) -> Any: ...
def _generate_parent(length, gene_set, get_fitness) -> Chromosome: ...
def _get_improvement(new_child, generate_parent, max_age, pool_size, max_seconds) -> Generator[nothing, Any, Any]: ...
def _mutate(parent, gene_set, get_fitness) -> Chromosome: ...
def _mutate_custom(parent, custom_mutate, get_fitness) -> Chromosome: ...
def bisect_left(a: Sequence[_T], x: _T, lo: int = ..., hi: int = ...) -> int: ...
def exp(__x: SupportsFloat) -> float: ...
def get_best(get_fitness, target_len, optimal_fitness, gene_set, display, custom_mutate = ..., custom_create = ..., max_age = ..., pool_size = ..., crossover = ..., max_seconds = ...) -> None: ...
