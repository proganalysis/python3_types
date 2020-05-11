# (generated with --quick)

import pathlib
from typing import Any, Dict, List, Optional, Type, Union

CONFIG_CANDIDATES: List[pathlib.Path]
DEFAULTS: Dict[str, Dict[str, Optional[Union[bool, str, Dict[str, str]]]]]
I3BAR: str
Path: Type[pathlib.Path]
SUFFIX: str
cliMainOverrideMap: Dict[nothing, nothing]
context: Any
copy: module
exc: Any
json: module
log: logging.Logger
logging: module
os: module
pprint: module
shutil: module

class I3configgerConfig:
    CONFIG_NAME: str
    MESSAGES_NAME: str
    PARTIALS_NAME: str
    configPath: pathlib.Path
    messagesPath: pathlib.Path
    partialsPath: pathlib.Path
    payload: Any
    targetPath: pathlib.Path
    def __init__(self, load = ...) -> None: ...
    def __str__(self) -> str: ...
    def get_bar_targets(self) -> Dict[Any, dict]: ...
    def load(self) -> None: ...

class MARK:
    COMMENT: str
    SET: str
    VAR: str

def ensure_i3_configger_sanity() -> None: ...
def fetch(path) -> Any: ...
def freeze(path, obj) -> None: ...
def get_i3wm_config_path() -> pathlib.Path: ...
