# (generated with --quick)

from typing import Any, Type
import unittest.case

BAD_FENCING_TOPOLOGY: str
BAD_FENCING_TOPOLOGY_REPORTS: list
CRM_VERIFY_ERROR_REPORT: str
TestCase: Type[unittest.case.TestCase]
fixture: Any
get_env_tools: Any
report_codes: Any
verify: Any

class CibAsWholeInvalid(unittest.case.TestCase):
    config: Any
    env_assist: Any
    def assert_raises_invalid_cib_content(self, extra_reports = ...) -> None: ...
    def test_add_following_errors(self) -> None: ...
    def test_continue_on_loadable_cib(self) -> None: ...
    def test_fail_immediately_on_unloadable_cib(self) -> None: ...

class CibAsWholeValid(unittest.case.TestCase):
    config: Any
    env_assist: Any
    def test_fail_on_invalid_fence_topology(self) -> None: ...
    def test_success_on_valid(self) -> None: ...

class CibIsMocked(unittest.case.TestCase):
    def test_success_on_valid_cib(self) -> None: ...

class VerboseMode(unittest.case.TestCase):
    config: Any
    env_assist: Any
    def test_success_on_valid_cib(self) -> None: ...
