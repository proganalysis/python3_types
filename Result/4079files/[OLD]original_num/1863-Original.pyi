# (generated with --quick)

import __future__
import configparser
from typing import Any, Dict, IO, Optional, Union

config: Any
context: Any
engine_from_config: Any
migrations: Any
pool: Any
poster: Any
target_metadata: Any
with_statement: __future__._Feature

def fileConfig(fname: Union[str, configparser.RawConfigParser, _PathLike[str], IO[str]], defaults: Optional[Dict[str, str]] = ..., disable_existing_loggers: bool = ...) -> None: ...
def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
