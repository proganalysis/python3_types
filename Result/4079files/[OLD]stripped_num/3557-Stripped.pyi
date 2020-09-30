# (generated with --quick)

from typing import Any, Tuple

Node: Any
lang_ast: Any

class Eval(Any):
    args: int
    ast: Any
    char: str
    ignore: bool
    results: None
    def __init__(self, ast) -> None: ...
    def __repr__(self) -> str: ...
    @classmethod
    def accepts(cls, code, accept = ...) -> Tuple[Any, Any]: ...
    def func(self, *args) -> Any: ...
