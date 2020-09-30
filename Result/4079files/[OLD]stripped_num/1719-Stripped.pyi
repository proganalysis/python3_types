# (generated with --quick)

from typing import Any

TreeBuild: Any

class TestTemplateManagerBase:
    def test_template(self, template_manager) -> None: ...

class TestTreeBuilder:
    def test_render_single_node(self, template_manager, simple_dsl_contract) -> None: ...
    def test_render_two_node(self, template_manager, simple_dsl_contract) -> None: ...
