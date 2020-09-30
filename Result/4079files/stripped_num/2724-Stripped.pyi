# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple

DBInterface: Any
collecter: CollectUpdateBookmarks
config: Any
datetime: module
json: module
os: module
pd: Any

class CollectUpdateBookmarks(object):
    __doc__: str
    dbi: Any
    @staticmethod
    def get_bookmarks() -> Tuple[bool, Any]: ...
    @staticmethod
    def get_file_time(dtms) -> Optional[datetime.datetime]: ...
    def main(self) -> bool: ...
    def original_count(self) -> Tuple[bool, int]: ...
    def searcher(self, dict_, folder_name = ..., counter = ..., parent_folder_name = ..., skip = ...) -> List[Dict[str, Any]]: ...
    def transform_json_to_df(self, json_data) -> Any: ...
