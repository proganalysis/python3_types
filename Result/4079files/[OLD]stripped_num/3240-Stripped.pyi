# (generated with --quick)

from typing import Any, Dict, IO, List, Optional, Pattern, Union

COMMENT_SUBREGEX: Pattern[str]
QUOTE_SUBREGEX: Pattern[str]
QUOTE_TRIPLE_SUBREGEX: Pattern[str]
__all__: List[str]
check_ast: Any
check_modules_regex: Any
check_modulesymbols_regex: Any
check_syntax_regex: Any
code: Union[bytes, str]
f: IO[Union[bytes, str]]
re: module

def detect(files = ..., codestr = ..., ast_checks = ..., modules_checks = ..., modsyms_checks = ..., stop_on_ok_ast = ..., modules_score = ..., symbols_score = ..., verbosity = ...) -> Dict[Any, Dict[str, Any]]: ...
def open(file: Union[_PathLike, bytes, int, str], mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., newline: Optional[str] = ..., closefd: bool = ...) -> IO: ...
def pprint(object: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ..., depth: Optional[int] = ..., *, compact: bool = ...) -> None: ...
def remove_str_comments(code) -> str: ...
