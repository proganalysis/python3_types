# (generated with --quick)

from typing import List

BUILD_FILES: List[str]
BUILD_FOLDERS: List[str]
argparse: module
itertools: module
os: module
subprocess: module

def filter_build_files_and_folders(input) -> list: ...
def filter_deleted_files(input) -> list: ...
def filter_extensions(input, extensions) -> list: ...
def flatten_file_list(file_args) -> list: ...
def get_changed_files(git_reference) -> List[str]: ...
def ignore_extensions(input, extensions) -> list: ...
def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
