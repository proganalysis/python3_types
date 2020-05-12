# (generated with --quick)

import collections
from typing import Any, Generator, Type

SEMESTER: Any
Subject: Any
datetime: Type[datetime.datetime]
defaultdict: Type[collections.defaultdict]
json: module
unidecode: Any

class LegacyPipeline(object):
    data: collections.defaultdict
    time_format: str
    def close_spider(self, spider) -> None: ...
    def process_item(self, item, spider) -> Any: ...

def classes(item) -> Generator[list, Any, None]: ...
