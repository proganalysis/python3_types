# (generated with --quick)

from typing import Any, Set

InitCommand: Any
ResetCommand: Any
TEST_DIR_PATHS: Set[str]
TEST_FILE_PATHS: Set[str]
TEST_PATHS: Set[str]
command: Any
os: module
pytest: Any
tempfile: module
textwrap: module

def test_files_deleted_from_remote_directory(command) -> None: ...
def test_files_moved_to_local_directory(command) -> None: ...
def test_option_keep_remote(command) -> None: ...
def test_option_no_retrieve(command) -> None: ...
def test_profile_is_deleted(command) -> None: ...
