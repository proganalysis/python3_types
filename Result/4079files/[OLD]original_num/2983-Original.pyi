# (generated with --quick)

import configparser
from typing import Any, Optional, Type, TypeVar, Union

ConfigParser: Type[configparser.ConfigParser]
os: module
sys: module

_T2 = TypeVar('_T2')

class Configuration:
    config: configparser.ConfigParser
    config_path: Any
    dest_trees: Any
    flora: Any
    gentoo_staging: Any
    kit_fixups: Any
    source_trees: Any
    def __init__(self, filename = ...) -> None: ...
    def base_url(self, repo) -> str: ...
    def branch(self, key) -> str: ...
    def db_connection(self, dbname) -> Optional[str]: ...
    def get_option(self, section, key, default: _T2 = ...) -> Union[str, _T2]: ...
