# (generated with --quick)

from typing import Any

AnalysisPlugin: Any
create_test_file_object: Any
get_config_for_testing: Any
pytest: Any
stub_plugin: Any
test_config: Any
test_determine_script_type_ending: Any
test_determine_script_type_file_type: Any
test_determine_script_type_shebang: Any
test_object: Any

class MockAdmin:
    def register_plugin(self, name, administrator) -> None: ...

def test_determine_script_type_raises(stub_plugin, test_object) -> None: ...
def test_process_object_no_issues(stub_plugin, test_object, monkeypatch) -> None: ...
def test_process_object_not_supported(stub_plugin, test_object) -> None: ...
def test_process_object_this_file(stub_plugin) -> None: ...
