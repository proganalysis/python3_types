# (generated with --quick)

from typing import TypeVar

configparser: module
logger: logging.Logger
logging: module
os: module

_T0 = TypeVar('_T0')

def create_if_not_exists() -> None: ...
def get_config_path() -> str: ...
def read_config(config: _T0 = ..., path = ...) -> _T0: ...
def write_config(section_name, section_content, path = ...) -> None: ...
