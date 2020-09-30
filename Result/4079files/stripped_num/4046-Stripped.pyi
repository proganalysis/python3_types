# (generated with --quick)

from typing import Any, Dict, List, Set, Tuple, Type, Union
import unit.project_loader.grammar
import unittest.mock

Equals: Any
GrammarBaseTestCase: Type[unit.project_loader.grammar.GrammarBaseTestCase]
compound: Any
grammar: Any
on: Any
patch: unittest.mock._patcher
snapcraft: Any
testtools: Any
to: Any

class CompoundStatementGrammarTestCase(unit.project_loader.grammar.GrammarBaseTestCase):
    scenarios: List[Tuple[str, Dict[str, Union[str, List[Union[str, Dict[str, List[str]], List[Union[str, Dict[str, List[str]]]]]], Set[str]]]]]
    test_compound_statement_grammar: Any

class CompoundStatementInvalidGrammarTestCase(unit.project_loader.grammar.GrammarBaseTestCase):
    scenarios: List[Tuple[str, Dict[str, Any]]]
    def test_on_statement_invalid_grammar(self) -> None: ...
