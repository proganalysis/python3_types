# (generated with --quick)

from typing import Any

handler: Any
http_request: Any
mock: module
mock_exc_info: Any
mock_exc_info_202: Any
mock_exc_info_http: Any

class TestBaseHandler:
    test_log_exception_http_error: Any
    test_log_exception_uncaught: Any
    def test_write_error(self, handler, mock_exc_info) -> None: ...
    def test_write_error_202(self, handler, mock_exc_info_202) -> None: ...
