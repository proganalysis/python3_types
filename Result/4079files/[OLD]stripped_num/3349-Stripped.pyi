# (generated with --quick)

from typing import Iterable, Iterator, Optional, TypeVar

_T = TypeVar('_T')

@overload
def islice(iterable: Iterable[_T], start: Optional[int], stop: Optional[int], step: Optional[int] = ...) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], stop: Optional[int]) -> Iterator[_T]: ...
def main(path) -> None: ...
