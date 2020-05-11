# (generated with --quick)

import configparser
from typing import Any, Tuple, Type
import uuid

ConfigParser: Type[configparser.ConfigParser]
path: module

class Config:
    config: configparser.ConfigParser
    config_file: str
    def __init__(self, config_dir) -> None: ...
    def _save(self) -> None: ...
    def read(self, key: tuple) -> Any: ...
    def write(self, key: tuple, val) -> None: ...

class Setting:
    __doc__: str
    analytics: Tuple[str, str, bool]
    ask_file: Tuple[str, str, bool]
    client_interval: Tuple[str, str, int]
    current_version: Tuple[str, str, str]
    last_client: Tuple[str, str, int]
    last_meta: Tuple[str, str, int]
    live_search: Tuple[str, str, bool]
    location: Tuple[str, str, str]
    meta_interval: Tuple[str, str, int]
    update: Tuple[str, str, bool]
    uuid: Tuple[str, str, str]

def uuid4() -> uuid.UUID: ...
