# (generated with --quick)

import collections
from typing import Any, Dict, List, Optional, Tuple, Type

_: List[str]
a: EventDocParser
ast: module
defaultdict: Type[collections.defaultdict]
dont_delete_files: List[nothing]
file: str
files: List[str]
os: module
path: str
paths: List[str]
re: module
root: str
rst_path: str

class EventDocParser(object):
    device_events: collections.defaultdict[nothing, list]
    device_labels: Dict[nothing, nothing]
    file: Any
    file_list: List[nothing]
    rst_path: Any
    def __init__(self, rst_path) -> None: ...
    def build_rst_entry(self, final_dict) -> Tuple[Any, str]: ...
    def create_file(self, event, rst) -> Any: ...
    def parse_args(self, args_string) -> str: ...
    def parse_file(self, file_name) -> None: ...
    def parse_string(self, string) -> Tuple[Optional[str], Optional[str]]: ...
    def string_to_args_dict(self, string, args) -> dict: ...
    def write_index(self) -> None: ...
