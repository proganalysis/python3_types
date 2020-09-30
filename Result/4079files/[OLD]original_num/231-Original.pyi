# (generated with --quick)

from typing import Any, Generator, List
import unittest.case

collections: module
numpy: module
pickle: module
pqkmeans: Any
unittest: module

class TestPQKMeans(unittest.case.TestCase):
    encoder: Any
    def data_source(self, n: int) -> Generator[List[int], Any, None]: ...
    def test_cluster_centers_are_really_nearest(self) -> None: ...
    def test_constructor_with_cluster_center(self) -> None: ...
    def test_fit_and_predict(self) -> None: ...
    def test_just_construction(self) -> None: ...
