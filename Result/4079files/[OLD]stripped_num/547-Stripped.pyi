# (generated with --quick)

from typing import Any, Dict, List, Union

BaseLinter: Any
SortImports: Any
os: module
sys: module

class Linter(Any):
    def allow(self, path) -> Any: ...
    def run(self, path, **meta) -> List[Dict[str, Union[int, str]]]: ...
