# (generated with --quick)

from typing import Any

CloudRecoIncludeTargetData: Any
CloudRecoService: Any
MaxNumResultsOutOfRange: Any
MockVWS: Any
VWS: Any
VuforiaDatabase: Any
io: module
pytest: Any
uuid: module

class TestCustomBaseVWQURL:
    __doc__: str
    def test_custom_base_url(self, high_quality_image) -> None: ...

class TestIncludeTargetData:
    __doc__: str
    def test_all(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_default(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_none(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_top(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...

class TestMaxNumResults:
    __doc__: str
    def test_custom(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_default(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_too_many(self, cloud_reco_client, high_quality_image) -> None: ...

class TestQuery:
    __doc__: str
    def test_match(self, vws_client, cloud_reco_client, high_quality_image) -> None: ...
    def test_no_matches(self, cloud_reco_client, high_quality_image) -> None: ...
