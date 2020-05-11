# (generated with --quick)

import collections
from typing import Any, List, Type, TypeVar

CONSTANTS: Any
OrderedDict: Type[collections.OrderedDict]
__author__: str
__copyright__: str
__credits__: List[str]
__email__: str
__license__: str
__maintainer__: str
__status__: str
__version__: str
logging: module
np: module
os: module
pd: Any
pp: module
sys: module

CollectionsOrderedDict = TypeVar('CollectionsOrderedDict')
PandasDataFrame = TypeVar('PandasDataFrame')

class TextFile:
    _TextFile__logger: logging.Logger
    _TextFile__max_width: Any
    _TextFile__path: Any
    def _TextFile__append_dataframe(self, data, label = ...) -> None: ...
    def _TextFile__append_pretty(self, data) -> None: ...
    def _TextFile__append_pretty_dict(self, data, label = ...) -> None: ...
    def _TextFile__read_array(self, skip) -> List[str]: ...
    def __init__(self, max_width = ...) -> None: ...
    def append(self, data) -> None: ...
    def exists(self) -> bool: ...
    def read(self, skip) -> List[str]: ...
    def reset(self) -> None: ...
    def set(self, path, title, ext) -> None: ...
    def size(self) -> int: ...
