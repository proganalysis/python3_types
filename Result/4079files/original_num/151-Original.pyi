# (generated with --quick)

from typing import Any

KrakenHMAC: Any
binascii: module
pytest: Any

class TestKrakenHMAC:
    expected_headers: Any
    expected_nonce: Any
    expected_signature: Any
    kraken_hmac: Any
    params: Any
    test_signature: Any
    urlpath: Any
    def test_headers(self, kraken_hmac, expected_headers) -> None: ...
    def test_initialize(self, kraken_hmac, params, urlpath, api_config) -> None: ...
    def test_nonce(self, kraken_hmac, expected_nonce) -> None: ...
    def test_wrong_key_or_secret(self, params, urlpath, corrupted_api_config) -> None: ...
