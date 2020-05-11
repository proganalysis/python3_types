# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, Type, TypeVar
import unittest.case

TestCase: Type[unittest.case.TestCase]
configparser: module
os: module
shutil: module
tempfile: module

_T = TypeVar('_T')

class TestBase(unittest.case.TestCase):
    __doc__: str
    copy_pants_into_tmpdir: Callable[..., contextlib._GeneratorContextManager]
    set_pants_cache_to_tmpdir: Callable[..., contextlib._GeneratorContextManager]
    setup_pants_in_tmpdir: Callable[..., contextlib._GeneratorContextManager]
    def create_dummy_build(self, *, parent_folder) -> None: ...
    def create_pants_ini(self, *, parent_folder, pants_version, python_version = ...) -> None: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
