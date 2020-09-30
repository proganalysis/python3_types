# (generated with --quick)

from typing import Any

RegCompare: Any
ivreg: Any
liml_cluster: Any
liml_robust: Any
liml_std: Any
path: module
pd: Any
pytest: Any
tsls_cluster: Any

class LimlCompare(Any):
    def init(self) -> None: ...
    def test_kappa(self) -> None: ...
    def test_mss(self) -> None: ...
    def test_r2(self) -> None: ...
    def test_r2_a(self) -> None: ...
    def test_ssr(self) -> None: ...

class TestLIML_cluster(LimlCompare):
    @classmethod
    def setup_class(cls) -> None: ...

class TestLIML_robust(LimlCompare):
    @classmethod
    def setup_class(cls) -> None: ...

class TestLIML_std(LimlCompare):
    @classmethod
    def setup_class(cls) -> None: ...

class TestLIML_tsls(LimlCompare):
    @classmethod
    def setup_class(cls) -> None: ...
