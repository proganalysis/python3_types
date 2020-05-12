# (generated with --quick)

from typing import Any, Dict, List

BaseLinter: Any
SortImports: Any
os: module
sys: module

class Linter(Any):
    def allow(self, path: str) -> bool: ...
    def run(self, path: str, **meta) -> List[Dict[str, Any]]: ...
