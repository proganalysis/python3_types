# (generated with --quick)

import requests.exceptions
from typing import Any, Dict, Type, Union
import unittest.mock

HTTPError: Type[requests.exceptions.HTTPError]
Mock: Any
RequestException: Type[requests.exceptions.RequestException]
SSLError: Type[requests.exceptions.SSLError]
TestFetchCountryByIp: Any
USER_AGENT: Any
call: Any
fetch_country_by_ip: Any
fetch_document: Any
fetch_host_ip: Any
fetch_host_ip_and_country: Any
patch: unittest.mock._patcher
pytest: Any
send_document: Any

class TestFetchDocument:
    call_args: Dict[str, Union[int, Dict[str, Any]]]
    test_exception_is_raised_if_both_protocols_fail: Any
    test_exception_is_raised_if_http_fails_and_raise_ssl_errors_true: Any
    test_exception_is_raised_if_url_fails: Any
    test_exception_is_raised_on_network_error: Any
    test_extra_headers: Any
    test_host_is_called_with_https_first_then_http: Any
    test_host_is_sanitized: Any
    test_path_is_sanitized: Any
    test_url_is_called: Any
    def test_raises_without_url_and_host(self) -> None: ...

class TestFetchHostIp:
    test_calls: Any

class TestFetchHostIpAndCountry:
    test_calls: Any

class TestSendDocument:
    call_args: Dict[str, Union[int, Dict[str, Any]]]
    test_headers_in_either_case_are_handled_without_exception: Any
    test_post_called_with_only_one_headers_kwarg: Any
    test_post_is_called: Any
    test_post_raises_and_returns_exception: Any
