# (generated with --quick)

from typing import Any, List, Optional, Tuple

_: List[str]
a: MachineVarDocParser
ast: module
dont_delete_files: List[nothing]
file: str
files: List[str]
os: module
path: str
paths: List[str]
re: module
root: str
rst_path: str

class MachineVarDocParser(object):
    file: Any
    file_list: List[nothing]
    def build_rst_entry(self, final_dict) -> Tuple[Any, str]: ...
    def create_file(self, machine_var, rst) -> Any: ...
    def parse_args(self, args_string) -> str: ...
    def parse_file(self, file_name) -> None: ...
    def parse_string(self, string) -> Tuple[Optional[str], Optional[str]]: ...
    def string_to_args_dict(self, string, args) -> dict: ...
    def write_index(self) -> None: ...
