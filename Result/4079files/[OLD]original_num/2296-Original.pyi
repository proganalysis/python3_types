# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, Type, TypeVar
import unittest.case

ConsoleMonitor: Any
ON_WIN: bool
OP_REGISTRY: Any
TestCase: Type[unittest.case.TestCase]
_counter: Iterator
anomaly: Any
create_tmp_file: Callable[..., contextlib._GeneratorContextManager]
datetime: Type[datetime.datetime]
itertools: module
np: module
object_to_qualified_name: Any
os: module
shutil: module
subset_spatial: Any
sys: module
tempfile: module
xr: Any

_T = TypeVar('_T')

class TestExternal(unittest.case.TestCase):
    __doc__: str
    def test_dask(self) -> None: ...
    def test_monitor(self) -> None: ...
    def test_nominal(self) -> None: ...
    def test_partial(self) -> None: ...
    def test_registered(self) -> None: ...
    def test_transform(self) -> None: ...
    def test_validation(self) -> None: ...

class TestInternal(unittest.case.TestCase):
    __doc__: str
    def test_nominal(self) -> None: ...
    def test_registered(self) -> None: ...

def assert_dataset_equal(expected, actual) -> None: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
