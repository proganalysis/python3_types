# (generated with --quick)

import __builtin__
import __future__
import itertools
from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, Optional, Pattern, Tuple, Type, TypeVar
import unittest.case

DIR: Any
DOCS_DIR: Any
DOCS_DIRS: List[str]
ENCODING: str
LICENSE_RE: Pattern[str]
LICENSE_RE_PATTERN: str
LICENSE_TEMPLATE: str
REPO_DIR: Any
SHEBANG: str
absolute_import: __future__._Feature
cf_units: Any
chain: Type[itertools.chain]
datetime: Type[datetime.datetime]
division: __future__._Feature
exclusion: List[str]
os: module
print_function: __future__._Feature
range: Type[__builtin__.range]
re: module
subprocess: module
unittest: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')
_T2 = TypeVar('_T2')

class TestFutureImports(unittest.case.TestCase):
    excluded: str
    future_imports_pattern: Pattern[str]
    six_import_pattern: Pattern[str]
    def test_future_imports(self) -> None: ...

class TestLicenseHeaders(unittest.case.TestCase):
    @staticmethod
    def last_change_by_fname() -> Dict[str, Optional[datetime.datetime]]: ...
    def test_license_headers(self) -> None: ...
    @staticmethod
    def whatchanged_parse(whatchanged_output) -> Generator[Tuple[str, Optional[datetime.datetime]], Any, None]: ...
    @staticmethod
    def years_of_license_in_file(fh) -> Optional[Tuple[int, int]]: ...

def filter(function: Optional[Callable[[_T], Any]], iterable: Iterable[_T]) -> Iterator[_T]: ...
def fnmatch(name: AnyStr, pat: AnyStr) -> bool: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def input(prompt: str = ...) -> str: ...
@overload
def map(function, *sequences: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def map(function: Callable[..., _T], *sequences: Iterable) -> Iterator[_T]: ...
@overload
def zip() -> Iterator[nothing]: ...
@overload
def zip(seq1, seq2, seq3, *seqs: Iterable) -> Iterator[tuple]: ...
@overload
def zip(seq1: Iterable, seq2: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def zip(seq1: Iterable[nothing], seq2: Iterable) -> Iterator[nothing]: ...
@overload
def zip(seq1: Iterable[_T]) -> Iterator[Tuple[_T]]: ...
@overload
def zip(seq1: Iterable[_T], seq2: Iterable[_T2]) -> Iterator[Tuple[_T, _T2]]: ...
