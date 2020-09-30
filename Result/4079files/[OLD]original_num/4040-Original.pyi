# (generated with --quick)

from typing import Any, Dict

CONFIG_FILENAME: Any
CONFIG_PATH: Any
OPTIONS: Any
configparser: module
os: module
traverse_options: Any

class Config:
    config: dict
    path_to_config: Any
    def __getattr__(self, name) -> Any: ...
    def __init__(self, config_file = ...) -> None: ...
    def get_config(self) -> Dict[str, str]: ...
    @staticmethod
    def get_config_path(config_file) -> Any: ...
    def merge(self, cli) -> None: ...
