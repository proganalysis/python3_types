from typing import Any

keywords: Any

def is_alpha(char: str) -> bool: ...
def is_numeric(char: str) -> bool: ...
def is_alpha_num(char: str) -> bool: ...

class LexerError(Exception):
    msg: Any = ...
    lineno: Any = ...
    def __init__(self, msg: Any, lineno: Any) -> None: ...

class Token:
    lexeme: Any = ...
    kind: Any = ...
    length: Any = ...
    lineno: Any = ...
    colno: Any = ...
    def __init__(self, lexeme: Any, kind: Any, length: Any, lineno: Any, colno: Any) -> None: ...
    def __repr__(self, bare: bool = ...): ...

class Lexer:
    buffer: Any = ...
    index: int = ...
    start: int = ...
    lineno: int = ...
    colno: int = ...
    def __init__(self) -> None: ...
    def feed(self, buf: Any) -> None: ...
    def char_next(self) -> str: ...
    def lookahead(self) -> str: ...
    def is_at_end(self) -> bool: ...
    def char_matches(self, char: str) -> bool: ...
    def skip_space(self) -> None: ...
    def skip_line(self) -> None: ...
    def get_tok(self) -> Token: ...
    def tok(self, kind: Any) -> Token: ...
    def identifier(self) -> Token: ...
    def number(self) -> Token: ...
    def string(self) -> Token: ...
