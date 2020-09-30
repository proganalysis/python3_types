# (generated with --quick)

import click.testing
from typing import Any, Type
import unittest.mock

CliRunner: Type[click.testing.CliRunner]
IParser: Any
MagicMock: Any
ParserEntry: Any
attr: module
doc2dash: Any
errno: module
log: logging.Logger
logging: module
main: Any
os: module
patch: unittest.mock._patcher
pytest: Any
runner: Any
shutil: module
sqlite3: module
sys: module

class TestArguments:
    def test_fails_with_unknown_icon(self, runner, tmpdir, monkeypatch) -> None: ...
    def test_handles_unknown_doc_types(self, tmpdir, runner) -> None: ...
    def test_quiet_and_verbose_conflict(self, runner, tmpdir) -> None: ...

class TestPrepareDocset:
    def test_plist_creation(self, monkeypatch, tmpdir) -> None: ...
    def test_with_index_page(self, monkeypatch, tmpdir) -> None: ...
    def test_with_javascript_enabled(self, monkeypatch, tmpdir) -> None: ...
    def test_with_online_redirect_url(self, monkeypatch, tmpdir) -> None: ...

class TestSetupLogging:
    test_logging: Any
    def test_quiet_and_verbose(self) -> None: ...

class TestSetupPaths:
    def test_add_to_global_overrides_destination(self) -> None: ...
    def test_cleans_name(self, tmpdir) -> None: ...
    def test_deducts_name_with_trailing_slash(self, tmpdir, monkeypatch) -> None: ...
    def test_detects_existing_dest(self, tmpdir, monkeypatch) -> None: ...
    def test_works(self, tmpdir) -> None: ...

def test_normal_flow(monkeypatch, tmpdir, runner) -> None: ...
