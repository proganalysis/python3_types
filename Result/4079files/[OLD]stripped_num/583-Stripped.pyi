# (generated with --quick)

from typing import Any, Callable, Type, TypeVar
import unittest.case

AioDbFactory: Any
AioMySQLDatabase: Any
AioPostgreSQLDatabase: Any
TestCase: Type[unittest.case.TestCase]

_FT = TypeVar('_FT', bound=Callable)

class AioDbFactoryTest(unittest.case.TestCase):
    def test_Failure(self) -> None: ...
    def test_Postgre(self) -> None: ...
    def test_mysql(self) -> None: ...

def expectedFailure(func: _FT) -> _FT: ...
