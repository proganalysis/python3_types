# (generated with --quick)

import click.core
import click.exceptions
from typing import Any

DaemonContext: Any
TimeoutPIDLockFile: Any
__version__: Any
cli: click.core.Command
click: module
lockfile: Any
os: module
signal: module
sys: module
traceback: module
typechecked: Any

class NoConsumerException(click.exceptions.UsageError): ...

def find_best_consumer(consumer_module) -> Any: ...
def locate_consumer(module_name, raise_if_not_found = ...) -> Any: ...
def main(as_module: bool = ...) -> None: ...
def prepare_import(path) -> str: ...
def read_pidfile(path) -> int: ...
