# (generated with --quick)

import enot.compiler.rebar
import enot.packages.package_builder
import http.client
import mock
import test.abs_test_class
from typing import Any, Type, Union

Builder: Type[enot.packages.package_builder.Builder]
HTTPResponse: Type[http.client.HTTPResponse]
RebarCompiler: Type[enot.compiler.rebar.RebarCompiler]
TestClass: Type[test.abs_test_class.TestClass]
enot: module
os: module
patch: mock._patcher
unittest: module

class ToolsTests(test.abs_test_class.TestClass):
    test_in_cache: Any
    test_in_system: Any
    test_missing: Any
    def __init__(self, method_name) -> None: ...

def ensure_dir(path: str) -> None: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
