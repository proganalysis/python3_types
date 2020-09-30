from sqlalchemy.sql.compiler import SQLCompiler as SQLCompiler
from sqlalchemy.sql.expression import Insert
from typing import Any

log: Any

class InsertOnDuplicate(Insert): ...

def insert_on_duplicate(tablename: str, values: Any=..., inline: bool=..., **kwargs: Any) -> Any: ...
def monkeypatch_TableClause() -> None: ...
def unmonkeypatch_TableClause() -> None: ...

STARTSEPS: str
ENDSEPS: str
INSERT_FIELDNAMES_REGEX: Any
RE_INSERT_FIELDNAMES: Any

def compile_insert_on_duplicate_key_update(insert: Insert, compiler: SQLCompiler, **kw: Any) -> str: ...

_TEST_CODE: str
