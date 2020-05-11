# (generated with --quick)

import typing
from typing import Any, IO, Type
import unittest.case
import unittest.mock

BASE_DIRECTORY: str
Counter: Type[typing.Counter]
MagicMock: Any
PHAB_ACTIVATED_DATA: Any
PHAB_DEFAULT_DATA: Any
PHAB_DISABLED_DATA: Any
directory: str
json: module
os: module
patch: unittest.mock._patcher
reviewers: Any
sys: module
tempfile: module
typing: module
unittest: module

class TestConfig(unittest.case.TestCase):
    config: Any
    config_file: IO[str]
    mock_args: Any
    def test_default_global_json(self) -> None: ...
    def test_read_configs_args(self) -> None: ...
    def test_read_configs_copy(self) -> None: ...
    def test_read_json(self) -> None: ...
    def test_read_malformed_json(self) -> None: ...
    def test_read_unusable(self) -> None: ...

class TestFindArcCommitReviewers(unittest.case.TestCase):
    finder: Any
    def test_multiple_reviews(self) -> None: ...
    def test_no_reviewers(self) -> None: ...
    def test_reviewers(self) -> None: ...

class TestFindLogReviewers(unittest.case.TestCase):
    finder: Any
    test_gets_reviewers: Any
    def check_extract_username_from_shortlog(self, shortlog, email, weight) -> None: ...
    def test_get_changed_files(self) -> None: ...
    def test_gets_generic_emails(self) -> None: ...
    def test_gets_uber_emails(self) -> None: ...
    def test_gets_user_weight(self) -> None: ...

class TestFindReviewers(unittest.case.TestCase):
    finder: Any
    mock_check_count: int
    mock_parse_count: int
    orig_reviewers_limit: Any
    test_check_phabricator_activated: Any
    test_check_phabricator_activated_none: Any
    test_run_command: Any
    test_run_command_empty_response: Any
    def check_extract_username(self, email, expected_user) -> None: ...
    def test_extract_uber_username_from_email(self) -> None: ...
    def test_extract_username_from_generic_email(self) -> None: ...
    def test_filter_phabricator_activated(self) -> None: ...
    def test_get_reviewers(self) -> None: ...

class TestGetReviewers(unittest.case.TestCase):
    test_verbose_reviewers: Any

class TestHistoricalReviewers(unittest.case.TestCase):
    finder: Any
    def test_get_reviewers(self) -> None: ...

class TestLogReviewers(unittest.case.TestCase):
    finder: Any
    def test_get_changed_files(self) -> None: ...

class TestMain(unittest.case.TestCase):
    test_ignore_reviewers: Any
    test_main: Any
    test_phabricator_disabled_reviewers: Any
    test_version: Any

class TestShowReviewers(unittest.case.TestCase):
    test_copy_reviewers: Any
    test_copy_reviewers_no_pbcopy: Any
    test_show_reviewers: Any
