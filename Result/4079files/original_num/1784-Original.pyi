# (generated with --quick)

import _ast
from typing import Any, Union

Boolean: Any
Environment: Any
List: Any
MAGIC_FRAME_DEPTH: int
Option: Any
RecursiveSearch: Any
Tuple: Any
UnknownConfiguration: Any
ast: module
os: module
sys: module

class Configuration(object):
    _recursive_search: Any
    boolean: Any
    list: Any
    loaders: Any
    option: Any
    tuple: Any
    def __call__(self, item, cast = ..., **kwargs) -> Any: ...
    def __init__(self, loaders = ...) -> None: ...
    @staticmethod
    def eval(node_or_string: Union[str, _ast.AST]) -> Any: ...

def _caller_path() -> str: ...
