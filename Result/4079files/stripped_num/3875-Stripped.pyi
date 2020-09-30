# (generated with --quick)

from typing import Any, Iterator, List, Tuple, Union
import xml.etree.ElementTree

CheckColumnConfiguration: Any
CheckEnvInject: Any
CheckForEmptyShell: Any
CheckJobReferences: Any
CheckShebang: Any
ElementTree: module
EnsureTimestamps: Any
EnsureWorkspaceCleanup: Any
FAILING_SHEBANG_ARGS: List[Union[str, Tuple[str, ...]]]
LintContext: Any
LintResult: Any
Linter: Any
PASSING_SHEBANG_ARGS: Iterator[Tuple[str, ...]]
RunContext: Any
configparser: module
get_config: Any
itertools: module
pytest: Any

class ShellTest:
    _shell_builder_template: str
    _xml_template: str
    def test_non_project_skipped(self) -> None: ...

class TestCheckColumnConfiguration:
    test_linter: Any

class TestCheckEnvInject:
    _template: str
    test_linter: Any
    test_no_properties_configured: Any

class TestCheckForEmptyShell(ShellTest):
    test_linter: Any

class TestCheckJobReferences:
    _config_template: str
    _trigger_builder_template: str
    test_linter: Any
    def test_completely_empty_projects_node(self) -> None: ...

class TestCheckShebang(ShellTest):
    test_multiple_shell_parts: Any
    test_project_with_shell: Any
    test_required_shell_options: Any
    def test_allow_default_shebang_false(self) -> None: ...
    def test_project_with_no_shell_part_skipped(self) -> None: ...

class TestEnsureTimestamps:
    test_linter: Any

class TestEnsureWorkspaceCleanup:
    test_linter: Any

class TestLinter:
    LintTestSubclass: type
    def test_check_and_text_passed_through(self, mocker) -> None: ...
    def test_wrong_root_tag_is_skipped_without_check(self, mocker) -> None: ...

def _elementtree_from_str(xml_string) -> xml.etree.ElementTree.ElementTree: ...
