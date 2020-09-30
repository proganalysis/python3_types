# (generated with --quick)

import argparse
import contextlib
import timeit
from typing import Any, Callable, Dict, Iterator, List, NoReturn, TextIO, Tuple, Type, TypeVar, Union

ArgumentParser: Type[argparse.ArgumentParser]
DiffEngine: Any
Timer: Type[timeit.Timer]
__cached_test_data_lines: Dict[nothing, nothing]
bench_methods: Dict[str, Tuple[str, str]]
diff: Any
generate_unified_diff: Any
parse_unified_diff: Any
stderr: TextIO
test_data: List[Tuple[str, str]]
textwrap: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def exit(arg: object = ...) -> NoReturn: ...
def main() -> None: ...
def test_data_lines(name, data_dir = ...) -> Any: ...
