# (generated with --quick)

import mock
import requests.models
from typing import Any, List, NoReturn, Type, Union
import unittest.mock

Hook: Any
Response: Type[requests.models.Response]
TestCase: Any
ValidationError: Any
json: module
os: module
patch: Union[mock._patcher, unittest.mock._patcher]
raise_context: Any
settings: Any

class HooksTestCase(Any):
    count: Any
    recipients: List[str]
    scripts: List[str]
    def check_output_error(self, *args, **kwargs) -> NoReturn: ...
    def check_output_run(self, check_data, *args, **kwargs) -> str: ...
    def check_output_run_http(self, method, url, data, **kwargs) -> requests.models.Response: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_http(self) -> None: ...
    def test_script(self) -> None: ...
