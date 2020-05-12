from typing import Any, Optional

__all__: Any
QUOTE_TRIPLE_SUBREGEX: Any
QUOTE_SUBREGEX: Any
COMMENT_SUBREGEX: Any

def remove_str_comments(code: Any): ...
def detect(files: Optional[Any] = ..., codestr: Optional[Any] = ..., ast_checks: bool = ..., modules_checks: bool = ..., modsyms_checks: bool = ..., stop_on_ok_ast: bool = ..., modules_score: int = ..., symbols_score: int = ..., verbosity: int = ...): ...
