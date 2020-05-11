# (generated with --quick)

from typing import Any

Linter: Any
_filter_config: Any
_get_default_linter_configs: Any
configparser: module
create_mock_for_class: Any
pytest: Any

class TestFilterConfig:
    test_returned_configparser_getlist: Any
    def test_filter_by_prefix(self, mocker) -> None: ...
    def test_sectionproxy_getlist(self, mocker) -> None: ...

class TestGetDefaultLinterConfigs:
    def test_no_linters_returns_empty_dict(self, mocker) -> None: ...
    def test_with_linters(self, mocker) -> None: ...
