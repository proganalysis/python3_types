# (generated with --quick)

import typing
from typing import Any, Dict, Optional

AccessSpecifier: Any
AstAction: Any
CursorKind: Any
Index: Any
TranslationUnit: Any
_generator: Optional[Generator]
conf: Any
get_fully_qualified_name: Any
itertools: module
os: module
sys: module

class Generator(object):
    two_stage_visit: list
    types: Dict[nothing, nothing]
    @staticmethod
    def _build_tree(file_path, compiler_parameters) -> Node: ...
    def process(self, module, args) -> None: ...

class Node(object):
    access: Any
    c: Any
    children: list
    contextual_unique_name: str
    fully_qualified_name: Any
    parent: Any
    def __getattr__(self, item) -> Any: ...
    def __init__(self, c, parent, access) -> None: ...
    def find_any_child(self, **kwargs) -> None: ...
    def find_child(self, **kwargs) -> None: ...
    def find_children(self, **kwargs) -> typing.Generator[nothing, Any, None]: ...
    def remove(self) -> None: ...
