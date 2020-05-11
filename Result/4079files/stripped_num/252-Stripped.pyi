# (generated with --quick)

from typing import Any
import unittest.mock

auth: Any
authenticator: Any
db: Any
errors: Any
patch: unittest.mock._patcher
pytest: Any
user_tokens: Any
users: Any

def test_process_request_bad_header(context_factory) -> None: ...
def test_process_request_basic_auth_valid(context_factory, user_factory) -> None: ...
def test_process_request_bump_login(context_factory, user_factory) -> None: ...
def test_process_request_bump_login_with_token(context_factory, user_token_factory) -> None: ...
def test_process_request_no_header(context_factory) -> None: ...
def test_process_request_token_auth_valid(context_factory, user_token_factory) -> None: ...
