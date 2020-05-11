# (generated with --quick)

import configparser
from typing import Dict, Optional, Type, Union

ConfigParser: Type[configparser.ConfigParser]
config: Config
os: module

class Config(object):
    DEFAULT_VALUE: Dict[str, Dict[str, Optional[Union[float, int, str]]]]
    FILE_PATH: str
    config: configparser.ConfigParser
    value: Dict[str, Dict[str, Optional[Union[float, int, str]]]]
    def _dict_to_config(self) -> None: ...
    def _save_config(self) -> None: ...
    def config_to_dict(self) -> None: ...
    def load_file_or_reset(self) -> None: ...
    def save_value(self) -> None: ...
