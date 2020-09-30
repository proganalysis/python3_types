# (generated with --quick)

import filecmp
import pathlib
from typing import Any, Dict, List, Type

Alteration: Any
LOGGER: Any
Path: Type[pathlib.Path]
argparse: module
configparser: module
dircmp: Type[filecmp.dircmp]
os: module
random: module
shutil: module
string: module
sys: module
tempfile: module

class TempDir:
    tmp_dir_list: List[nothing]
    @classmethod
    def ask_delete_tmp(cls) -> None: ...
    @classmethod
    def create(cls) -> str: ...
    @classmethod
    def delete_all(cls) -> None: ...

def diff_files(dcmp, alterations, target) -> None: ...
def fetch_addons(input, type) -> list: ...
def parse_args() -> Dict[str, Any]: ...
def parse_conf(conf_file) -> Dict[str, str]: ...
def verify_path(dir_path, to_check) -> None: ...
