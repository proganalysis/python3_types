# (generated with --quick)

import itertools
from typing import Any, Generator, Iterable, Iterator, List, Optional, Type, TypeVar

chain: Type[itertools.chain]

_T = TypeVar('_T')

def grouper_chunk(n, iterable) -> Generator[itertools.chain[nothing], Any, None]: ...
@overload
def islice(iterable: Iterable[_T], start: Optional[int], stop: Optional[int], step: Optional[int] = ...) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], stop: Optional[int]) -> Iterator[_T]: ...
def libsvm_row(labels, data) -> Generator[List[str], Any, None]: ...
