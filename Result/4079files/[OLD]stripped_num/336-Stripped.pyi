# (generated with --quick)

import __future__
import configparser
import flask.globals
from typing import Any, Dict, IO, Optional, Union

config: Any
context: Any
current_app: flask.globals._FlaskLocalProxy
engine_from_config: Any
pool: Any
target_metadata: Any
with_statement: __future__._Feature

def fileConfig(fname: Union[str, configparser.RawConfigParser, _PathLike[str], IO[str]], defaults: Optional[Dict[str, str]] = ..., disable_existing_loggers: bool = ...) -> None: ...
def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
