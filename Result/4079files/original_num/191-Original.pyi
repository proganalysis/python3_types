# (generated with --quick)

import contextlib
import io
from typing import Any, Match, Optional, Pattern, Type, TypeVar, Union
import unittest.case

Class: Any
Grouping: Any
Statistic: Any
StringIO: Type[io.StringIO]
Tabulate: Any
Var: Any
pd: Any
redirect_stdout: Type[contextlib.redirect_stdout]
saspy: Any
unittest: module

AnyStr = TypeVar('AnyStr', str, bytes)

class TestSASTabulate(unittest.case.TestCase):
    cars: Any
    sas: Any
    def test_classes(self) -> None: ...
    def test_composition_serialization(self) -> None: ...
    def test_hierarchy(self) -> None: ...
    def test_procedure(self) -> None: ...
    def test_stats(self) -> None: ...
    def test_tabulate(self) -> None: ...
    def test_to_dataframe(self) -> None: ...
    def test_vars(self) -> None: ...

def match(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, flags: int = ...) -> Optional[Match[AnyStr]]: ...
