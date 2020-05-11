# (generated with --quick)

from typing import Any, Tuple

Code: Any
TRANSLATION_TABLE: Tuple[Tuple[str, str], Tuple[str, str]]
os: module
pathlib: module
pymongo: Any

class GitExplorerBase(object):
    @staticmethod
    def _get_code(file_name) -> Any: ...
    @staticmethod
    def _mongodb_escape(input_string) -> Any: ...
    @staticmethod
    def _mongodb_unescape(input_string) -> Any: ...
    @staticmethod
    def get_gitexplorer_database() -> Any: ...
