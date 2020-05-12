from typing import Iterator, Optional
from unittest import TestCase

class TestBase(TestCase):
    def copy_pants_into_tmpdir(self) -> Iterator[str]: ...
    def set_pants_cache_to_tmpdir(self) -> Iterator[None]: ...
    def setup_pants_in_tmpdir(self) -> Iterator[str]: ...
    def create_pants_ini(self, parent_folder: str, pants_version: str, *, python_version: Optional[str]=...) -> None: ...
    def create_dummy_build(self, parent_folder: str) -> None: ...
