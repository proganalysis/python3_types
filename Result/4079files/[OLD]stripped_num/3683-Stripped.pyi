# (generated with --quick)

import pathlib
from typing import Any, Dict, Type

Path: Type[pathlib.Path]
os: module

class Required:
    v_type: Any
    def __init__(self, v_type = ...) -> None: ...

class Settings:
    COOKIE_SECRET: str
    DB_HOST: str
    DB_NAME: str
    DB_PASSWORD: Required
    DB_PORT: str
    DB_USER: str
    MESSAGE_FILE: pathlib.Path
    _ENV_PREFIX: str
    __doc__: str
    _custom_settings: Dict[str, Any]
    def __init__(self, **custom_settings) -> None: ...
    def substitute_environ(self) -> None: ...
