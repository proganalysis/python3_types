# (generated with --quick)

from typing import Any

Chunk: Any
Delta: Any
DiffEngine: Any
Patch: Any
T: Any
hashlib: module

class DiffNode:
    __slots__ = ["i", "j", "lastSnake", "prev", "snake"]
    __doc__: str
    i: Any
    j: Any
    lastSnake: Any
    prev: Any
    snake: bool
    def __init__(self, i, j) -> None: ...
    def is_snake(self) -> bool: ...
    def previous_snake(self) -> Any: ...

class MyersEngine(Any):
    hash_optimization: Any
    name: str
    def __init__(self, hash_optimization = ...) -> None: ...
    def __repr__(self) -> str: ...
    def diff(self, original, revised) -> Any: ...

def build_path(original: list, revised: list) -> DiffNode: ...
def build_revision(path: DiffNode, original: list, revised: list) -> Any: ...
def create_diff_node(i, j, prev) -> DiffNode: ...
def create_snake(i, j, prev) -> DiffNode: ...
