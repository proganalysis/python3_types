# (generated with --quick)

import __future__
import _csv
from typing import Any, Generator, Optional

HttpSite: Any
absolute_import: __future__._Feature
csv: module
io: module
re: module

class CsvSite(Any):
    _delim: Optional[str]
    delim: Any
    dialect: Any
    def get_content(self) -> _csv._reader: ...
    def run(self) -> Generator[Any, Any, None]: ...
