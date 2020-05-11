# (generated with --quick)

from typing import Any, IO, List, Optional, TypeVar, Union
import unittest.case

find_zipfile_member: Any
get_file_listing_sha: Any
match_file_listing: Any
match_files: Any
match_zipfile_members: Any
merge_paths: Any
os: module
strip_file_listing: Any
strip_full_path: Any
unique_listing_directories: Any
unittest: module
zipfile: module

AnyStr = TypeVar('AnyStr', str, bytes)

class TestFileDirectoryListing(unittest.case.TestCase):
    paths: List[str]
    def test_strip_file_listing(self) -> None: ...
    def test_unique_listing_directories(self) -> None: ...

class TestMatchFiles(unittest.case.TestCase):
    pattern: str
    def test_match_files(self) -> None: ...
    def test_match_listings(self) -> None: ...

class TestPathFormatters(unittest.case.TestCase):
    base_path: str
    directory: str
    def test_merge_paths(self) -> None: ...
    def test_strip_full_path(self) -> None: ...

class TestSHA(unittest.case.TestCase):
    def test_get_file_listing_sha(self) -> None: ...

class TestZipPaths(unittest.case.TestCase):
    pattern: str
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def test_find_zipfile_member(self) -> None: ...
    def test_match_zipfile_members(self) -> None: ...

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def mock_file_listing() -> List[str]: ...
def mock_pattern() -> str: ...
def mock_pattern_match() -> List[str]: ...
