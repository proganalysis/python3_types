# (generated with --quick)

from typing import Any, Type
import unittest.case
import unittest.mock
import werkzeug.exceptions

BadRequest: Type[werkzeug.exceptions.BadRequest]
ContestHandler: Any
Database: Any
Forbidden: Type[werkzeug.exceptions.Forbidden]
Logger: Any
Utils: Any
patch: unittest.mock._patcher
unittest: module

class TestContestHandler(unittest.case.TestCase):
    handler: Any
    inputid: str
    log_backup: Any
    test_generate_input: Any
    test_generate_input_already_have: Any
    test_generate_input_transaction_broken: Any
    test_submit: Any
    test_submit_broken_transaction: Any
    test_submit_db_broken: Any
    test_sumbit_invalid_source: Any
    test_sumbit_not_matching: Any
    def _insert_data(self, token = ..., task = ...) -> None: ...
    def test_compute_score(self) -> None: ...
    def test_generate_input_invalid_task(self) -> None: ...
    def test_generate_input_invalid_token(self) -> None: ...
    def test_submit_invalid_output(self) -> None: ...
    def test_update_user_score(self) -> None: ...
    def test_update_user_score_less(self) -> None: ...
