# (generated with --quick)

from typing import Any, List, Optional

os: module

class FileCrawler(object):
    Treshold_restraint: int
    root_dirs: List[str]
    def _find(self, name, path, target_xright, level) -> Any: ...
    @staticmethod
    def _is_exe(filepath) -> bool: ...
    def find(self, target, target_xright = ...) -> Optional[str]: ...
