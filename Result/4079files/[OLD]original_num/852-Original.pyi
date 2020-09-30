# (generated with --quick)

import __builtin__
import collections
from typing import Any, List, Optional, Tuple, Type

OrderedDict: Type[collections.OrderedDict]
re: module

class LocalesDict(object):
    _choice_cache: __builtin__.dict[str, Any]
    dict: collections.OrderedDict[nothing, nothing]
    def choose_locale(self, locale: str) -> str: ...
    def list_locales(self) -> List[Optional[str]]: ...

class LocalesFlatDict(LocalesDict):
    __doc__: str
    _choice_cache: __builtin__.dict[nothing, nothing]
    dict: collections.OrderedDict[str, __builtin__.dict[str, str]]
    def update(self, new_data: __builtin__.dict[str, __builtin__.dict[str, str]]) -> None: ...

def compare_locales(a, b) -> int: ...
def split_locale(locale: str) -> Tuple[str, Optional[str]]: ...
