# (generated with --quick)

from typing import Any

AcmeChallenge: Any
Http404: Any
RequestFactory: Any
TestCase: Any
detail: Any

class TestAcmeChallenge(Any):
    __doc__: str
    def test_acme_url(self) -> None: ...
    def test_acme_url_no_reverse_match(self) -> None: ...
    def test_challenge(self) -> None: ...
    def test_response(self) -> None: ...
    def test_str(self) -> None: ...

class TestAcmeChallengeViews(Any):
    __doc__: str
    detail_url: str
    expected_challenge: str
    expected_response: str
    expected_response_bytes: bytes
    expected_response_decode: str
    factory: Any
    test_challenge: Any
    def setUp(self) -> None: ...
    def test_detail(self) -> None: ...
    def test_detail_404(self) -> None: ...
