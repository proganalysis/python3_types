# (generated with --quick)

import __future__
import configparser
from typing import Any, Dict, IO, Optional, Union

config: Any
context: Any
create_engine: Any
db: Any
engine_from_config: Any
os: module
pool: Any
target_metadata: Any
with_statement: __future__._Feature

def fileConfig(fname: Union[str, configparser.RawConfigParser, _PathLike[str], IO[str]], defaults: Optional[Dict[str, str]] = ..., disable_existing_loggers: bool = ...) -> None: ...
def get_database_url() -> str: ...
def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
