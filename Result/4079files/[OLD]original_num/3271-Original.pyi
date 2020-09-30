# (generated with --quick)

from typing import Any, Callable, Type, TypeVar
import unittest.case

TestCase: Type[unittest.case.TestCase]
app: Any
db: Any
flask: module
login: Any
url_next: Any

_FT = TypeVar('_FT', bound=Callable)

class WebTestCase(unittest.case.TestCase):
    app: Any
    test_login_via_github: Callable
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def test_homepage(self) -> None: ...
    def test_logout(self) -> None: ...
    def test_provide_correct_redirect_url(self) -> None: ...

def skipIf(condition: object, reason: str) -> Callable[[_FT], _FT]: ...
