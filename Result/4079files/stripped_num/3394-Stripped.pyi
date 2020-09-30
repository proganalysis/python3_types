# (generated with --quick)

import contextlib
from typing import Any, Type
import unittest.case
import werkzeug.test
import werkzeug.wrappers

BaseResponse: Type[werkzeug.wrappers.BaseResponse]
Client: Type[werkzeug.test.Client]
DatabaseError: Any
TestDatabase: Any
closing: Type[contextlib.closing]
components: Any
generate_name: Any
json: module
main: Any
unittest: module
users: Any

class TestUsers(unittest.case.TestCase):
    _old_redis_key: Any
    def test_get_all(self) -> None: ...
    def test_get_all_no_connection(self) -> None: ...

class TestUsersIntegration(unittest.case.TestCase):
    _old_redis_key: Any
    test_get_all: Any
