# (generated with --quick)

from typing import Any, Pattern

ENDSEPS: str
INSERT_FIELDNAMES_REGEX: str
Insert: Any
RE_INSERT_FIELDNAMES: Pattern[str]
SQLCompiler: Any
STARTSEPS: str
SqlaDialectName: Any
TableClause: Any
_TEST_CODE: str
compile_insert_on_duplicate_key_update: Any
compiles: Any
get_brace_style_log_with_null_handler: Any
log: Any
re: module

class InsertOnDuplicate(Any):
    __doc__: str

def insert_on_duplicate(tablename, values = ..., inline = ..., **kwargs) -> InsertOnDuplicate: ...
def monkeypatch_TableClause() -> None: ...
def unmonkeypatch_TableClause() -> None: ...
