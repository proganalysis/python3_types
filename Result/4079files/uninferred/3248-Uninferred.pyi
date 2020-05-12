import unittest
from typing import IO
from yamldown import yamldown

def yaml_first_yamldown() -> str: ...
def just_yaml() -> str: ...
def just_md() -> str: ...
def md_first_yamldown() -> str: ...
def buffer_with(contents: str) -> yamldown.Buffer: ...
def string_document(contents: str) -> IO[str]: ...

class TestLoad(unittest.TestCase):
    def test_yaml_start_at_start(self) -> None: ...
    def test_yaml_not_started(self) -> None: ...
    def test_yaml_already_started(self) -> None: ...
    def test_yaml_end_at_end(self) -> None: ...
    def test_yaml_not_ended(self) -> None: ...
    def test_yaml_not_started(self) -> None: ...
    def test_load_yaml_first(self) -> None: ...
    def test_load_md_first(self) -> None: ...

class TestDump(unittest.TestCase):
    def test_dump_yaml_first(self) -> None: ...
    def test_dump_md_first(self) -> None: ...
