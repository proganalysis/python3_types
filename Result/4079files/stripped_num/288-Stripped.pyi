# (generated with --quick)

import numpy
from typing import Any, Iterable, Iterator, Tuple, TypeVar

AxialSymmetricMesh: Any
FloatingBody: Any
LOG: logging.Logger
Mesh: Any
logging: module
np: module

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

class Sphere(Any):
    __doc__: str
    geometric_center: numpy.ndarray
    radius: Any
    volume: Any
    def __init__(self, radius = ..., center = ..., ntheta = ..., nphi = ..., clever = ..., clip_free_surface = ..., name = ...) -> None: ...
    def _generate_clever_sphere_mesh(self, ntheta = ..., nphi = ..., clip_free_surface = ..., name = ...) -> Any: ...
    def _generate_sphere_mesh(self, ntheta, nphi, clip_free_surface = ..., name = ...) -> Any: ...

@overload
def product(iter1: Iterable, iter2: Iterable, iter3: Iterable, iter4: Iterable, iter5: Iterable, iter6: Iterable, iter7: Iterable, *iterables: Iterable) -> Iterator[tuple]: ...
@overload
def product(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5], iter6: Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(*iterables: Iterable, repeat: int = ...) -> Iterator[tuple]: ...
