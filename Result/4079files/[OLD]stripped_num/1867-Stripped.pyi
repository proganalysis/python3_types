# (generated with --quick)

from typing import Any, Dict, List, Optional, Pattern, Tuple

CONFIG_EXT: Any
DictProperty: Any
FileParseError: Any
HOME_DIR: Any
INFO_FILE: Any
SETTINGS_FILE: Any
datetime: module
json: module
os: module
re: module
rm_ext: Any
time: module

class ConfigFile:
    COMMENT_REGEX: Pattern[str]
    SEPARATOR: str
    __doc__: str
    path: Any
    raw_vals: dict
    vals: Any
    def __init__(self, path) -> None: ...
    def read(self) -> None: ...
    @classmethod
    def readline(cls, line) -> Optional[Tuple[Any, Any]]: ...

class JSONFile:
    __doc__: str
    path: Any
    vals: Any
    def __init__(self, path) -> None: ...
    def read(self) -> None: ...
    def write(self) -> None: ...

class ProgramConfigFile(ConfigFile):
    __doc__: str
    _all_keys: List[str]
    _bool_keys: List[str]
    _defaults: Dict[str, str]
    _opt_keys: List[str]
    _req_keys: List[nothing]
    false_vals: List[str]
    path: Any
    raw_vals: dict
    true_vals: List[str]
    vals: Any
    def _check_value(self, key, value) -> Optional[str]: ...
    def check_all(self, check_empty = ..., context = ...) -> None: ...

class ProgramData:
    __doc__: str
    _cfg_file: ProgramConfigFile
    _info_file: ProgramInfoFile
    id_format: Any
    last_sync: Any
    overwrite_always: Optional[bool]
    def __init__(self) -> None: ...
    def generate(self) -> None: ...
    def read(self) -> None: ...
    def write(self) -> None: ...

class ProgramInfoFile(JSONFile):
    __doc__: str
    path: Any
    vals: Any
    def generate(self) -> None: ...
