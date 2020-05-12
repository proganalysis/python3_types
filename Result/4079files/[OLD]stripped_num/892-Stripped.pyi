# (generated with --quick)

import pathlib
from typing import Any, NoReturn, Type, Union

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
    def __str__(self) -> str: ...

class Remove(Suggestion):
    column: Any
    line: Any
    pos: Any
    token: Any
    tokens: Any
    def __init__(self, pos, tokens) -> None: ...
    def __str__(self) -> str: ...

class Replace(Suggestion):
    column: Any
    fix: Any
    line: Any
    pos: Any
    token: Any
    tokens: Any
    def __init__(self, fix, tokens) -> None: ...
    def __str__(self) -> str: ...

class Suggestion:
    __doc__: str
    def __str__(self) -> NoReturn: ...
    @staticmethod
    def enclose(filename, fix) -> Union[Insert, Remove, Replace]: ...

def format_fix(filename, fix) -> None: ...
def format_line(tokens, insert_space_before = ...) -> str: ...
def get_token_line(pos, tokens) -> Any: ...
def not_implemented() -> NoReturn: ...
