# (generated with --quick)

import __future__
import codecs
import functools
import mock
from typing import Any, List, Type, TypeVar, Union
import unittest.case
import unittest.mock

TestCase: Type[unittest.case.TestCase]
_builtin: str
curdir: str
main: Any
open: functools.partial[nothing]
options: Any
os: module
parse_from_file: Any
partial: Type[functools.partial]
patch: Union[mock._patcher, unittest.mock._patcher]
path: module
print_function: __future__._Feature
subprocess: module
sys: module
test_md: str
test_rst: str
unicode_literals: __future__._Feature

_T = TypeVar('_T')

class TestConvert(unittest.case.TestCase):
    _orig_argv: List[str]
    def test_anonymous_reference_option(self) -> None: ...
    def test_disable_inline_math(self) -> None: ...
    def test_dryrun(self) -> None: ...
    def test_no_file(self) -> None: ...
    def test_overwrite_file(self) -> None: ...
    def test_overwrite_option(self) -> None: ...
    def test_parse_file(self) -> None: ...
    def test_underscore_option(self) -> None: ...
    def test_write_file(self) -> None: ...

def _open(filename: str, mode: str = ..., encoding: str = ..., errors: str = ..., buffering: int = ...) -> codecs.StreamReaderWriter: ...
def copy(x: _T) -> _T: ...
