from .base import TestCase
from typing import Any

class TestCSSProperties(TestCase):
    def test_normalize(self, js: Any, css: Any) -> None: ...

class TestCSSStyleDeclaration(TestCase):
    css: Any = ...
    def setUp(self) -> None: ...
    def test_init(self) -> None: ...
    def test_set_get_remove(self) -> None: ...
    def test_property_access(self) -> None: ...
    def test_property_access_dash(self) -> None: ...
    def test_property_access_dash_two(self) -> None: ...
    def test_float(self) -> None: ...

class TestCSSParseDecl(TestCase):
    def test_parse_style_order(self, input: Any, css: Any) -> None: ...
    def test_parse_style_unordered(self, input: Any, *csses: Any) -> None: ...

class TestCSSStyleRule(TestCase):
    rule: Any = ...
    def setUp(self) -> None: ...
    def test_blank(self) -> None: ...
    def test_init(self) -> None: ...
    def test_overwrite_style(self) -> None: ...

class TestCSSRuleList(TestCase):
    list: Any = ...
    style: Any = ...
    rule: Any = ...
    def setUp(self) -> None: ...
    def test_blank(self) -> None: ...
    def test_append(self) -> None: ...
    def test_append2(self) -> None: ...

class TestParseRules(TestCase):
    def test_parse_style_rules(self, input: Any, rule: Any) -> None: ...