# (generated with --quick)

import __builtin__
import collections
from typing import Any, List, Tuple, Type

OrderedDict: Type[collections.OrderedDict]
re: module

class LocalesDict(object):
    _choice_cache: __builtin__.dict[Any, None]
    dict: collections.OrderedDict[nothing, nothing]
    def choose_locale(self, locale) -> None: ...
    def list_locales(self) -> List[None]: ...

class LocalesFlatDict(LocalesDict):
    __doc__: str
    _choice_cache: __builtin__.dict[nothing, nothing]
    dict: collections.OrderedDict[Any, __builtin__.dict]
    def update(self, new_data) -> None: ...

def compare_locales(a, b) -> int: ...
def split_locale(locale) -> Tuple[str, str]: ...
