from sqlalchemy.engine.base import Engine
from typing import Tuple

def is_sqlserver(engine: Engine) -> bool: ...
def get_sqlserver_product_version(engine: Engine) -> Tuple[int]: ...

SQLSERVER_MAJOR_VERSION_2000: int
SQLSERVER_MAJOR_VERSION_2005: int
SQLSERVER_MAJOR_VERSION_2008: int
SQLSERVER_MAJOR_VERSION_2012: int
SQLSERVER_MAJOR_VERSION_2014: int
SQLSERVER_MAJOR_VERSION_2016: int
SQLSERVER_MAJOR_VERSION_2017: int

def is_sqlserver_2008_or_later(engine: Engine) -> bool: ...
