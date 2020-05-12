from collections import namedtuple
from typing import Any, Optional

def get_available_port(): ...
def _generate_jjb_config(url: Optional[Any] = ..., password: str = ...): ...

class IntegrationTestRunner:
    def run_test_command(self, command: Any): ...

class ActualJenkinsRunner(IntegrationTestRunner):
    container_id: Any = ...
    image_name: Any = ...
    def __init__(self, image_name: Any) -> None: ...
    def check_docker_output(self, args: Any): ...
    def do_retry(self, func: Any): ...
    def _run_test_without_cleanup(self, tmpdir: Any, config: Any): ...
    def run_test(self, tmpdir: Any, config: Any): ...

class DirectRunner(IntegrationTestRunner):
    def run_test(self, tmpdir: Any, config: Any): ...

class JJBSubcommandRunner(IntegrationTestRunner):
    def run_test(self, tmpdir: Any, config: Any): ...

def runner(request: Any): ...
def test_integration(runner: Any, tmpdir: Any, integration_testcase: Any) -> None: ...

IntegrationTestcase = namedtuple('IntegrationTestcase', ['test_name', 'jobs_yaml', 'expected_output', 'expect_success', 'config', 'runners_to_skip'])

def _get_case_item(key: Any, case_dict: Any, defaults: Any, required: bool = ...): ...
def _parse_case(case_dict: Any, defaults: Any): ...
def _parse_testcases(filenames: Any) -> None: ...
def pytest_generate_tests(metafunc: Any): ...
