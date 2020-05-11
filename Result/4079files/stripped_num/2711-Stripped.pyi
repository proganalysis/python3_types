# (generated with --quick)

from typing import Any

configparser: module
io: module
logging: module
passgithelper: module
pytest: Any
test_parse_mapping_file_missing: Any
test_parse_mapping_from_xdg: Any
xdg_dir: Any

class TestEntryNameExtractor:
    def test_smoke(self) -> None: ...

class TestRegexSearchExtractor:
    def test_configuration(self) -> None: ...
    def test_configuration_checks_groups(self) -> None: ...
    def test_missing_group(self) -> None: ...
    def test_smoke(self) -> None: ...

class TestScript:
    test_custom_mapping_used: Any
    test_entry_name_is_user: Any
    test_path_used_if_present: Any
    test_path_used_if_present_fails: Any
    test_prefix_skipping: Any
    test_regex_username_selection: Any
    test_select_unknown_extractor: Any
    test_smoke_resolve: Any
    test_username_provided: Any
    test_username_skipped_if_provided: Any
    test_wildcard_matching: Any
    def test_help(self, capsys) -> None: ...
    def test_skip(self, monkeypatch, capsys) -> None: ...

class TestSkippingDataExtractor:
    ExtractorImplementation: type
    def test_smoke(self) -> None: ...
    def test_too_short(self) -> None: ...

class TestSpecificLineExtractor:
    def test_no_such_line(self) -> None: ...
    def test_smoke(self) -> None: ...

def test_handle_skip_exits(monkeypatch) -> None: ...
def test_handle_skip_nothing(monkeypatch) -> None: ...
