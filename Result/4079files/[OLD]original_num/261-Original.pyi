# (generated with --quick)

from typing import Any, Optional, Type
import unittest.case

MoneyBird: Any
OAuthAuthentication: Any
TEST_TOKEN: Optional[str]
TestCase: Type[unittest.case.TestCase]
TokenAuthentication: Any
os: module

class APIConnectionTest(unittest.case.TestCase):
    __doc__: str
    api: Any
    auth: Any
    def test_contacts_roundtrip(self) -> None: ...
    def test_get_administrations(self) -> None: ...

class OAuthAuthenticationTest(unittest.case.TestCase):
    __doc__: str
    auth: Any
    def test_authorize_url(self) -> None: ...
    def test_generate_state(self) -> None: ...
    def test_initial_state(self) -> None: ...

class TokenAuthenticationTest(unittest.case.TestCase):
    __doc__: str
    auth: Any
    def test_initial_state(self) -> None: ...
    def test_session(self) -> None: ...
    def test_set_token(self) -> None: ...

def unquote(string: str, encoding: str = ..., errors: str = ...) -> str: ...
