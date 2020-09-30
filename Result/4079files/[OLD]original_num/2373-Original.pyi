# (generated with --quick)

import configparser
from typing import Dict, Type, TypeVar, Union

CFG_DIR: str
CFG_PATH: str
ConfigParser: Type[configparser.ConfigParser]
DEFAULT_CFG_PATH: str
config: configparser.ConfigParser
os: module

_AnyPath = TypeVar('_AnyPath', str, _PathLike[str])

def check_user_config() -> None: ...
def config_to_dict() -> Dict[str, Dict[str, str]]: ...
def copyfile(src: Union[str, _PathLike[str]], dst: _AnyPath, *, follow_symlinks: bool = ...) -> _AnyPath: ...
def load_config() -> None: ...
def update_config_from_dict(conf) -> None: ...
def write_config() -> None: ...
