# (generated with --quick)

import pathlib
from typing import Any, NoReturn, Type

Deletion: Any
Edit: Any
Insertion: Any
Path: Type[pathlib.Path]
Substitution: Any
Terminal: Any
Vind: Any
current_language: Any

class Insert(Suggestion):
    column: Any
    insert_after: bool
    insert_before: bool
    line: Any
    pos: Any
    token: Any
    tokens: Any
    def __init__(self, token, pos, tokens) -> None: ...

class Remove(Suggestion):
    column: Any
    line: Any
    pos: Any
    token: Any
    tokens: Any
    def __init__(self, pos, tokens) -> None: ...

class Replace(Suggestion):
    column: Any
    fix: Any
    line: Any
    pos: int
    token: Any
    tokens: Any
    def __init__(self, fix, tokens) -> None: ...

class Suggestion:
    __doc__: str
    column: int
    line: int
    def __str__(self) -> str: ...
    @staticmethod
    def enclose(filename: pathlib.Path, fix) -> Suggestion: ...

def format_fix(filename: pathlib.Path, fix) -> None: ...
def format_line(tokens, insert_space_before = ...) -> str: ...
def get_token_line(pos, tokens) -> Any: ...
def not_implemented() -> NoReturn: ...
