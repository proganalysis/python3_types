# (generated with --quick)

import configparser
from typing import Dict, List, Type, TypeVar, Union

SafeConfigParser: Type[configparser.SafeConfigParser]
__all__: List[str]
os: module

_T0 = TypeVar('_T0')

class Config(configparser.SafeConfigParser):
    __doc__: str
    _defaultValue: Dict[str, Dict[str, Union[int, str]]]
    endpoint: Dict[str, Dict[str, str]]
    def __init__(self, fromFile = ..., fromDict = ...) -> None: ...
    def _pathExpand_(self, pathList: _T0) -> _T0: ...
    def _readEnv(self) -> None: ...
    def _setDefaultValue(self) -> None: ...
