# (generated with --quick)

import subprocess
import types
from typing import Any, Optional, Tuple, Type

BASEDIR: Optional[str]
PIPE: int
Popen: Type[subprocess.Popen]
STDOUT: int
SimpleNamespace: Type[types.SimpleNamespace]
commands: Any
dir_function: Any
os: module
project_class: Any
project_function: Any
project_function_clean: Any
project_session: Any
pytest: Any
random: module
settings_manager: Any
shutil: module
string: module
suite: Any
test_case: Any
test_execution: Any
test_utils: Any
testdir_class: Any
testdir_function: Any
testdir_session: Any
utils: Any

class Project:
    __doc__: str
    name: Any
    path: str
    settings: Any
    testdir: Any
    testdir_fixture: Any
    def __init__(self, testdir_fixture) -> None: ...
    def activate(self) -> Tuple[Any, str]: ...
    def remove(self) -> None: ...
    def values(self) -> Tuple[Any, str]: ...

class TestDirectory:
    __doc__: str
    basedir: Any
    name: Any
    path: Any
    settings: Any
    def __init__(self, basedir) -> None: ...
    def activate(self) -> str: ...
    def remove(self) -> None: ...

class TestUtils:
    @staticmethod
    def create_empty_file(path, filename) -> None: ...
    @staticmethod
    def create_suite(testdir, project, name, content = ..., tests = ..., processes = ..., browsers = ..., environments = ..., tags = ...) -> None: ...
    @staticmethod
    def create_test(testdir, project, parents, name, content = ...) -> str: ...
    @staticmethod
    def random_numeric_string(length, prefix = ...) -> Any: ...
    @staticmethod
    def random_string(length, prefix = ...) -> Any: ...
    @staticmethod
    def run_command(cmd) -> str: ...
    @staticmethod
    def set_project_setting(testdir, setting, setting_value) -> None: ...

def get_basedir() -> Any: ...
def pytest_addoption(parser) -> None: ...
def pytest_runtest_setup(item) -> None: ...
