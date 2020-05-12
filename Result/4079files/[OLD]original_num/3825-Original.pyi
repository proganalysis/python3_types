# (generated with --quick)

from typing import Any, Callable, Generator, Iterable, Iterator, List, Tuple, TypeVar

__all__: List[str]

_S = TypeVar('_S')
_T = TypeVar('_T')

def group_by(iterable, predicate) -> Generator[Tuple[Any, list], Any, None]: ...
@overload
def groupby(iterable: Iterable[_T], key: Callable[[_T], _S]) -> Iterator[Tuple[_S, Iterator[_T]]]: ...
@overload
def groupby(iterable: Iterable[_T], key: None = ...) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
