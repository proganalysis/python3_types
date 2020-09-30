# (generated with --quick)

import collections
from typing import Any, Generator, Type, TypeVar

SEMESTER: Any
Subject: Any
datetime: Type[datetime.datetime]
defaultdict: Type[collections.defaultdict]
json: module
unidecode: Any

_T0 = TypeVar('_T0')

class LegacyPipeline(object):
    data: collections.defaultdict
    time_format: str
    def close_spider(self, spider) -> None: ...
    def process_item(self, item: _T0, spider) -> _T0: ...

def classes(item) -> Generator[list, Any, None]: ...
