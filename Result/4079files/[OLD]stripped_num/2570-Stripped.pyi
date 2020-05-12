# (generated with --quick)

from typing import Any

RegCompare: Any
areg_cluster: Any
areg_robust: Any
areg_std: Any
path: module
pd: Any
pytest: Any
reg: Any

class AregCompare(Any):
    def init(self) -> None: ...
    def test_mss(self) -> None: ...
    def test_r2(self) -> None: ...
    def test_r2_a(self) -> None: ...

class TestAreg_cluster(AregCompare):
    @classmethod
    def setup_class(cls) -> None: ...

class TestAreg_hc1(AregCompare):
    @classmethod
    def setup_class(cls) -> None: ...

class TestAreg_std(AregCompare):
    @classmethod
    def setup_class(cls) -> None: ...
