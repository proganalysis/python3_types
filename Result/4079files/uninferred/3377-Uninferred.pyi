from typing import Any

class MockAdmin:
    def register_plugin(self, name: Any, administrator: Any) -> None: ...

def test_config(): ...
def test_object(): ...
def stub_plugin(test_config: Any, monkeypatch: Any): ...
def test_determine_script_type_file_type(mime_and_type: Any, stub_plugin: Any, test_object: Any) -> None: ...
def test_determine_script_type_shebang(shebang_and_type: Any, stub_plugin: Any, test_object: Any) -> None: ...
def test_determine_script_type_ending(ending_and_type: Any, stub_plugin: Any, test_object: Any) -> None: ...
def test_determine_script_type_raises(stub_plugin: Any, test_object: Any) -> None: ...
def test_process_object_not_supported(stub_plugin: Any, test_object: Any) -> None: ...
def test_process_object_this_file(stub_plugin: Any) -> None: ...
def test_process_object_no_issues(stub_plugin: Any, test_object: Any, monkeypatch: Any): ...
