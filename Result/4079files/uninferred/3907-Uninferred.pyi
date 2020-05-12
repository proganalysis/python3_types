import pathlib
from typing import Any

RIMWORLD_MOD_DIR: str
MOD_NAME: str
MOD_ASSEMBLIES: str

def banner_execute() -> pathlib.Path: ...
def dir_exists(path_str: pathlib, check_absolute: bool=...) -> bool: ...
def main(args: Any): ...
