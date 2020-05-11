# (generated with --quick)

from typing import Any, Pattern

logging: module
re: module
sqldebug: Any

class SQLSummaryFilter(logging.Filter):
    __doc__: str
    _regex_sql: Pattern[str]
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def _count_sql_parameters(record) -> int: ...
    def filter(self, record) -> bool: ...

def setup_logging(sql_logging = ...) -> None: ...
