import unittest
from six.moves import filter as filter, input as input, map as map, range as range, zip as zip
from typing import Any

LICENSE_TEMPLATE: Any
LICENSE_RE_PATTERN: Any
SHEBANG: str
ENCODING: str
LICENSE_RE: Any
DIR: Any
REPO_DIR: Any
DOCS_DIR: Any
exclusion: Any
DOCS_DIRS: Any

class TestLicenseHeaders(unittest.TestCase):
    @staticmethod
    def years_of_license_in_file(fh: Any): ...
    @staticmethod
    def whatchanged_parse(whatchanged_output: Any) -> None: ...
    @staticmethod
    def last_change_by_fname(): ...
    def test_license_headers(self): ...

class TestFutureImports(unittest.TestCase):
    excluded: str = ...
    future_imports_pattern: Any = ...
    six_import_pattern: Any = ...
    def test_future_imports(self) -> None: ...
