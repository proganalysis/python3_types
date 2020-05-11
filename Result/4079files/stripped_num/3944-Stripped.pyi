# (generated with --quick)

from typing import Any, Generator, Iterable, List, Pattern, Tuple

BaseDialect: Any
DEFAULT_CONNECTOR: str
DatabaseException: Any
NO_DEFAULT: Any
UnsupportedOperationException: Any
__path__: Iterable[str]
find_col_expr: Pattern[str]
io: module
md_column: Any
md_index: Any
md_types: Any
re: module

class Sqlite3Dialect(Any):
    __doc__: str
    has_cascade: bool
    has_checkpoints: bool
    has_default: bool
    has_ilike: bool
    has_returns: bool
    has_serial: bool
    has_truncate: bool
    lastval_method: str
    def get_column_sql(self, table_name = ..., *, emitter) -> str: ...
    def get_index_sql(self, table_name = ..., *, emitter) -> str: ...
    def get_primary_key_index_name(self, table_name) -> str: ...
    def get_unique_column_index_name(self, table_name, column_name) -> str: ...
    def get_upsert_sql(self, table_name, *, on_conflict_update = ...) -> Tuple[str, set]: ...
    def transform_rows_to_columns(self, *rows, table_name) -> Generator[Any, Any, None]: ...
    def transform_rows_to_indexes(self, *rows, table_name) -> Generator[Any, Any, None]: ...

def _parse_numeric_params(t) -> List[int]: ...
def extend_path(path: Iterable[str], name: str) -> Iterable[str]: ...
