# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, Optional, Type, TypeVar
import unittest.case

TestCase: Type[unittest.case.TestCase]
configparser: module
os: module
shutil: module
tempfile: module

_T = TypeVar('_T')

class TestBase(unittest.case.TestCase):
    __doc__: str
    copy_pants_into_tmpdir: Callable[..., contextlib._GeneratorContextManager[str]]
    set_pants_cache_to_tmpdir: Callable[..., contextlib._GeneratorContextManager[None]]
    setup_pants_in_tmpdir: Callable[..., contextlib._GeneratorContextManager[str]]
    def create_dummy_build(self, *, parent_folder: str) -> None: ...
    def create_pants_ini(self, *, parent_folder: str, pants_version: str, python_version: Optional[str] = ...) -> None: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
