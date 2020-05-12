# (generated with --quick)

from typing import Any, Tuple

Engine: Any
ResultProxy: Any
SQLSERVER_MAJOR_VERSION_2000: int
SQLSERVER_MAJOR_VERSION_2005: int
SQLSERVER_MAJOR_VERSION_2008: int
SQLSERVER_MAJOR_VERSION_2012: int
SQLSERVER_MAJOR_VERSION_2014: int
SQLSERVER_MAJOR_VERSION_2016: int
SQLSERVER_MAJOR_VERSION_2017: int
SqlaDialectName: Any
get_dialect_name: Any

def get_sqlserver_product_version(engine) -> Tuple[int]: ...
def is_sqlserver(engine) -> bool: ...
def is_sqlserver_2008_or_later(engine) -> bool: ...
