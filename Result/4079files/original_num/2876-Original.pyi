# (generated with --quick)

import filecmp
import pathlib
from typing import Any, List, Type

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

def diff_files(dcmp: filecmp.dircmp, alterations: list, target: str) -> None: ...
def fetch_addons(input: str, type: str) -> List[str]: ...
def parse_args() -> dict: ...
def parse_conf(conf_file: str) -> dict: ...
def verify_path(dir_path: str, to_check: list) -> None: ...
